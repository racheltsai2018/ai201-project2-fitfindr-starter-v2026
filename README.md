# FitFindr

> ### 👋 Start here
>
> **New to this repo? Read [RUNNING.md](RUNNING.md) first** — setup, every
> command, and what to do when something breaks.
>
> Once `python test.py` passes:
>
> ```bash
> python app.py listings --full -n 6      # read the data (Milestone 1)
> python app.py fields                    # what you can filter on
> python app.py ask 'vintage graphic tee under $30'
> ```
>
> All three tools are stubs, so that last command will do nothing useful yet.
> That's the starting position.
>
> **The rest of this file is your submission.** Fill it in as you go.

---

<!-- ─────────────────────────────────────────────────────────────────────────
     HOW TO USE THIS FILE

     This is your submission. Fill each section in as you finish the milestone
     it belongs to — don't leave it all to the end.

     Unit 3 asks for the first five sections. Unit 4 adds the five below them.
     Leave the unit 4 sections alone until then; they're here so you know
     what's coming.

     Everything is pasted as TEXT. No screenshots, no images, no video links.
     A typed block of output gets full credit; a picture of the same output
     gets none.
     ───────────────────────────────────────────────────────────────────────── -->

<!-- ═══════════════════════ UNIT 3 — THE BUILD ═══════════════════════ -->

## What This Does

The FitFindr is an AI agent that takes a user's request and searches the available clothing listings for matching clothings. If clothing matching the user's description is found, the agents will then suggest outfits that goes well with the clothing. In the last step, the agent will geneate a fit card for the user, which can be posted on social media. 


---

## Tool Inventory

### `search_listings`

- **What it does:** Search the listings data for items matching a description, and optionally a size and a price ceiling.
- **Inputs:** 'description' (str), 'size' (str or None), 'max_price' (float or None)
- **Returns:** A list of matching listing dicts, which includes id, title, description, category, style_tags (list), size, condition, price (float), colors (list), brand (str or None), and platform for each listing dict.
- **When it has nothing:** This method will return an empty list when nothing matches.

### `suggest_outfit`

- **What it does:** This method suggest one or two outfits based on the input thrifted item and the user's wardrobe.
- **Inputs:** 'new_item' (dict), 'wardrobe' (dict), 'items' (list) in wardrobe
- **Returns:** A non-empty string with one or two outfit suggestions.
- **When it has nothing:** If the wardrobe is empty, return some general styling advice.

### `create_fit_card`

- **What it does:** This method writes a short captions for the item the user searched for, and the outfit suggestions from the method suggest_outfit.
- **Inputs:** 'outfit' (str), 'new_item' (dict)
- **Returns:** A two to four sentence talking about the item, and the suggested outfits in social media post format.
- **When it has nothing:** If the suggested outfit is empty or whitespace, a descriptive message will be returned. 

---

## Planning Loop

<!-- Your branch rule, stated as a rule — the condition AND both paths — plus
     the file and function that holds it.

     Like this:
       "If search_listings returns an empty list, put a message in the session
        and stop. Otherwise take the first result and go to suggest_outfit."
        — agent.py::run_agent

     The grader checks your code against what you claim here, so the file and
     function have to be real. -->

**Branch rule:**  If search_listings returns an empty list, put a message in the session and stop. Otherwise take the first result and go to suggest_outfit.

If the wardrobe which is an input for 'suggest_outfit' is empty, return general styling advice, and pass the result to 'create_fit_card'. Otherwise, take recommended outfit result and go to 'create_fit_card'

**Where it lives:** `agent.py::run_agent` (the search listing branch rule) and `tools.py::suggest_outfit` (suggest outfit branch rule)

**How the query is parsed:** The query is sent to the model to parse the parameters including 'description', 'size', and 'max_price'. The result will then be saved into session["parsed"].

**What moves through the session:** First, the query is parsed then saved into session["parsed"]. Second, 'search_listing' is called with what is parsed as input, and the generated result from 'search_listing' will be saved into session["search_results"]. If the result from 'search_listing' is "no results", input a message in session["error"]. Third, an item should be selected from the 'search_listing' and saved to session["selected_item"]. Fourth, 'suggest_outfit' will be called and the results will be saved in session["outfit_suggestion"]. Lastly, 'create_fit_card' is called and the result is saved into session["fit_card"]. 

