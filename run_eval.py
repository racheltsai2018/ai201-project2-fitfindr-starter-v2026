#!/usr/bin/env python3
"""
Run your scenarios repeatedly and write the results down. ← UNIT 4

    python run_eval.py --label before      five tries, the default
    python run_eval.py --label after       after your improvement
    python run_eval.py --tries 10          more tries

This does the mechanical half of unit 4 for you. It runs every scenario in
`scenarios.py` five separate times, **with caching off** so you get five real
answers, captures the trace and the session for each, and writes it all into
`results/` in the table format the submission asks for.

Five, because your criteria are written out of five — "4 of 5 tries", "5 of 5
tries". One column per try means you count the passes and read the verdict
straight off the row, with no arithmetic in between.

⚠️ What it does NOT do is decide whether a try passed.

That judgment is yours, and it has to be, because it depends on criteria you
wrote. The Verdict column comes out blank and you fill it in from the output
underneath. Deciding what counts as a pass is the lesson — a scorer handed to
you would teach you nothing.

**Two of your three tools call a model, so tries will legitimately differ.**
That is expected here, unlike pair 1. If all five tries come back identical
on a criterion that involves the fit card, check that you're really in test
mode — caching is what usually explains it.
"""

import argparse
import datetime as dt
import sys
import traceback

import config
import scenarios as scenario_module


def run_once(scenario, use_trace=True):
    """One scenario, one try. Returns everything worth recording."""
    from agent import run_agent
    from utils.data_loader import get_example_wardrobe, get_empty_wardrobe
    import trace as trace_module

    wardrobe = (
        get_empty_wardrobe() if scenario["wardrobe"] == "empty" else get_example_wardrobe()
    )

    if use_trace:
        trace_module.start_trace()

    record = {"error": None, "session": None, "trace": "", "crashed": None}

    # "model_offline": True simulates the model being unreachable during query
    # parsing only. agent.py's own `generate` is used only by parse_query, so
    # swapping it leaves suggest_outfit and create_fit_card (tools.py) online.
    import agent as agent_module
    from generate import ModelUnavailable
    real_generate = agent_module.generate
    if scenario.get("model_offline"):
        def _unreachable(*args, **kwargs):
            raise ModelUnavailable("simulated: model unreachable during parsing")
        agent_module.generate = _unreachable

    # "price_failure": True makes estimate_price (tool 4) raise, to check the
    # rest of the run survives it. Criterion 10.
    real_estimate = agent_module.estimate_price
    if scenario.get("price_failure"):
        def _broken_estimate(*args, **kwargs):
            raise RuntimeError("simulated: estimate_price failed")
        agent_module.estimate_price = _broken_estimate

    try:
        record["session"] = run_agent(scenario["query"], wardrobe)
    except Exception as exc:  # noqa: BLE001 — a crash is a result worth logging
        record["crashed"] = f"{type(exc).__name__}: {exc}"
        record["traceback"] = traceback.format_exc()
    finally:
        agent_module.generate = real_generate
        agent_module.estimate_price = real_estimate

    if use_trace:
        record["trace"] = trace_module.get_trace()

    return record


def main():
    parser = argparse.ArgumentParser(description="Run the scenarios and log the results.")
    parser.add_argument("--tries", "--trials", type=int, default=5, dest="tries",
                        help="tries per scenario (default 5, matching your criteria)")
    parser.add_argument("--label", default="", help="a name for this run, e.g. 'before'")
    args = parser.parse_args()

    problems = scenario_module.validate()
    if problems:
        print("scenarios.py has problems:\n", file=sys.stderr)
        for problem in problems:
            print(f"  - {problem}", file=sys.stderr)
        sys.exit(1)

    if not scenario_module.SCENARIOS:
        print("scenarios.py is empty. Milestone 3 starts by filling it in.", file=sys.stderr)
        sys.exit(1)

    if args.tries < 5:
        print(f"⚠️  {args.tries} tries. Your criteria are written out of five.\n")

    # Caching off. Five tries have to be five real answers.
    config.CACHE_ENABLED = False
    print("Cache is OFF for this run — that's deliberate.\n")

    rows = []
    for scenario in scenario_module.SCENARIOS:
        print(f"{scenario['name']}  ({scenario['wardrobe']} wardrobe)")
        print(f"  query: {scenario['query']}")

        tries = []
        for attempt in range(1, args.tries + 1):
            record = run_once(scenario)
            tries.append(record)

            if record["crashed"]:
                print(f"  try {attempt}: CRASHED — {record['crashed']}")
            else:
                session = record["session"] or {}
                if session.get("error"):
                    print(f"  try {attempt}: stopped early — {str(session['error'])[:60]}")
                else:
                    card = (session.get("fit_card") or "")
                    print(f"  try {attempt}: completed — fit card {len(card)} chars")

        rows.append({"scenario": scenario, "tries": tries})
        checker = AUTO_CHECKS.get(scenario.get("criterion"))
        if checker:
            passes = sum(1 for t in tries if checker(t))
            print(f"  criterion {scenario['criterion']}: {passes}/{len(tries)} passed")
        print()

    write_report(rows, args)


