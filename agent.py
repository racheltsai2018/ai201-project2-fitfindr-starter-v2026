"""
The FitFindr planning loop.

This is the file that makes FitFindr an agent rather than a script. It decides
which tool to run next based on what the last one returned.

If your loop calls all three tools no matter what comes back, you have a list
of function calls. A loop looks at the last result before it picks the next
step. **That branch is the graded part of this unit.**

Build and test your three tools in `tools.py` first. Then come here.

    python agent.py          runs both example paths below
"""

import json
import re

import config
import trace
from tools import search_listings, suggest_outfit, create_fit_card
from generate import generate, ModelUnavailable, QuotaGuard
from mcp_client import call_tool


# ── session state ─────────────────────────────────────────────────────────────

def new_session(query: str, wardrobe: dict) -> dict:
    """
    A fresh session for one user interaction.

    The session is the single source of truth for a run. Every tool result goes
    in here, and the next tool reads it back out.

    You could pass values straight from one call to the next. It would work,
    and you would not be able to test it — you can't print a variable you have
    already overwritten. Going through the session is what makes the state
    visible, and unit 4 has you write a criterion about exactly that.

    Add fields if you need them.
    """
    return {
        "query": query,              # what the user typed
        "parsed": {},                # description / size / max_price you pulled out of it
        "parsed_by": None,           # "model", or "regex" if the model couldn't be used
        "search_results": [],        # everything search_listings returned
        "selected_item": None,       # the one you chose — goes into suggest_outfit
        "wardrobe": wardrobe,        # the user's wardrobe
        "outfit_suggestion": None,   # what suggest_outfit returned
        "fit_card": None,            # what create_fit_card returned
        "error": None,               # set when the run ended early
    }


# ── planning loop ─────────────────────────────────────────────────────────────

def run_agent(query: str, wardrobe: dict) -> dict:
    """
    Run the loop once and return the finished session.

    Args:
        query:    what the user asked for, in plain language
                  (e.g. "vintage graphic tee under $30, size M").
        wardrobe: a wardrobe dict — get_example_wardrobe() or
                  get_empty_wardrobe() from utils/data_loader.py.

    Returns:
        The session dict. **Check session["error"] first** — if it isn't None,
        the run ended early and the later fields will still be None.

    ─────────────────────────────────────────────────────────────────────────
    TODO — build this, following the branch rule you wrote in Milestone 2.

      1. Start a session with new_session().

      2. Count the times round the loop, and call trace.check_iterations(count)
         on each one before you go again. It raises when the count passes
         MAX_ITERATIONS in config.py — see trace.py.

      3. Parse the query into a description, a size, and a max_price. Regex,
         string splitting, or asking the model are all fine — say which you
         chose in your README. Put the result in session["parsed"].

      4. Call search_listings() with what you parsed.
         Put the results in session["search_results"].

         ⚠️ THIS IS THE BRANCH. If nothing came back:
              - put a message in session["error"] saying what the user could
                change — "No results" is not that message
              - return the session
              - do NOT call suggest_outfit with nothing

      5. Choose an item — the first result is fine. Put it in
         session["selected_item"].

      6. Call suggest_outfit() with the selected item and the wardrobe.
         Put the result in session["outfit_suggestion"].

      7. Call create_fit_card() with the outfit and the item.
         Put the result in session["fit_card"].

      8. Return the session.

    ─────────────────────────────────────────────────────────────────────────
    IN UNIT 4 you come back and add two things:

      • Trace calls. One per step. `trace.step("search_listings", inputs=...,
        returned=...)` — see trace.py. Your README needs the output.

      • A handler for ModelUnavailable, so a bad key produces a message rather
        than a stack trace. The import is already at the top of this file.
    """
    #start new session
    session = new_session(query, wardrobe)

    # Each pass looks at what the last step produced and picks the next one.
    next_step = "parse"
    count = 0

    while next_step != "done":
        count += 1
        trace.check_iterations(count)
        #parse query
        if next_step == "parse":
            session["parsed"], session["parsed_by"] = parse_query(session["query"])
            trace.step("parse_query", inputs=session["query"], returned=session["parsed"], note=f"parsed by {session['parsed_by']}")
            next_step = "search"
        #search listing
        elif next_step == "search":
            parsed = session["parsed"]
            session["search_results"] = call_tool("search_listings", {
                "description": parsed["description"],
                "size": parsed["size"],
                "max_price": parsed["max_price"],
            })

            # THE BRANCH: nothing matched, so stop here instead of styling nothing.
            if not session["search_results"]:
                session["error"] = _no_results_message(parsed)
                trace.step("search_listings (with MCP)", inputs=parsed, returned=session["search_results"], note="branch: empty, stopping")
                next_step = "done"
            else:
                next_step = "select"

        #choose an item
        elif next_step == "select":
            session["selected_item"] = session["search_results"][0]
            trace.step("select_item", inputs=f"{len(session['search_results'])} results", returned=session["selected_item"], note="selected first result")
            next_step = "suggest"

        #suggest outfit
        elif next_step == "suggest":
            # suggest_outfit handles the empty-wardrobe case itself
            # (general styling advice), so both wardrobe paths continue here.
            session["outfit_suggestion"] = suggest_outfit(
                session["selected_item"], session["wardrobe"]
            )
            trace.step("suggest_outfit", inputs={"item": session["selected_item"].get("title"), "wardrobe_items": len(session["wardrobe"].get("items", []))}, returned=session["outfit_suggestion"])
            next_step = "fit_card"

        #create fit card
        elif next_step == "fit_card":
            session["fit_card"] = create_fit_card(
                session["outfit_suggestion"], session["selected_item"]
            )
            trace.step("create_fit_card", inputs={"item": session["selected_item"].get("title"), "outfit": session["outfit_suggestion"]}, returned=session["fit_card"])
            next_step = "done"

    return session