---

## Sample Run

<!-- Two things go here.

     1. One FULL query and its output, pasted as text.
     2. Your three per-tool terminal tests — the command and what it printed. -->

**One full query**

```
$ python app.py ask '...'

Found:    Y2K Baby Tee — Butterfly Print — $18.0 on depop

  Outfit:   * **Y2K Streetwear Contrast:** Pair the pink-and-purple butterfly baby tee with your baggy dark-wash straight-leg jeans to balance the cropped silhouette with a relaxed, low-key bottom. Layer the slightly cropped vintage black denim jacket on top, and finish the look with your chunky white sneakers and the black crossbody bag. 
* **Model-Off-Duty Casual:** Tuck the baby tee into your wide-leg khaki trousers, defined by the brown leather belt to pull in the earth tones. Throw your oversized grey crewneck sweatshirt overyour shoulders or wear it open, and anchor the outfit with your chunky white sneakers for an effortless, texture-mixed everyday vibe.

  Fit card: scored this absolute dream of a butterfly baby tee on depop for $18 and I’m literally obsessed. styled it with baggy dark-wash denim and a heavy black jacket for that perfect y2k contrast. honestly such a good find for the rotation.
```

**The three tools, tested one at a time**

**1. `search_listings`**

```
$ python -c "from tools import search_listings; print(search_listings('graphic tee', max_price=30))"

[{'id': 'lst_002', 'title': 'Y2K Baby Tee — Butterfly Print', 'description': 'Super cute early 2000s baby tee with butterfly graphic. Fitted crop length. Tag says medium but fits like a small.','category': 'tops', 'style_tags': ['y2k', 'vintage', 'graphic tee', 'cottagecore'], 'size': 'S/M', 'condition': 'excellent', 'price': 18.0, 'colors': ['white', 'pink', 'purple'], 'brand': None, 'platform': 'depop'},
 {'id': 'lst_006', 'title': 'Graphic Tee — 2003 Tour Bootleg Style', 'description': 'Vintage-style bootleg tee with faded graphic. Slightly boxy fit. 100% cotton, soft and worn-in.', 'category': 'tops', 'style_tags': ['graphic tee', 'vintage', 'grunge', 'streetwear', 'band tee'], 'size': 'L', 'condition': 'good', 'price': 24.0, 'colors': ['black'], 'brand': None, 'platform': 'depop'},
 {'id': 'lst_033', 'title': 'Vintage Band Tee — Faded Grey', 'description': 'Faded grey band-style tee with distressed graphic. Crew neck. Fits boxy. Well-loved but no holes or major damage.', 'category': 'tops', 'style_tags': ['vintage', 'grunge', 'band tee', 'graphic tee', 'streetwear'], 'size': 'L', 'condition': 'fair', 'price': 19.0, 'colors': ['grey', 'charcoal'], 'brand': None, 'platform': 'depop'},
 {'id': 'lst_015', 'title': 'Vintage Graphic Hoodie — Faded Black', 'description': 'Faded black pullover hoodie with barely-visible vintage graphic on the chest. Cozy interior. Some pilling but adds to the worn-in look.', 'category': 'tops', 'style_tags': ['vintage', 'grunge', 'graphic', 'streetwear'], 'size': 'L', 'condition': 'fair', 'price': 26.0, 'colors': ['black', 'charcoal'], 'brand': None, 'platform': 'depop'},
 {'id': 'lst_017', 'title': 'Mesh Long-Sleeve Top — Black', 'description': 'Sheer black mesh long-sleeve. Great for layering under a graphic tee or over a bralette. Stretchy material, fits true to size.', 'category': 'tops', 'style_tags': ['y2k', 'grunge', 'goth', 'layering'], 'size': 'S/M', 'condition': 'excellent', 'price': 15.0, 'colors': ['black'], 'brand': None, 'platform': 'depop'},
 {'id': 'lst_011', 'title': 'Low-Rise Cargo Pants — Khaki', 'description': 'Y2K era low-rise cargo pants. Lots of pockets. Khaki color, slightly distressed at the hems. Great for layering with a long tee.', 'category': 'bottoms', 'style_tags': ['y2k', 'cargo', '2000s', 'streetwear'], 'size': 'W29', 'condition': 'fair', 'price': 27.0, 'colors': ['khaki', 'tan'], 'brand': None, 'platform': 'poshmark'}]
```

