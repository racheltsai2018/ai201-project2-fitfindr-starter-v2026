"""
The three FitFindr tools.

Each one is a standalone function you can call and test on its own, before any
of them are wired into the loop. Build and test them one at a time — three
untested tools joined by a loop is one problem that looks like six, because you
can't tell which layer is lying to you.

    search_listings(description, size, max_price)  → list[dict]
    suggest_outfit(new_item, wardrobe)             → str
    create_fit_card(outfit, new_item)              → str

All three are stubs right now. They run and they do nothing — that's the
starting position and it's deliberate.

⚠️ Before you write any of them, fill in the **Tool Inventory** section of your
README (Milestone 2). Four lines per tool: what it does, each input with its
type, exactly what it returns, and what it returns when it has nothing to give.
That last line is what your loop branches on. "Returns a list" earns nothing —
the description has to say what is *in* the list.
"""

import re

import config
from generate import generate
from utils.data_loader import load_listings


# ── Tool 1: search_listings ───────────────────────────────────────────────────

def search_listings(
    description: str,
    size: str | None = None,
    max_price: float | None = None,
) -> list[dict]:
    """
    Search the listings data for items matching a description, and optionally a
    size and a price ceiling.

    This is the tool that doesn't call the model, which makes it the easiest one
    to test and the one to move onto MCP in unit 4.

    Args:
        description: keywords describing what the user wants
                     (e.g. "vintage graphic tee").
        size:        a size string to filter by, or None to skip size filtering.
                     Match case-insensitively — "M" should match "S/M".

                     ⚠️ Read the sizes in the data before you reach for a plain
                     substring test. `"s" in "us 9"` is True, and so is
                     `"l" in "xl"`. A filter that returns shoes when someone
                     asked for a small top reads like a broken search, and it
                     will quietly cost you in unit 4 when you test criterion 1.
                     What counts as a size match is part of your spec — decide
                     it and write it into your Tool Inventory.
        max_price:   maximum price, inclusive, or None to skip price filtering.

    Returns:
        A list of matching listing dicts, best match first.
        **Returns an empty list when nothing matches — an empty list, not None,
        and not an exception.** Your loop branches on this.

    Each listing dict has these fields:
        id, title, description, category, style_tags (list), size,
        condition, price (float), colors (list), brand (str or None), platform

    Note that `brand` is None for most listings. That is deliberate and
    realistic — thrift listings often have no brand. If something you write
    assumes a brand is always there, you will find out in unit 4.

    TODO:
        1. Load every listing with load_listings().
        2. Filter by max_price and by size, when each is provided.
        3. Score what's left by keyword overlap with `description`.
        4. Drop anything scoring zero.
        5. Sort by score, highest first, and return the listing dicts —
           at most config.SEARCH_RESULT_LIMIT of them.

    Test it from a terminal before you move on:
        python -c "from tools import search_listings; print(search_listings('graphic tee', max_price=30))"
    """
    #load listing
    listings = load_listings()

    # Filter by price and size first, so we only score what's eligible.
    if max_price is not None:
        listings = [l for l in listings if l["price"] <= max_price]
    if size:
        listings = [l for l in listings if _size_matches(size, l["size"])]

    query_words = set(_tokenize(description))
    if not query_words:
        return []

    scored = []
    for listing in listings:
        #score listing
        score = _score_listing(query_words, listing)
        if score > 0:
            scored.append((score, listing))

    # sorted() is stable, so ties keep the dataset's original order.
    scored.sort(key=lambda pair: pair[0], reverse=True)
    return [listing for _, listing in scored[: config.SEARCH_RESULT_LIMIT]]


# Words too common to say anything about what the user wants.
_STOPWORDS = {"a", "an", "the", "and", "or", "for", "with", "in", "of", "to", "i", "want", "looking", "some"}


def _tokenize(text: str) -> list[str]:
    """Lowercase `text` and split it into words, dropping punctuation and stopwords."""
    words = re.findall(r"[a-z0-9]+", text.lower())
    return [w for w in words if w not in _STOPWORDS]


def _size_tokens(size: str) -> set[str]:
    """Split a size string into whole tokens: "S/M" → {"s", "m"}, "US 9" → {"us", "9"}."""
    return set(re.findall(r"[a-z0-9.]+", size.lower()))