# ── query parsing ─────────────────────────────────────────────────────────────

# "under $30", "below 30", "less than $30", "max $30", "up to $30", or a bare "$30".
_PRICE_RE = re.compile(
    r"(?:under|below|less than|max(?:imum)?|up to|<)\s*\$?\s*(\d+(?:\.\d+)?)"
    r"|\$\s*(\d+(?:\.\d+)?)",
    re.IGNORECASE,
)

# "size M", "size XXS", "size US 9", "size W30 L32", "in a size 8".
_SIZE_RE = re.compile(
    r"\bsize\s+((?:us\s*)?\d+(?:\.\d+)?|w\d+(?:\s*l\d+)?|x{0,3}[sml]|xxl|xxxl)\b",
    re.IGNORECASE,
)


_PARSE_SYSTEM = (
    "You extract search filters from a shopper's request for secondhand "
    "clothing. Reply with only a JSON object, no code fences, no commentary."
)

_PARSE_PROMPT = """Extract these fields from the request below:

  "description": the item the person wants, as short keywords (e.g. "vintage graphic tee").
                 Leave out price, size, and filler like "looking for".
  "size":        the size they asked for, written the way a listing would show it
                 ("M", "XXS", "US 9", "W30 L32"), or null if they gave none.
                 Turn words into letters: "medium" -> "M", "extra small" -> "XS".
  "max_price":   the most they want to pay, as a number, or null if they gave none.

Request: {query}

JSON:"""


def parse_query(query: str) -> tuple[dict, str]:
    """
    Turn a plain-language query into {"description", "size", "max_price"}.

    Asks the model first. If the model can't be reached, or answers with
    something that isn't usable JSON, falls back to the regex parser so the
    run can still go ahead.

    Returns the parsed dict and which parser produced it: "model" or "regex".
    """
    try:
        return _parse_with_model(query), "model"
    except (ModelUnavailable, QuotaGuard, RuntimeError, ValueError):
        # RuntimeError covers a missing key and rate limits that never cleared;
        # ValueError covers a reply that wasn't the JSON we asked for.
        return _parse_with_regex(query), "regex"