**2. `suggest_outfit`**

```
$ python -c "from tools import suggest_outfit; from utils.data_loader import get_example_wardrobe, load_listings; print(suggest_outfit(load_listings()[0], get_example_wardrobe()))"

* **The Casual Sporty Look:** Tuck your white ribbed tank top into the vintage Levi's 501 jeans, cinched at the waist with the brown leather belt. Layer the black cropped zip hoodie on top, and finish the outfit with the chunky white sneakers and the black crossbody bag for an easy, street-style-ready daytime vibe.
* **The Grunge Contrast Look:** Pair the Levi's 501 jeans with the oversized grey crewneck sweatshirt let loose over the waistband. Add the vintage black denim jacket as a layer, ground the outfit with the black combat boots, and sling the black crossbody bag across your chest for a cool, textured mix of denim and grey.
```

**3. `create_fit_card`**

```
$ python -c "from tools import create_fit_card; from utils.data_loader import load_listings; print(create_fit_card('jeans and white sneakers', load_listings()[0]))"

Finally tracked down the ultimate pair of vintage Levi's 501 jeans on Depop for just $38. The knee fading is so good and they just fit right. Tossed them on with fresh white sneakers for that effortlessly lazy Sunday running errands look.
```

---

## How I Used AI

<!-- Two specific moments. What you asked, what came back, what you changed.

     "I used Claude to help me code" is not enough.

     "I gave Claude my search_listings spec. It returned None on no match
     instead of an empty list, so I changed it" is the level we want. -->

**Moment 1**

- *What I asked for:* I asked claude to help me with parsing the query.
- *What came back:* I wrote a method with parsing the query with Regex.
- *What I changed:* However, I wanted to parse with the model, so another method for parsing with the model is written with the prompt, and parsing with regex is used as a backup method when the model is not accessible. 

**Moment 2**

- *What I asked for:* I asked Claude to help me the `agent.py::run_agent` method. 
- *What came back:* Since it was not specified when entering the prompt, Claude passed arguments directly between function calls instead of storing them in the session. 
- *What I changed:* Instead of passing the arguments directly between function calls, the values are saved to the session and retrieved from session. 

**Unit 4**
- *What I asked for:* I asked Claude to help me with editing run_eval.py so the program are tested properly to check whether the criteria are MET.
- *What I changed:* In order to check criteria 4 properly, the character count is added to all tries.

<!-- ═══════════════════════ UNIT 4 — THE TEST ═══════════════════════

     Don't fill these in during unit 3.
     ═══════════════════════════════════════════════════════════════════ -->

---

## Run Log — Before

<!-- Five criteria, five tries each, in this exact format.

     Five, because your criteria are written out of five. Mark each try PASS
     or FAIL, count the passes, and read that count against your target — a
     row targeting 4 of 5 with three PASS cells is MISSED (3/5).

     `python run_eval.py --label before` runs everything and writes the table
     into results/. Paste it here and fill in the verdicts. -->

| Criterion | Target | Try 1 | Try 2 | Try 3 | Try 4 | Try 5 | Verdict |
|---|---|---|---|---|---|---|---|
| 1. matching query completes | 4 of 5 | PASS | PASS | PASS | PASS | PASS | MET (5/5) |
| 2. impossible query stops early | 5 of 5 | PASS | PASS | PASS | PASS | PASS | MET (5/5) |
| 3. search results carried into suggest_outfit | 5 of 5 | PASS | PASS | PASS | PASS | PASS | MET (5/5) |
| 4. fit card under 280 chars, names item + outfit | 4 of 5 | PASS | PASS | FAIL | FAIL | FAIL | MISSED (2/5) |
| 5. regex fallback when model unreachable | 5 of 5 | PASS | PASS | PASS | PASS | PASS | MET (5/5) |

**Real output from one try**, pasted as text, naming the file and function
that produced it:

```
Criteria 1:
`agent.py::run_agent`
```
- Query: `vintage graphic tee under $30`
- Wardrobe: example

**Try 1**

