"""
Tests for Tool 4: estimate_price (listing price fairness).

    python test_price.py

No model calls and no API key needed. Most tests swap in a small fake
dataset so the typical price is known in advance.
"""

import tools
from tools import estimate_price, _deal_label, _median


def _listing(id, title, price, tags=("tee",)):
    return {
        "id": id, "title": title, "description": "", "category": "tops",
        "style_tags": list(tags), "size": "M", "condition": "good",
        "price": price, "colors": [], "brand": None, "platform": "depop",
    }


# Five tees priced 10, 15, 20, 25, 30 → median (typical) price is $20.
FAKE_TEES = [
    _listing("t1", "Graphic Tee", 10.0),
    _listing("t2", "Graphic Tee", 15.0),
    _listing("t3", "Graphic Tee", 20.0),
    _listing("t4", "Graphic Tee", 25.0),
    _listing("t5", "Graphic Tee", 30.0),
    _listing("j1", "Denim Jacket", 80.0, tags=("jacket",)),  # should not count
]


def use_fake_data(listings):
    tools.load_listings = lambda: listings


# ── _deal_label: the three labels and their boundaries (typical $20) ─────────

def test_good_deal():
    assert _deal_label(10.0, 20.0) == "good deal"

def test_good_deal_boundary_exactly_20_percent_below():
    assert _deal_label(16.0, 20.0) == "good deal"

def test_fair_just_above_good_deal_boundary():
    assert _deal_label(16.01, 20.0) == "fair"

def test_fair_at_typical():
    assert _deal_label(20.0, 20.0) == "fair"

def test_fair_boundary_exactly_20_percent_above():
    assert _deal_label(24.0, 20.0) == "fair"

def test_overpriced():
    assert _deal_label(24.01, 20.0) == "overpriced"
    assert _deal_label(50.0, 20.0) == "overpriced"

def test_unknown_without_typical_price():
    assert _deal_label(20.0, None) == "unknown"

def test_unknown_without_listing_price():
    assert _deal_label(None, 20.0) == "unknown"


# ── _median ───────────────────────────────────────────────────────────────────

def test_median_odd():
    assert _median([10, 20, 30]) == 20

def test_median_even():
    assert _median([10, 20, 30, 40]) == 25


# ── estimate_price on fake data ───────────────────────────────────────────────

def test_typical_price_is_median_of_matches():
    use_fake_data(FAKE_TEES)
    result = estimate_price("graphic tee", [])
    assert result["typical_price"] == 20.0
    assert result["sample_size"] == 5  # the jacket doesn't match

def test_rates_each_listing():
    use_fake_data(FAKE_TEES)
    results = [_listing("a", "Graphic Tee", 12.0),
               _listing("b", "Graphic Tee", 21.0),
               _listing("c", "Graphic Tee", 40.0)]
    deals = [r["deal"] for r in estimate_price("graphic tee", results)["rated"]]
    assert deals == ["good deal", "fair", "overpriced"]

def test_keeps_order_and_fields():
    use_fake_data(FAKE_TEES)
    results = [FAKE_TEES[4], FAKE_TEES[0]]
    rated = estimate_price("graphic tee", results)["rated"]
    assert [r["id"] for r in rated] == ["t5", "t1"]  # best match stays first
    assert set(rated[0]) == {"id", "title", "price", "deal"}

def test_too_few_comparables_gives_unknown():
    use_fake_data(FAKE_TEES[:2])  # only 2 tees, minimum is 3
    result = estimate_price("graphic tee", [FAKE_TEES[0]])
    assert result["typical_price"] is None
    assert result["sample_size"] == 2
    assert result["rated"][0]["deal"] == "unknown"

def test_nothing_matches():
    use_fake_data(FAKE_TEES)
    result = estimate_price("ballgown", [])
    assert result == {"typical_price": None, "sample_size": 0, "rated": []}

def test_empty_description():
    use_fake_data(FAKE_TEES)
    result = estimate_price("", [FAKE_TEES[0]])
    assert result["typical_price"] is None
    assert result["rated"][0]["deal"] == "unknown"

def test_empty_listings_returns_empty_rated():
    use_fake_data(FAKE_TEES)
    assert estimate_price("graphic tee", [])["rated"] == []


# ── estimate_price on the real dataset ────────────────────────────────────────

def test_real_data_ignores_budget_filter():
    """The typical price comes from the whole market, not the user's budget."""
    tools.load_listings = ORIGINAL_LOAD
    cheap = tools.search_listings("graphic tee", max_price=15)
    any_price = tools.search_listings("graphic tee")
    assert (estimate_price("graphic tee", cheap)["typical_price"]
            == estimate_price("graphic tee", any_price)["typical_price"])

def test_real_data_every_result_gets_a_valid_label():
    tools.load_listings = ORIGINAL_LOAD
    results = tools.search_listings("vintage graphic tee", max_price=30)
    rated = estimate_price("vintage graphic tee", results)["rated"]
    assert len(rated) == len(results)
    assert all(r["deal"] in {"good deal", "fair", "overpriced", "unknown"} for r in rated)


# ── runner ────────────────────────────────────────────────────────────────────

ORIGINAL_LOAD = tools.load_listings

if __name__ == "__main__":
    tests = [(n, f) for n, f in list(globals().items()) if n.startswith("test_")]
    failed = 0
    for name, fn in tests:
        try:
            fn()
            print(f"  PASS  {name}")
        except AssertionError as e:
            failed += 1
            print(f"  FAIL  {name}  {e}")
        except Exception as e:
            failed += 1
            print(f"  ERROR {name}  {type(e).__name__}: {e}")
        finally:
            tools.load_listings = ORIGINAL_LOAD
    print(f"\n{len(tests) - failed}/{len(tests)} passed")
    raise SystemExit(1 if failed else 0)