def _parse_with_model(query: str) -> dict:
    """Ask the model for the three fields. Raises ValueError on a bad reply."""
    reply = generate(_PARSE_PROMPT.format(query=query), system=_PARSE_SYSTEM, temperature=0.0)

    # Models sometimes wrap JSON in ```json fences despite being asked not to.
    reply = re.sub(r"^```(?:json)?\s*|\s*```$", "", reply.strip())
    data = json.loads(reply)  # json.JSONDecodeError is a ValueError
    if not isinstance(data, dict):
        raise ValueError(f"expected a JSON object, got {type(data).__name__}")

    description = data.get("description")
    if not isinstance(description, str) or not description.strip():
        raise ValueError("model returned no description")

    size = data.get("size")
    if size is not None and (not isinstance(size, str) or not size.strip()):
        size = None

    max_price = data.get("max_price")
    if max_price is not None:
        max_price = float(max_price)  # raises ValueError on junk like "cheap"

    return {
        "description": description.strip(),
        "size": size.strip().upper() if size else None,
        "max_price": max_price,
    }


def _parse_with_regex(query: str) -> dict:
    """
    Backup parser — no model call. Pull a description, a size, and a max_price
    out of the query with regex. Whatever isn't price or size is left as the
    description.

        "vintage graphic tee under $30, size M"
        → {"description": "vintage graphic tee", "size": "M", "max_price": 30.0}
    """
    max_price = None
    price_match = _PRICE_RE.search(query)
    if price_match:
        max_price = float(price_match.group(1) or price_match.group(2))

    size = None
    size_match = _SIZE_RE.search(query)
    if size_match:
        size = size_match.group(1).upper()

    # Remove the price and size phrases, then tidy leftover punctuation.
    description = _PRICE_RE.sub(" ", query)
    description = _SIZE_RE.sub(" ", description)
    description = re.sub(r"[,;]+", " ", description)
    description = re.sub(r"\s+", " ", description).strip()

    return {"description": description, "size": size, "max_price": max_price}


def _no_results_message(parsed: dict) -> str:
    """Tell the user what they could change, based on which filters they used."""
    suggestions = []
    if parsed["max_price"] is not None:
        suggestions.append(f"raise your budget above ${parsed['max_price']:.0f}")
    if parsed["size"]:
        suggestions.append(f"drop the size filter (size {parsed['size']})")
    suggestions.append("try broader or different words than "
                       f"\"{parsed['description']}\"")

    return (
        f"Nothing matched \"{parsed['description']}\""
        + (f" in size {parsed['size']}" if parsed["size"] else "")
        + (f" under ${parsed['max_price']:.0f}" if parsed["max_price"] is not None else "")
        + ". You could " + ", or ".join(suggestions) + "."
    )


# ── running it directly ───────────────────────────────────────────────────────

def _show(session: dict) -> None:
    if session["error"]:
        print(f"  stopped: {session['error']}")
        print(f"  fit_card is {session['fit_card']!r} — it should still be None here")
        return

    item = session["selected_item"] or {}
    print(f"  found:    {item.get('title')} — ${item.get('price')} on {item.get('platform')}")
    print(f"  outfit:   {session['outfit_suggestion']}")
    print(f"  fit card: {session['fit_card']}")


if __name__ == "__main__":
    from utils.data_loader import get_example_wardrobe

    print("=== A query the data can match ===")
    _show(run_agent(
        query="looking for a vintage graphic tee under $30",
        wardrobe=get_example_wardrobe(),
    ))

    print("\n=== A query it can't ===")
    _show(run_agent(
        query="designer ballgown size XXS under $5",
        wardrobe=get_example_wardrobe(),
    ))

    print(
        "\nThe second one should stop before the fit card. If both paths look "
        "the same,\nthe branch isn't doing anything yet."
    )