def write_report(rows, args):
    config.RESULTS_DIR.mkdir(exist_ok=True)
    stamp = dt.datetime.now().strftime("%Y-%m-%d_%H%M")
    label = f"_{args.label}" if args.label else ""
    path = config.RESULTS_DIR / f"run_{stamp}{label}.md"

    n = args.tries
    headers = " | ".join(f"Try {i}" for i in range(1, n + 1))
    divider = "|".join(["---"] * n)

    lines = [
        f"# Run log{f' — {args.label}' if args.label else ''}",
        "",
        "- Produced by: `run_eval.py::main`",
        "- Loop: `agent.py::run_agent` · tools: `tools.py`",
        f"- Tries per scenario: {n}, caching off",
        f"- Temperature: {config.TEMPERATURE}",
        f"- When: {dt.datetime.now().strftime('%Y-%m-%d %H:%M')}",
        "",
        "Paste the table below into your README. Fill in the Criterion and",
        "Target columns from `criteria.md`, then mark each try PASS or FAIL",
        "from the output underneath and count them for the Verdict.",
        "",
        f"| Criterion | Target | {headers} | Verdict |",
        f"|---|---|{divider}|---|",
    ]

    for row in rows:
        scenario = row["scenario"]
        number = scenario.get("criterion")
        # A scenario with "criterion": None is a diagnostic run, not one of
        # your five. It's marked so you don't paste an unnumbered row into a
        # table the README asks you to number 1-5.
        label_text = (
            f"{number}. {scenario['name']}"
            if number
            else f"{scenario['name']} _(diagnostic — not one of your five)_"
        )
        checker = AUTO_CHECKS.get(number)
        if checker:
            # Criteria 6-10 are deterministic, so they're scored automatically.
            marks = ["PASS" if checker(t) else "FAIL" for t in row["tries"]]
            passes = marks.count("PASS")
            lines.append(f"| {label_text} | 5/5 | {' | '.join(marks)} | "
                         f"{'MET' if passes == n else 'MISSED'} ({passes}/{n}) |")
            continue
        lines.append(f"| {label_text} |  | {' | '.join([' '] * n)} |  |")

    lines += [
        "",
        "> The Try and Verdict columns are blank on purpose. Whether a try",
        "> passed depends on the criterion you wrote, so it's yours to decide.",
        "> Count the passes, then read that count against your target: a row",
        "> targeting 4 of 5 with three PASS cells is MISSED (3/5).",
        "",
        "---",
        "",
        "## What actually happened",
        "",
        "Real output, as text. Paste the relevant parts into your README —",
        "the rubric asks for output, not a description of it.",
        "",
    ]

    for row in rows:
        scenario = row["scenario"]
        lines += [f"### {scenario['name']}", "",
                  f"- Query: `{scenario['query']}`",
                  f"- Wardrobe: {scenario['wardrobe']}", ""]

        for i, record in enumerate(row["tries"], 1):
            lines.append(f"**Try {i}**")
            lines.append("")

            if record["crashed"]:
                lines += ["Crashed:", "", "```", record["crashed"], "```", ""]
                continue

            session = record["session"] or {}
            item = session.get("selected_item") or {}
            lines += [
                f"- stopped early: {'yes — ' + str(session.get('error')) if session.get('error') else 'no'}",
                f"- selected_item: {item.get('title', '(none)')}"
                + (f" (${item.get('price')}, {item.get('platform')})" if item else ""),
                f"- search_results: {len(session.get('search_results') or [])}",
                "",
            ]
            if session.get("parsed_by"):
                lines += [f"- parsed_by: {session['parsed_by']} — parsed: {session.get('parsed')}", ""]
            lines += _price_lines(session)
            if session.get("outfit_suggestion"):
                lines += ["Outfit suggestion:", "", "```",
                          str(session["outfit_suggestion"]), "```", ""]
            if session.get("fit_card"):
                card = str(session["fit_card"])
                lines += ["Fit card:", "", "```", card, "```", "",
                          f"- Character count (including spaces): {len(card)}", ""]
            if record["trace"]:
                lines += ["Trace:", "", "```", record["trace"], "```", ""]

    path.write_text("\n".join(lines), encoding="utf-8")

    import generate

    print(f"Wrote {path.relative_to(config.ROOT)}")
    print(generate.usage())
    print("\nCommit this file. It's the evidence the test actually happened.")

    if not any(r["tries"][0]["trace"] for r in rows):
        print(
            "\nNote: no trace was captured. You haven't added trace.step() calls\n"
            "to run_agent() yet — that's Milestone 2, and the trace is required\n"
            "evidence worth a point."
        )