- stopped early: no
- selected_item: Y2K Baby Tee — Butterfly Print ($18.0, depop)
- search_results: 10

Outfit suggestion:

```
* **Y2K Streetwear:** Pair the butterfly baby tee with your baggy dark-wash straight-leg jeans and chunky white sneakers. Throw on your black cropped zip hoodie unzipped over top, and finish the look with your black crossbody bag for an effortless 2000s throwback.
* **Casual Contrast:** Tuck the fitted baby tee into your wide-leg khaki trousers, cinched with the brown leather belt to balance the proportions. Layer your vintage black denim jacket over your shoulders and ground the outfit with your chunky white sneakers for an easy, vintage-meets-earth-tones everyday look.
```

Fit card:

```
Found the ultimate y2k butterfly baby tee on depop for eighteen dollars and I am officially obsessed. I’ve been styling it with baggy dark-wash jeans and a zip hoodie for the most effortless 2000s throwback fit. Such a good little score!
```
```
Criteria 2:
`tools.py::search_listings`
```
- Query: `designer ballgown size XXS under $5`
- Wardrobe: example

**Try 1**

- stopped early: yes — Nothing matched "designer ballgown" in size XXS under $5. You could raise your budget above $5, or drop the size filter (size XXS), or try broader or different words than "designer ballgown".
- selected_item: (none)
- search_results: 0

Trace:

```
[1] parse_query
      in:  designer ballgown size XXS under $5
      out: dict with keys: description, size, max_price
      →    parsed by model
[2] search_listings (with MCP)
      in:  dict with keys: description, size, max_price
      out: [] (empty)
      →    branch: empty, stopping
```

```
Criteria 3:
`agent.py::run_agent`
```
- Query: `denim jacket size S under $50`
- Wardrobe: example

**Try 1**

- stopped early: no
- selected_item: Denim Jacket — Light Wash, Cropped ($42.0, poshmark)
- search_results: 1

Outfit suggestion:

```
* **Double Denim Streetwear:** Pair the light wash cropped denim jacket with your white ribbed tank top tucked into the baggy dark-wash straight-leg jeans. Cinch the waist with the brown leather belt, and finish the look with the chunky white sneakers and the black crossbody bag. The contrast between the light jacket and dark bottoms creates an effortless, balanced silhouette.

* **Contrast Layering:** Layer the oversized grey crewneck sweatshirt underneath the light wash cropped denim jacket, letting the grey hem peek out the bottom for a cool proportion play. Pair this with the wide-leg khaki trousers, the brown leather belt, and the black combat boots for an earthy, textured outfit that leans into streetwear.
```

Fit card:

```
Scored this cropped light wash denim jacket on Poshmark for $42 and I'm obsessed with the structured shoulders. Been living in it layered over an oversized grey sweatshirt with khaki trousers and combat boots for that effortless streetwear look. Such a good basic to throw on with literally anything.
```

Trace:

```
[1] parse_query
      in:  denim jacket size S under $50
      out: dict with keys: description, size, max_price
      →    parsed by model
[2] select_item
      in:  1 results
      out: Denim Jacket — Light Wash, Cropped ($42.0, poshmark)
      →    selected first result
[3] suggest_outfit
      in:  dict with keys: item, wardrobe_items
      out: * **Double Denim Streetwear:** Pair the light wash cropped denim jacket with your white ribbed tank top tucked…
[4] create_fit_card
      in:  dict with keys: item, outfit
      out: Scored this cropped light wash denim jacket on Poshmark for $42 and I'm obsessed with the structured shoulders…
```

Criteria 4:
`agent.py::run_agent`

- Query: `black leather bomber jacket under $80`
- Wardrobe: example

**Try 1**

- stopped early: no
- selected_item: 90s Leather Bomber — Black ($75.0, depop)
- search_results: 10

Outfit suggestion:

```
* **90s Grunge Streetwear:** Layer your white ribbed tank top into the baggy straight-leg jeans with the brown leather belt. Throw the 90s leather bomber over top and finish with the black combat boots and black crossbody bag for an effortless, texture-rich silhouette.
* **Cozy Contrast:** Wear the oversized grey crewneck sweatshirt over your baggy straight-leg jeans—letting the hem of the grey crewneck peek out—and layer the 90s leather bomber on top to play with proportions. Ground the heavy layers with the chunky white sneakers and keep your black crossbody bag across your chest.
```