def _size_matches(wanted: str, listing_size: str) -> bool:
    """
    True when every token of the requested size is a whole token of the
    listing's size. "M" matches "S/M" and "M/L"; "S" does not match "US 9";
    "L" does not match "XL" or "W30 L30".
    """
    wanted_tokens = _size_tokens(wanted)
    return bool(wanted_tokens) and wanted_tokens <= _size_tokens(listing_size)


def _score_listing(query_words: set[str], listing: dict) -> int:
    """
    Count how many query words appear in the listing. A hit in the title or
    style tags counts double, because those describe the item most directly.
    """
    strong = set(_tokenize(listing["title"] + " " + " ".join(listing["style_tags"])))
    weak = set(_tokenize(" ".join([
        listing["description"],
        listing["category"],
        " ".join(listing["colors"]),
        listing["brand"] or "",  # brand is None for most listings
    ])))

    score = 0
    for word in query_words:
        if word in strong:
            score += 2
        elif word in weak:
            score += 1
    return score


# ── Tool 2: suggest_outfit ────────────────────────────────────────────────────

def suggest_outfit(new_item: dict, wardrobe: dict) -> str:
    """
    Given a thrifted item and the user's wardrobe, suggest one or two outfits.

    This one calls the model, through `generate()`. You don't need to think
    about rate limits — the adapter handles pacing for you.

    Args:
        new_item: a listing dict — the item the user is considering.
        wardrobe: a wardrobe dict with an 'items' key holding a list of items.
                  **It may be empty.** Handle that.

    Returns:
        A non-empty string with outfit suggestions.
        With an empty wardrobe, return general styling advice rather than
        raising or returning "". Unit 4 has you trigger the empty wardrobe on
        purpose, so decide now what it should do.

    TODO:
        1. Check whether wardrobe['items'] is empty.
        2. If it is, ask the model for general styling ideas for this item.
        3. If it isn't, format the wardrobe items into the prompt and ask for
           specific combinations naming pieces the user already owns.
        4. Return the model's response.

    Test it from a terminal before you move on:
        python -c "from tools import suggest_outfit; from utils.data_loader import get_example_wardrobe, load_listings; print(suggest_outfit(load_listings()[0], get_example_wardrobe()))"
    """
    items = (wardrobe or {}).get("items") or []
    item_text = _describe_listing(new_item)

    if not items:
        # Empty wardrobe: nothing to combine with, so give general advice.
        prompt = (
            f"Someone is considering this thrifted item:\n{item_text}\n\n"
            "We don't know what's in their wardrobe. Suggest one or two outfits "
            "built around this item, naming the kinds of pieces that pair well "
            "with it (e.g. 'straight-leg dark jeans', 'chunky white sneakers'). "
            "Keep it to a short paragraph or a few bullets."
        )
    else:
        wardrobe_text = "\n".join(_describe_wardrobe_item(w) for w in items)
        prompt = (
            f"Someone is considering this thrifted item:\n{item_text}\n\n"
            f"Here is what they already own:\n{wardrobe_text}\n\n"
            "Suggest one or two outfits that pair the new item with specific "
            "pieces from their wardrobe. Refer to wardrobe pieces by name, and "
            "only use pieces from the list above. Keep it to a short paragraph "
            "or a few bullets."
        )

    system = (
        "You are a friendly thrift-store stylist. Give concrete, wearable outfit "
        "ideas. Be specific about colors and silhouettes. No preamble."
    )
    response = generate(prompt, system=system).strip()

    # The contract is a non-empty string, even if the model comes back blank.
    if not response:
        return f"Try pairing the {new_item.get('title', 'item')} with simple basics in neutral colors."
    return response


def _describe_listing(listing: dict) -> str:
    """One readable block describing a listing, skipping fields that are missing."""
    lines = [f"- {listing.get('title', 'Untitled item')}"]
    if listing.get("category"):
        lines.append(f"  category: {listing['category']}")
    if listing.get("colors"):
        lines.append(f"  colors: {', '.join(listing['colors'])}")
    if listing.get("style_tags"):
        lines.append(f"  style: {', '.join(listing['style_tags'])}")
    if listing.get("description"):
        lines.append(f"  description: {listing['description']}")
    return "\n".join(lines)


def _describe_wardrobe_item(item: dict) -> str:
    """One line per wardrobe piece: name, category, colors, tags, and notes if any."""
    parts = [item.get("name", "Unnamed piece")]
    if item.get("category"):
        parts.append(item["category"])
    if item.get("colors"):
        parts.append("colors: " + ", ".join(item["colors"]))
    if item.get("style_tags"):
        parts.append("style: " + ", ".join(item["style_tags"]))
    if item.get("notes"):  # notes is null for many items
        parts.append(f"notes: {item['notes']}")
    return "- " + " | ".join(parts)