def _expected_label(price, typical):
    """The 20% rule, recomputed independently of tools.py. Criterion 7."""
    if price is None or not typical:
        return "unknown"
    if price <= typical * 0.8:
        return "good deal"
    if price > typical * 1.2:
        return "overpriced"
    return "fair"


def _price_lines(session):
    """Price-estimate evidence for criteria 6-10."""
    est = session.get("price_estimate")
    if not est:
        return ["- price_estimate: (none)", ""]

    from tools import _tokenize, _score_listing
    from utils.data_loader import load_listings

    typical = est.get("typical_price")
    rated = est.get("rated") or []
    result_ids = {l.get("id") for l in session.get("search_results") or []}
    rated_ids = {r.get("id") for r in rated}
    valid = {"good deal", "fair", "overpriced", "unknown"}

    lines = [
        f"- typical_price: {typical} (sample_size {est.get('sample_size')})",
        f"- every search result rated: {result_ids <= rated_ids} "
        f"({len(rated)} rated / {len(result_ids)} results)",
        f"- all labels valid: {all(r.get('deal') in valid for r in rated)}",
        "",
        "Labels (actual vs. 20% rule):",
        "",
        "| id | title | price | deal | expected | match |",
        "|---|---|---|---|---|---|",
    ]
    for r in rated:
        exp = _expected_label(r.get("price"), typical)
        lines.append(f"| {r.get('id')} | {r.get('title')} | {r.get('price')} | "
                     f"{r.get('deal')} | {exp} | {'yes' if exp == r.get('deal') else 'NO'} |")

    # The listings estimate_price used for typical_price. Criterion 9.
    description = (session.get("parsed") or {}).get("description", "")
    words = set(_tokenize(description))
    comps = [l for l in load_listings() if words and _score_listing(words, l) > 0]
    lines += ["", f"Comparables for '{description}' ({len(comps)}):", ""]
    lines += [f"- {l.get('title')} — ${l.get('price')}" for l in comps]
    lines.append("")
    return lines


# ── automatic PASS/FAIL for criteria 6-10 ─────────────────────────────────────
# These criteria are about estimate_price, which doesn't call a model, so a
# try can be scored mechanically. Each check takes one try's record.

_VALID_LABELS = {"good deal", "fair", "overpriced", "unknown"}


def _estimate(record):
    if record["crashed"]:
        return None, None
    session = record["session"] or {}
    return session, session.get("price_estimate")


def _comparables(session):
    # Recompute exactly what estimate_price priced against: listings matching
    # the description, in the category of the top search result.
    from tools import comparable_listings
    results = session.get("search_results") or []
    category = results[0].get("category") if results else None
    description = (session.get("parsed") or {}).get("description", "")
    return comparable_listings(description, category)


def _check_6(record):
    """Every search result is rated with one of the four labels."""
    session, est = _estimate(record)
    if not est:
        return False
    rated = est.get("rated") or []
    result_ids = {l.get("id") for l in session.get("search_results") or []}
    return (bool(result_ids)
            and result_ids <= {r.get("id") for r in rated}
            and all(r.get("deal") in _VALID_LABELS for r in rated))


def _check_7(record):
    """Every label matches the 20% rule against typical_price."""
    _, est = _estimate(record)
    if not est or not est.get("rated"):
        return False
    typical = est.get("typical_price")
    return all(_expected_label(r.get("price"), typical) == r.get("deal")
               for r in est["rated"])


def _check_8(record):
    """Fewer than 3 comparables: typical_price None, all labels 'unknown', no crash."""
    _, est = _estimate(record)
    if not est or not est.get("rated"):
        return False
    return (est.get("typical_price") is None
            and est.get("sample_size", 0) < 3
            and all(r.get("deal") == "unknown" for r in est["rated"]))


def _check_9(record):
    """Every comparable is in the same category as the selected item."""
    session, est = _estimate(record)
    if not est:
        return False
    category = (session.get("selected_item") or {}).get("category")
    comps = _comparables(session)
    return bool(category) and bool(comps) and all(c.get("category") == category for c in comps)


def _check_10(record):
    """estimate_price failed, yet suggest_outfit and create_fit_card finished."""
    if record["crashed"]:
        return False
    session = record["session"] or {}
    return bool(session.get("outfit_suggestion")) and bool(session.get("fit_card"))


AUTO_CHECKS = {6: _check_6, 7: _check_7, 8: _check_8, 9: _check_9, 10: _check_10}


if __name__ == "__main__":
    main()