Fit card:

```
Manifested the exact 90s leather bomber I’ve been hunting for and scored it on Depop for $75. The broken-in leather is so good, and it adds the ultimate grunge edge whether I'm throwing it over a basic white tank and combat boots or layering it up with an oversized crewneck.
```

Trace:

```
[1] parse_query
      in:  black leather bomber jacket under $80
      out: dict with keys: description, size, max_price
      →    parsed by model
[2] select_item
      in:  10 results
      out: 90s Leather Bomber — Black ($75.0, depop)
      →    selected first result
[3] suggest_outfit
      in:  dict with keys: item, wardrobe_items
      out: * **90s Grunge Streetwear:** Layer your white ribbed tank top into the baggy straight-leg jeans with the brown…
[4] create_fit_card
      in:  dict with keys: item, outfit
      out: Manifested the exact 90s leather bomber I’ve been hunting for and scored it on Depop for $75. The broken-in le…
```

Criteria 5:
`agent.py::run_agent`

- Query: `silk slip dress size M under $40`
- Wardrobe: example

**Try 1**

Crashed:

```
ModelUnavailable: Couldn't reach the model: simulated: model unreachable
```
---

## Verdicts and Diagnoses

<!-- MET or MISSED per criterion against LAST UNIT's target, plus a sentence on
     how you decided.

     Then, for every miss: which of the four places it happened — a tool, the
     loop's branch, the session, or the model's output — AND the mechanism.

     Not a diagnosis:  "The fit card was bad."
     A diagnosis:      "The fit card criterion missed on 2 of 5 items. Both had
                        an empty brand field. My prompt puts the brand in the
                        first sentence, so the card opened with a blank and read
                        like a fragment. The tool worked; the prompt assumed a
                        field that isn't always there."

     Look for a pattern. Three misses on the same tool is one problem, not
     three. -->

| # | Criterion | Target | Verdict | How I decided |
|---|---|---|---|---|
| 1 | Full three-tool run returns a fit card | 4 of 5 | MET | If everything is working, the three-tool always return a fit card. For all tries, it passed so the verdict is met. |
| 2 | Empty search stops before tool 2 | 5 of 5 | MET | For all tries, if the search_listing method is unable to find suitable clothing pieces, it stops before tool 2. |
| 3 | Tracked session state across five runs to verify that the ID, title, and description from the search results accurately persists as input for suggest_outfit | 5 of 5 | MET | The results are saved to session and then passed to suggest_outfit by fetching from the data saved in session 5 out of 5 times so the criteria is met. |
| 4 | Generated fit card caption include both the target and suggest outfit while keeping the caption under 280 characters | 4 of 5 | MISSED | Out of the five tries, only two tried passed. The reason is the caption are not under 280 character for three tries. |
| 5 | When model cannot be reached, system will fall back to regex | 5 of 5 | MET | Whenever the model cannot be reached when parsing, the system always fall back to regex for parsing for 5 of 5 tries. |

**Diagnoses**
The fit card criterion missed on 3 of 5 tries. In 3 tries, the caption were generated as intended. However, the number of chracters for the 3 tries were over 280 characters. The reason for this miss is because the prompt is not specific enough. In the prompt, it was mentioned that the caption should be 2-4 sentence, but there was no mention of the caption needs to be under 280 characters. When fixing the prompt, it also needs to be mentioned that whether the 280 characters include spaces or not because it could make a huge difference. If we are following the rules from twitter then spaces will be included in the 280 characters.


---

## Loop Trace

<!-- One full run, printed step by step, with the MCP call visible in it.

     `python app.py ask '...' --trace` once you've added the trace.step()
     calls in Milestone 2.

     Worth pasting BOTH the happy path and the empty-search path. The empty
     one should be visibly shorter, because it stops. If your two traces are
     the same length, your branch isn't working — and this is the fastest way
     anyone will ever find that out. -->

**Happy path**

