"""
The runs your test needs. ← UNIT 4, MILESTONE 3

Each of your five criteria needs something run against it. A criterion about
the empty-search branch needs an impossible query. One about the fit card needs
the same item run more than once. Working that out is Milestone 3's first step,
and this file is where you write it down.

`run_eval.py` runs everything here five times and writes the run log — five
because your criteria are written out of five.

Three scenarios are filled in to show the shape. Add or change whatever your
own criteria need — these are a starting point, not a fixed set.
"""

SCENARIOS = [
    {
        # A query the data can match. Criterion 1.
        "name": "matching query completes",
        "query": "vintage graphic tee under $30",
        "wardrobe": "example",
        "criterion": 1,
    },
    {
        # A query nothing can match. Criterion 2 — the branch.
        "name": "impossible query stops early",
        "query": "designer ballgown size XXS under $5",
        "wardrobe": "example",
        "criterion": 2,
    },
    {
        # A user with nothing saved. One of unit 4's three failure modes.
        "name": "empty wardrobe",
        "query": "denim jacket under $50",
        "wardrobe": "empty",
        "criterion": None,
    },
    # TODO: add what your criteria 3, 4 and 5 need.
        #
        # Set "criterion" to the number in criteria.md that the scenario tests.
        # "criterion": None means a diagnostic run — useful to have, but it isn't
        # one of your five, and run_eval.py marks it as such in the table.
        #
        # For a state criterion, any normal query works — what you're checking is
        # what ends up in the session, not what the user typed.
        #
        # For a fit-card criterion, you probably want the SAME query listed more
        # than once, or several different items, depending on what your criterion
        # actually says.
    {
        # A normal matching query. Criterion 3 — check that the listing in
        # session["search_results"] has the same id, title and description as
        # the new_item passed into suggest_outfit.
        "name": "search result carried into suggest_outfit",
        "query": "denim jacket size S under $50",
        "wardrobe": "example",
        "criterion": 3,
    },
    {
        # The same item every try. Criterion 4 — the caption is under 280
        # characters and names both the new item and the suggested outfit.
        "name": "fit card under 280 chars, names item + outfit",
        "query": "black leather bomber jacket under $80",
        "wardrobe": "example",
        "criterion": 4,
    },
    {
        # Runs with the model unreachable (see "model_offline" in run_eval.py).
        # Criterion 5 — session["parsed_by"] is "regex" and description,
        # size and max_price are all filled in.
        "name": "regex fallback when model unreachable",
        "query": "silk slip dress size M under $40",
        "wardrobe": "example",
        "criterion": 5,
        "model_offline": True,   # run_eval.py makes every model call fail
    }
]

WARDROBES = ("example", "empty")


def validate() -> list[str]:
    """Complain about anything malformed, before a long run rather than during."""
    problems = []
    for i, scenario in enumerate(SCENARIOS, 1):
        if not scenario.get("query", "").strip():
            problems.append(f"scenario {i} has no query")
        if scenario.get("wardrobe") not in WARDROBES:
            problems.append(
                f"scenario {i} has wardrobe {scenario.get('wardrobe')!r} — "
                f"it should be one of {WARDROBES}"
            )
    return problems