# ── Tool 3: create_fit_card ───────────────────────────────────────────────────

def create_fit_card(outfit: str, new_item: dict) -> str:
    """
    Write a short caption someone would actually post about the find.

    This calls the model too.

    Args:
        outfit:   the outfit suggestion string from suggest_outfit().
        new_item: the listing dict for the item.

    Returns:
        A two-to-four sentence caption.
        If `outfit` is empty or whitespace, return a descriptive message rather
        than raising.

    The caption should read like a real post rather than a product description,
    mention the item and its price and platform once each, and be specific about
    the vibe.

    It should also come out **differently for different inputs**. If you run
    this three times on the same item and get three word-for-word identical
    strings, it's one of two things, and both are near the top of `config.py`:

        • CACHE_ENABLED — the adapter handed back an answer it already had
        • TEMPERATURE   — at 0.0 the model gives the same words every time

    TODO:
        1. Guard against an empty or whitespace-only `outfit`.
        2. Build a prompt with the item details and the outfit.
        3. Call generate() and return the response.

    Test it from a terminal before you move on:
        python -c "from tools import create_fit_card; from utils.data_loader import load_listings; print(create_fit_card('jeans and white sneakers', load_listings()[0]))"
    """
    title = new_item.get("title", "this find")

    # No outfit to caption: say so instead of asking the model to invent one.
    if not outfit or not outfit.strip():
        return f"No outfit suggestion was provided for the {title}, so there's nothing to caption yet."

    price = new_item.get("price")
    price_text = f"${price:.2f}" if isinstance(price, (int, float)) else "an unlisted price"
    platform = new_item.get("platform") or "a thrift shop"

    prompt = (
        f"The thrifted item:\n{_describe_listing(new_item)}\n"
        f"  price: {price_text}\n"
        f"  platform: {platform}\n\n"
        f"How it's being styled:\n{outfit.strip()}\n\n"
        "Write a 2-4 sentence social media caption about this find, the way a "
        "real person would post it. The poster bought this item on the platform "
        "(they are not selling it). Mention the item, its price, and the "
        "platform exactly once each. Be specific about the vibe of the outfit. "
        "No hashtag walls, no product-description tone, no quotation marks "
        "around the caption. "
        # Ask for less than the hard limit so most replies fit on the first try.
        f"Keep the whole caption under {config.FIT_CARD_MAX_CHARS - 40} characters, "
        "counting spaces."
    )
    system = (
        "You write casual, authentic captions for thrift-haul posts. Sound like "
        "a person, not a brand. Return only the caption."
    )
    # cache=False so the same item gets a fresh caption each time.
    response = generate(prompt, system=system, cache=False).strip()

    # Too long: ask the model to shorten it, a limited number of times.
    for _ in range(config.FIT_CARD_RETRIES):
        if len(response) <= config.FIT_CARD_MAX_CHARS:
            break
        shorten = (
            f"This caption is {len(response)} characters. Rewrite it in under "
            f"{config.FIT_CARD_MAX_CHARS - 40} characters, counting spaces. Keep "
            f"the item, the price ({price_text}), and the platform ({platform}). "
            f"Return only the caption.\n\n{response}"
        )
        response = generate(shorten, system=system, cache=False).strip()

    # Keep the contract: always return a usable caption.
    if not response:
        response = f"Thrifted this {title} on {platform} for {price_text} and I'm obsessed with how it styles."
    return _trim_caption(response, config.FIT_CARD_MAX_CHARS)


def _trim_caption(text: str, limit: int) -> str:
    """
    Last line of defence for the length limit. Cut at the last full sentence
    that fits; if no sentence fits, cut at a word boundary and add "…".
    """
    text = text.strip()
    if len(text) <= limit:
        return text

    # Last sentence end (. ! ?) at or before the limit.
    cut = max(text.rfind(p, 0, limit) for p in ".!?")
    if cut > 0:
        return text[: cut + 1].strip()

    # No sentence fits: cut at a space, leaving room for the ellipsis.
    cut = text.rfind(" ", 0, limit - 1)
    return text[: cut if cut > 0 else limit - 1].rstrip(" ,;:-") + "…"