```
Command: python app.py ask 'vintage graphic tee under $30'
Results:
[1] parse_query
      in:  vintage graphic tee under $30
      out: dict with keys: description, size, max_price
      →    parsed by model
[2] select_item
      in:  10 results
      out: Y2K Baby Tee — Butterfly Print ($18.0, depop)
      →    selected first result
[3] suggest_outfit
      in:  dict with keys: item, wardrobe_items
      out: * **Y2K Streetwear Contrast:** Pair the pink-and-purple butterfly baby tee with your baggy dark-wash straight-…
[4] create_fit_card
      in:  dict with keys: item, outfit
      out: scored this adorable little y2k butterfly baby tee on depop for eighteen dollars and i’m obsessed. paired it w…

  Found:    Y2K Baby Tee — Butterfly Print — $18.0 on depop

  Outfit:   * **Y2K Streetwear Contrast:** Pair the pink-and-purple butterfly baby tee with your baggy dark-wash straight-leg jeans to balance the cropped silhouette with a relaxed, low-key bottom. Layer the slightly cropped vintage black denim jacket on top, and finish the look with your chunky white sneakers and the black crossbody bag. 
* **Model-Off-Duty Casual:** Tuck the baby tee into your wide-leg khaki trousers, defined by the brown leather belt to pull in the earth tones. Throw your oversized grey crewneck sweatshirt over your shoulders or wear it open, and anchor the outfit with your chunky white sneakers for an effortless, texture-mixed everyday vibe.

  Fit card: scored this adorable little y2k butterfly baby tee on depop for eighteen dollars and i’m obsessed. paired it with baggy dark-wash denim and a black jacket for that perfect casual streetwear contrast.

```

**Empty search**

```
Command: python app.py ask 'Suit size M under $10'

Results:

 [1] parse_query
      in:  Suit size M under $10
      out: dict with keys: description, size, max_price
      →    parsed by model
[2] search_listings (with MCP)
      in:  dict with keys: description, size, max_price
      out: [] (empty)
      →    branch: empty, stopping

  Nothing matched "suit" in size M under $10. You could raise your budget above $10, or drop the size filter (size M), or try broader or different words than "suit".
```

**Empty wardrobe**
```
Command: python app.py ask 'vintage graphic tee under $30' --empty-wardrobe

Results:
(running with an empty wardrobe)
[1] parse_query
      in:  vintage graphic tee under $30
      out: dict with keys: description, size, max_price
      →    parsed by model
[2] select_item
      in:  10 results
      out: Y2K Baby Tee — Butterfly Print ($18.0, depop)
      →    selected first result
[3] suggest_outfit
      in:  dict with keys: item, wardrobe_items
      out: * **90s Streetwear Vibe:** Pair the baby tee with baggy, mid-rise light-wash denim carpenter jeans to balance …
[4] create_fit_card
      in:  dict with keys: item, outfit
      out: Found this literal dream of a Y2K butterfly baby tee on depop for just $18 and I am never taking it off. It’s …

  Found:    Y2K Baby Tee — Butterfly Print — $18.0 on depop

  Outfit:   * **90s Streetwear Vibe:** Pair the baby tee with baggy, mid-rise light-wash denim carpenter jeans to balance the fitted crop top. Finish the look with chunky white platform sneakers, a small pastel pink shoulder bag, and wire-rimmed sunglasses.
* **Cozy Cottagecore Twist:** Tuck the tee into a moss-green corduroy A-line mini skirt. Layer an oversized, cream-colored chunky cable-knit cardigan on top, and wear it with cream ribbedcrew socks and dark brown leather Mary Jane flats.

  Fit card: Found this literal dream of a Y2K butterfly baby tee on depop for just $18 and I am never taking it off. It’s giving major early 2000s mallrat energy paired with baggy mid-rise carpenter jeans and chunky sneakers. Honestly might switch it up next time with a corduroy mini skirt and Mary Janes for a cozier vibe.
```

**Unavailable model**
```
Command: python app.py ask 'flannel shirt under $30'

Results:
[1] parse_query
      in:  flannel shirt under $30
      out: dict with keys: description, size, max_price
      →    parsed by regex
[2] select_item
      in:  2 results
      out: Oversized Flannel Shirt — Plaid Red/Black ($22.0, thredUp)
      →    selected first result
2 model calls this session

ModelUnavailable: The model rejected your API key. Check GEMINI_API_KEY in your .env file, or create a fresh key at aistudio.google.com.
```

