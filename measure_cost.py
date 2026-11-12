#!/usr/bin/env python3
"""
Measure what one FitFindr run costs.

    python measure_cost.py            10 runs (default)
    python measure_cost.py -n 20

Sends each query through serve.py's real /ask route (Flask's test client, so
no server needs to be running), which means every run also writes its normal
line to results/serve_log.jsonl. The cache is turned OFF so every model call
is a real, billed call. Token counts come from Gemini's own usage_metadata on
each response, not from the pricing page.

It also sends two requests that are meant to fail (an empty query and a query
that matches nothing) so the log shows what a failure looks like. Those are
not counted in the average.
"""

import argparse
import os
import statistics

os.environ["AI201_CACHE"] = "0"   # must be set before config is imported

import serve  # noqa: E402 — after the env var on purpose

QUERIES = [
    "vintage graphic tee under $30",
    "black jeans size M",
    "y2k top under $25",
    "cozy sweater",
    "denim jacket under $50",
]


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("-n", type=int, default=10)
    n = parser.parse_args().n

    client = serve.app.test_client()

    # Failures first: these go in the log, not in the average.
    client.post("/ask", json={})
    client.post("/ask", json={"query": "designer ballgown size XXS under $5"})

    rows = []
    for i in range(n):
        q = QUERIES[i % len(QUERIES)]
        before = _log_len()
        client.post("/ask", json={"query": q})
        entry = _last_entry(before)
        rows.append(entry)
        print(f"run {i + 1:>2}/{n}  {entry['duration_s']:>6.2f}s  "
              f"{entry['total_tokens']:>5} tokens  {entry['model_calls']} calls  {q}")

    def avg(key):
        return statistics.mean(r[key] for r in rows)

    print(f"\nAverage over {n} runs (cache off, model {serve.config.MODEL}):")
    print(f"  duration      {avg('duration_s'):.2f} s   "
          f"(min {min(r['duration_s'] for r in rows):.2f}, max {max(r['duration_s'] for r in rows):.2f})")
    print(f"  model calls   {avg('model_calls'):.1f}")
    print(f"  prompt tokens {avg('prompt_tokens'):.0f}")
    print(f"  output tokens {avg('output_tokens'):.0f}")
    print(f"  total tokens  {avg('total_tokens'):.0f}")


def _log_len() -> int:
    try:
        with open(serve.LOG_PATH, encoding="utf-8") as f:
            return sum(1 for _ in f)
    except OSError:
        return 0


def _last_entry(before: int) -> dict:
    import json
    with open(serve.LOG_PATH, encoding="utf-8") as f:
        lines = f.readlines()
    assert len(lines) > before, "the run wrote no log line"
    return json.loads(lines[-1])


if __name__ == "__main__":
    main()