**On the MCP move:** 
The 'search_listing' method is registered as an MCP tool in 'mcp_server.py' and called with 'call_tool("search_listings", {...})' from 'mcp_client.py'. The results generated from both direct calls and through MCP were similar.

---

## The Improvement

<!-- What you changed, why your diagnosis pointed at it, and the after-run in
     the same table format. One change, measured properly.

     `python run_eval.py --label after` -->

**What I changed:** The 'create_fit_card' prompt is edited and a safety net method is added.

**Which failure it was meant to fix:** The method originally created captions that are over 280 characters. After the fix, it ensures that the caption is under 280 characters.

### Run Log — After

| Criterion | Target | Try 1 | Try 2 | Try 3 | Try 4 | Try 5 | Verdict |
|---|---|---|---|---|---|---|---|
| 1. matching query completes | 4 of 5 | PASS | PASS | PASS | PASS | PASS | MET (5/5) |
| 2. impossible query stops early | 5 of 5 | PASS | PASS | PASS | PASS | PASS | MET (5/5) |
| 3. search result carried into suggest_outfit | 5 of 5 | PASS | PASS | PASS | PASS | PASS | MET (5/5) |
| 4. fit card under 280 characters, names item + outfit | 4 of 5 | PASS | PASS | PASS | PASS | PASS | MET (5/5) |
| 5. regex fallback when model unreachable | 5 of 5 | PASS | PASS | PASS | PASS | PASS | MET (5/5) |

**Did it help, and how do I know:**

<!-- If it made things worse, say that. Honestly reported, that earns full
     credit and is more interesting than one that worked. -->

The changes made in Milestone 5 helped fix the issue regarding the caption generated from 'create_fit_card'. According to Criterion 4, the captions generated should be under 280 characters. However, when it tested when running 'run_eval' it failed 3 times out of 5 times. Aside from editing the prompt to restrict the length of the caption, and a safety net is added to ensure the caption will be under 280 characters. With the edited prompt and method trim_caption, it ensures that all captions that are generated by the method 'create_fit_card' will be under 280 characters.



---

## What's Still Broken

<!-- For each criterion still missed: what you'd do, and why you stopped where
     you did. "I ran out of time" is fine if it's true. Pretending nothing is
     left is not. -->
Currently all criterion has been met. However, there are still a few things that are broken that are not mentioned in the criterion. First, when the model becomes unreachable or unavailable, the program will end immediately by sending the message "ModelUnavailable: Couldn't reach the model: simulated: model unreachable". This problem can be solved by adding fallback methods for 'suggest_outfit' and 'create_fit_card' to avoid this issue. Another issue is in the regex method for parsing. Currently, the regex assums that the first number becomes the price ceiling. 

<!-- ═════════════════════════════════════════════════════════════════════

     SUBMISSION CHECKLIST — unit 3

       [ ] criteria.md has five numbered criteria, each with a target
       [ ] Each criterion has a reason underneath it
       [ ] All five unit 3 sections above have real content
       [ ] Tool Inventory: all three tools, inputs WITH TYPES, a specific
           return value, and the empty case
       [ ] Planning Loop names the branch rule and agent.py::run_agent
       [ ] Sample Run: one full query plus the three per-tool tests, as text
       [ ] At least four new commits
       [ ] Repository URL submitted — WRITE IT DOWN, you submit the same one
           next unit

     SUBMISSION CHECKLIST — unit 4

       [ ] mcp_server.py exists with one tool registered
           (or a written record of exactly where the rewire broke)
       [ ] Run Log — Before, five criteria, five tries each
       [ ] Real output pasted underneath, naming file and function
       [ ] A verdict on every criterion
       [ ] A diagnosis for every miss, naming a place AND a mechanism
       [ ] Loop Trace, with the MCP call visible in it
       [ ] All three failure modes triggered and handled
       [ ] One improvement, with Run Log — After in the same format
       [ ] What's Still Broken
       [ ] At least four new commits
       [ ] The SAME repository URL as last unit

     Do not delete and recreate this repository. Your commit history is what
     shows your criteria existed before your results did.
     ═════════════════════════════════════════════════════════════════════ -->

---

📖 **How to run this project: [RUNNING.md](RUNNING.md)**
