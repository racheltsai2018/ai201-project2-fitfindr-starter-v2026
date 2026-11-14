# Run log — unit9_m5_run2

- Produced by: `run_eval.py::main`
- Loop: `agent.py::run_agent` · tools: `tools.py`
- Tries per scenario: 5, caching off
- Temperature: 0.9
- When: 2026-11-13 23:39

Paste the table below into your README. Fill in the Criterion and
Target columns from `criteria.md`, then mark each try PASS or FAIL
from the output underneath and count them for the Verdict.

| Criterion | Target | Try 1 | Try 2 | Try 3 | Try 4 | Try 5 | Verdict |
|---|---|---|---|---|---|---|---|
| 1. matching query completes |  |   |   |   |   |   |  |
| 2. impossible query stops early |  |   |   |   |   |   |  |
| empty wardrobe _(diagnostic — not one of your five)_ |  |   |   |   |   |   |  |
| 3. search result carried into suggest_outfit |  |   |   |   |   |   |  |
| 4. fit card under 280 chars, names item + outfit |  |   |   |   |   |   |  |
| 5. regex fallback when model unreachable |  |   |   |   |   |   |  |
| 6. every listing gets a label | 5/5 | PASS | PASS | PASS | PASS | PASS | MET (5/5) |
| 7. label matches the 20% rule | 5/5 | PASS | PASS | PASS | PASS | PASS | MET (5/5) |
| 8. too few comparables -> all unknown | 5/5 | PASS | PASS | PASS | PASS | PASS | MET (5/5) |
| 9. comparables are the same category | 5/5 | FAIL | FAIL | FAIL | FAIL | FAIL | MISSED (0/5) |
| 10. price estimation failure doesn't break the run | 5/5 | PASS | PASS | PASS | PASS | PASS | MET (5/5) |

> The Try and Verdict columns are blank on purpose. Whether a try
> passed depends on the criterion you wrote, so it's yours to decide.
> Count the passes, then read that count against your target: a row
> targeting 4 of 5 with three PASS cells is MISSED (3/5).

---

## What actually happened

Real output, as text. Paste the relevant parts into your README —
the rubric asks for output, not a description of it.

### matching query completes

- Query: `vintage graphic tee under $30`
- Wardrobe: example

**Try 1**

- stopped early: no
- selected_item: Y2K Baby Tee — Butterfly Print ($18.0, depop)
- search_results: 10

- parsed_by: model — parsed: {'description': 'vintage graphic tee', 'size': None, 'max_price': 30.0}

- typical_price: 27.0 (sample_size 31)
- every search result rated: True (10 rated / 10 results)
- all labels valid: True

Labels (actual vs. 20% rule):

| id | title | price | deal | expected | match |
|---|---|---|---|---|---|
| lst_002 | Y2K Baby Tee — Butterfly Print | 18.0 | good deal | good deal | yes |
| lst_006 | Graphic Tee — 2003 Tour Bootleg Style | 24.0 | fair | fair | yes |
| lst_033 | Vintage Band Tee — Faded Grey | 19.0 | good deal | good deal | yes |
| lst_015 | Vintage Graphic Hoodie — Faded Black | 26.0 | fair | fair | yes |
| lst_003 | Oversized Flannel Shirt — Plaid Red/Black | 22.0 | fair | fair | yes |
| lst_012 | Oversized Crewneck Sweatshirt — Vintage Navy | 20.0 | good deal | good deal | yes |
| lst_013 | 90s Silk Slip Dress — Floral, Midi Length | 30.0 | fair | fair | yes |
| lst_014 | Leather Belt — Brown, Braided | 12.0 | good deal | good deal | yes |
| lst_016 | High-Waisted Denim Shorts — Cutoff | 24.0 | fair | fair | yes |
| lst_017 | Mesh Long-Sleeve Top — Black | 15.0 | good deal | good deal | yes |

Comparables for 'vintage graphic tee' (31):

- Vintage Levi's 501 Jeans — Medium Wash — $38.0
- Y2K Baby Tee — Butterfly Print — $18.0
- Oversized Flannel Shirt — Plaid Red/Black — $22.0
- 90s Track Jacket — Navy/White Stripe — $45.0
- Corduroy Wide-Leg Pants — Rust — $32.0
- Graphic Tee — 2003 Tour Bootleg Style — $24.0
- Denim Jacket — Light Wash, Cropped — $42.0
- Vintage Windbreaker — Color Block Purple/Teal — $40.0
- Low-Rise Cargo Pants — Khaki — $27.0
- Oversized Crewneck Sweatshirt — Vintage Navy — $20.0
- 90s Silk Slip Dress — Floral, Midi Length — $30.0
- Leather Belt — Brown, Braided — $12.0
- Vintage Graphic Hoodie — Faded Black — $26.0
- High-Waisted Denim Shorts — Cutoff — $24.0
- Mesh Long-Sleeve Top — Black — $15.0
- Vintage Linen Blazer — Cream — $38.0
- Henley Long Sleeve — Washed Burgundy — $16.0
- Straight Leg Khaki Trousers — Olive — $29.0
- 90s Leather Bomber — Black — $75.0
- Vintage Polo Shirt — Forest Green — $18.0
- Oversized College Crewneck — Faded Red — $21.0
- Suede Chelsea Boots — Tan — $44.0
- Silk Button-Down — Sage Green — $28.0
- Vintage Knit Vest — Argyle Brown/Cream — $25.0
- Baggy Carpenter Jeans — Dark Wash — $36.0
- Vintage Band Tee — Faded Grey — $19.0
- Bucket Hat — Reversible, Brown Plaid — $14.0
- Velvet Blazer — Emerald Green — $52.0
- Straight Leg Black Jeans — Faded — $30.0
- Denim Vest — Medium Wash, Studded — $27.0
- Mini Shoulder Bag — Tan Leather — $38.0

Outfit suggestion:

```
* **Y2K Streetwear Contrast:** Pair the pink-and-purple butterfly baby tee with your baggy dark-wash straight-leg jeans to balance the cropped silhouette with a relaxed, low-key bottom. Layer the slightly cropped vintage black denim jacket on top, and finish the look with your chunky white sneakers and the black crossbody bag. 
* **Model-Off-Duty Casual:** Tuck the baby tee into your wide-leg khaki trousers, defined by the brown leather belt to pull in the earth tones. Throw your oversized grey crewneck sweatshirt over your shoulders or wear it open, and anchor the outfit with your chunky white sneakers for an effortless, texture-mixed everyday vibe.
```

Fit card:

```
scored this sweet y2k butterfly baby tee for just $18 on depop. obsessed with how it looks styled with baggy dark wash jeans and chunky sneakers for the ultimate street fit.
```

- Character count (including spaces): 173

Trace:

```
[1] parse_query
      in:  vintage graphic tee under $30
      out: dict with keys: description, size, max_price
      →    parsed by model
[2] estimate_price
      in:  dict with keys: description, results
      out: dict with keys: typical_price, sample_size, rated
[3] select_item
      in:  10 results
      out: Y2K Baby Tee — Butterfly Print ($18.0, depop)
      →    selected first result
[4] suggest_outfit
      in:  dict with keys: item, wardrobe_items
      out: * **Y2K Streetwear Contrast:** Pair the pink-and-purple butterfly baby tee with your baggy dark-wash straight-…
[5] create_fit_card
      in:  dict with keys: item, outfit
      out: scored this sweet y2k butterfly baby tee for just $18 on depop. obsessed with how it looks styled with baggy d…
```

**Try 2**

- stopped early: no
- selected_item: Y2K Baby Tee — Butterfly Print ($18.0, depop)
- search_results: 10

- parsed_by: model — parsed: {'description': 'vintage graphic tee', 'size': None, 'max_price': 30.0}

- typical_price: 27.0 (sample_size 31)
- every search result rated: True (10 rated / 10 results)
- all labels valid: True

Labels (actual vs. 20% rule):

| id | title | price | deal | expected | match |
|---|---|---|---|---|---|
| lst_002 | Y2K Baby Tee — Butterfly Print | 18.0 | good deal | good deal | yes |
| lst_006 | Graphic Tee — 2003 Tour Bootleg Style | 24.0 | fair | fair | yes |
| lst_033 | Vintage Band Tee — Faded Grey | 19.0 | good deal | good deal | yes |
| lst_015 | Vintage Graphic Hoodie — Faded Black | 26.0 | fair | fair | yes |
| lst_003 | Oversized Flannel Shirt — Plaid Red/Black | 22.0 | fair | fair | yes |
| lst_012 | Oversized Crewneck Sweatshirt — Vintage Navy | 20.0 | good deal | good deal | yes |
| lst_013 | 90s Silk Slip Dress — Floral, Midi Length | 30.0 | fair | fair | yes |
| lst_014 | Leather Belt — Brown, Braided | 12.0 | good deal | good deal | yes |
| lst_016 | High-Waisted Denim Shorts — Cutoff | 24.0 | fair | fair | yes |
| lst_017 | Mesh Long-Sleeve Top — Black | 15.0 | good deal | good deal | yes |

Comparables for 'vintage graphic tee' (31):

- Vintage Levi's 501 Jeans — Medium Wash — $38.0
- Y2K Baby Tee — Butterfly Print — $18.0
- Oversized Flannel Shirt — Plaid Red/Black — $22.0
- 90s Track Jacket — Navy/White Stripe — $45.0
- Corduroy Wide-Leg Pants — Rust — $32.0
- Graphic Tee — 2003 Tour Bootleg Style — $24.0
- Denim Jacket — Light Wash, Cropped — $42.0
- Vintage Windbreaker — Color Block Purple/Teal — $40.0
- Low-Rise Cargo Pants — Khaki — $27.0
- Oversized Crewneck Sweatshirt — Vintage Navy — $20.0
- 90s Silk Slip Dress — Floral, Midi Length — $30.0
- Leather Belt — Brown, Braided — $12.0
- Vintage Graphic Hoodie — Faded Black — $26.0
- High-Waisted Denim Shorts — Cutoff — $24.0
- Mesh Long-Sleeve Top — Black — $15.0
- Vintage Linen Blazer — Cream — $38.0
- Henley Long Sleeve — Washed Burgundy — $16.0
- Straight Leg Khaki Trousers — Olive — $29.0
- 90s Leather Bomber — Black — $75.0
- Vintage Polo Shirt — Forest Green — $18.0
- Oversized College Crewneck — Faded Red — $21.0
- Suede Chelsea Boots — Tan — $44.0
- Silk Button-Down — Sage Green — $28.0
- Vintage Knit Vest — Argyle Brown/Cream — $25.0
- Baggy Carpenter Jeans — Dark Wash — $36.0
- Vintage Band Tee — Faded Grey — $19.0
- Bucket Hat — Reversible, Brown Plaid — $14.0
- Velvet Blazer — Emerald Green — $52.0
- Straight Leg Black Jeans — Faded — $30.0
- Denim Vest — Medium Wash, Studded — $27.0
- Mini Shoulder Bag — Tan Leather — $38.0

Outfit suggestion:

```
* **Y2K Streetwear Contrast:** Pair the pink-and-purple butterfly baby tee with your baggy dark-wash straight-leg jeans to balance the cropped silhouette with a relaxed, low-key bottom. Layer the slightly cropped vintage black denim jacket on top, and finish the look with your chunky white sneakers and the black crossbody bag. 
* **Model-Off-Duty Casual:** Tuck the baby tee into your wide-leg khaki trousers, defined by the brown leather belt to pull in the earth tones. Throw your oversized grey crewneck sweatshirt over your shoulders or wear it open, and anchor the outfit with your chunky white sneakers for an effortless, texture-mixed everyday vibe.
```

Fit card:

```
scored this butterfly y2k baby tee on depop for $18 and i'm obsessed. styling it with baggy dark denim and chunky sneakers for the ultimate model-off-duty vibe.
```

- Character count (including spaces): 160

Trace:

```
[1] parse_query
      in:  vintage graphic tee under $30
      out: dict with keys: description, size, max_price
      →    parsed by model
[2] estimate_price
      in:  dict with keys: description, results
      out: dict with keys: typical_price, sample_size, rated
[3] select_item
      in:  10 results
      out: Y2K Baby Tee — Butterfly Print ($18.0, depop)
      →    selected first result
[4] suggest_outfit
      in:  dict with keys: item, wardrobe_items
      out: * **Y2K Streetwear Contrast:** Pair the pink-and-purple butterfly baby tee with your baggy dark-wash straight-…
[5] create_fit_card
      in:  dict with keys: item, outfit
      out: scored this butterfly y2k baby tee on depop for $18 and i'm obsessed. styling it with baggy dark denim and chu…
```

**Try 3**

- stopped early: no
- selected_item: Y2K Baby Tee — Butterfly Print ($18.0, depop)
- search_results: 10

- parsed_by: model — parsed: {'description': 'vintage graphic tee', 'size': None, 'max_price': 30.0}

- typical_price: 27.0 (sample_size 31)
- every search result rated: True (10 rated / 10 results)
- all labels valid: True

Labels (actual vs. 20% rule):

| id | title | price | deal | expected | match |
|---|---|---|---|---|---|
| lst_002 | Y2K Baby Tee — Butterfly Print | 18.0 | good deal | good deal | yes |
| lst_006 | Graphic Tee — 2003 Tour Bootleg Style | 24.0 | fair | fair | yes |
| lst_033 | Vintage Band Tee — Faded Grey | 19.0 | good deal | good deal | yes |
| lst_015 | Vintage Graphic Hoodie — Faded Black | 26.0 | fair | fair | yes |
| lst_003 | Oversized Flannel Shirt — Plaid Red/Black | 22.0 | fair | fair | yes |
| lst_012 | Oversized Crewneck Sweatshirt — Vintage Navy | 20.0 | good deal | good deal | yes |
| lst_013 | 90s Silk Slip Dress — Floral, Midi Length | 30.0 | fair | fair | yes |
| lst_014 | Leather Belt — Brown, Braided | 12.0 | good deal | good deal | yes |
| lst_016 | High-Waisted Denim Shorts — Cutoff | 24.0 | fair | fair | yes |
| lst_017 | Mesh Long-Sleeve Top — Black | 15.0 | good deal | good deal | yes |

Comparables for 'vintage graphic tee' (31):

- Vintage Levi's 501 Jeans — Medium Wash — $38.0
- Y2K Baby Tee — Butterfly Print — $18.0
- Oversized Flannel Shirt — Plaid Red/Black — $22.0
- 90s Track Jacket — Navy/White Stripe — $45.0
- Corduroy Wide-Leg Pants — Rust — $32.0
- Graphic Tee — 2003 Tour Bootleg Style — $24.0
- Denim Jacket — Light Wash, Cropped — $42.0
- Vintage Windbreaker — Color Block Purple/Teal — $40.0
- Low-Rise Cargo Pants — Khaki — $27.0
- Oversized Crewneck Sweatshirt — Vintage Navy — $20.0
- 90s Silk Slip Dress — Floral, Midi Length — $30.0
- Leather Belt — Brown, Braided — $12.0
- Vintage Graphic Hoodie — Faded Black — $26.0
- High-Waisted Denim Shorts — Cutoff — $24.0
- Mesh Long-Sleeve Top — Black — $15.0
- Vintage Linen Blazer — Cream — $38.0
- Henley Long Sleeve — Washed Burgundy — $16.0
- Straight Leg Khaki Trousers — Olive — $29.0
- 90s Leather Bomber — Black — $75.0
- Vintage Polo Shirt — Forest Green — $18.0
- Oversized College Crewneck — Faded Red — $21.0
- Suede Chelsea Boots — Tan — $44.0
- Silk Button-Down — Sage Green — $28.0
- Vintage Knit Vest — Argyle Brown/Cream — $25.0
- Baggy Carpenter Jeans — Dark Wash — $36.0
- Vintage Band Tee — Faded Grey — $19.0
- Bucket Hat — Reversible, Brown Plaid — $14.0
- Velvet Blazer — Emerald Green — $52.0
- Straight Leg Black Jeans — Faded — $30.0
- Denim Vest — Medium Wash, Studded — $27.0
- Mini Shoulder Bag — Tan Leather — $38.0

Outfit suggestion:

```
* **Y2K Streetwear Contrast:** Pair the pink-and-purple butterfly baby tee with your baggy dark-wash straight-leg jeans to balance the cropped silhouette with a relaxed, low-key bottom. Layer the slightly cropped vintage black denim jacket on top, and finish the look with your chunky white sneakers and the black crossbody bag. 
* **Model-Off-Duty Casual:** Tuck the baby tee into your wide-leg khaki trousers, defined by the brown leather belt to pull in the earth tones. Throw your oversized grey crewneck sweatshirt over your shoulders or wear it open, and anchor the outfit with your chunky white sneakers for an effortless, texture-mixed everyday vibe.
```

Fit card:

```
Scored this adorable Y2K butterfly baby tee for just $18 on Depop! Styled it with baggy dark wash jeans and a black jacket for that perfect low-key streetwear vibe.
```

- Character count (including spaces): 164

Trace:

```
[1] parse_query
      in:  vintage graphic tee under $30
      out: dict with keys: description, size, max_price
      →    parsed by model
[2] estimate_price
      in:  dict with keys: description, results
      out: dict with keys: typical_price, sample_size, rated
[3] select_item
      in:  10 results
      out: Y2K Baby Tee — Butterfly Print ($18.0, depop)
      →    selected first result
[4] suggest_outfit
      in:  dict with keys: item, wardrobe_items
      out: * **Y2K Streetwear Contrast:** Pair the pink-and-purple butterfly baby tee with your baggy dark-wash straight-…
[5] create_fit_card
      in:  dict with keys: item, outfit
      out: Scored this adorable Y2K butterfly baby tee for just $18 on Depop! Styled it with baggy dark wash jeans and a …
```

**Try 4**

- stopped early: no
- selected_item: Y2K Baby Tee — Butterfly Print ($18.0, depop)
- search_results: 10

- parsed_by: model — parsed: {'description': 'vintage graphic tee', 'size': None, 'max_price': 30.0}

- typical_price: 27.0 (sample_size 31)
- every search result rated: True (10 rated / 10 results)
- all labels valid: True

Labels (actual vs. 20% rule):

| id | title | price | deal | expected | match |
|---|---|---|---|---|---|
| lst_002 | Y2K Baby Tee — Butterfly Print | 18.0 | good deal | good deal | yes |
| lst_006 | Graphic Tee — 2003 Tour Bootleg Style | 24.0 | fair | fair | yes |
| lst_033 | Vintage Band Tee — Faded Grey | 19.0 | good deal | good deal | yes |
| lst_015 | Vintage Graphic Hoodie — Faded Black | 26.0 | fair | fair | yes |
| lst_003 | Oversized Flannel Shirt — Plaid Red/Black | 22.0 | fair | fair | yes |
| lst_012 | Oversized Crewneck Sweatshirt — Vintage Navy | 20.0 | good deal | good deal | yes |
| lst_013 | 90s Silk Slip Dress — Floral, Midi Length | 30.0 | fair | fair | yes |
| lst_014 | Leather Belt — Brown, Braided | 12.0 | good deal | good deal | yes |
| lst_016 | High-Waisted Denim Shorts — Cutoff | 24.0 | fair | fair | yes |
| lst_017 | Mesh Long-Sleeve Top — Black | 15.0 | good deal | good deal | yes |

Comparables for 'vintage graphic tee' (31):

- Vintage Levi's 501 Jeans — Medium Wash — $38.0
- Y2K Baby Tee — Butterfly Print — $18.0
- Oversized Flannel Shirt — Plaid Red/Black — $22.0
- 90s Track Jacket — Navy/White Stripe — $45.0
- Corduroy Wide-Leg Pants — Rust — $32.0
- Graphic Tee — 2003 Tour Bootleg Style — $24.0
- Denim Jacket — Light Wash, Cropped — $42.0
- Vintage Windbreaker — Color Block Purple/Teal — $40.0
- Low-Rise Cargo Pants — Khaki — $27.0
- Oversized Crewneck Sweatshirt — Vintage Navy — $20.0
- 90s Silk Slip Dress — Floral, Midi Length — $30.0
- Leather Belt — Brown, Braided — $12.0
- Vintage Graphic Hoodie — Faded Black — $26.0
- High-Waisted Denim Shorts — Cutoff — $24.0
- Mesh Long-Sleeve Top — Black — $15.0
- Vintage Linen Blazer — Cream — $38.0
- Henley Long Sleeve — Washed Burgundy — $16.0
- Straight Leg Khaki Trousers — Olive — $29.0
- 90s Leather Bomber — Black — $75.0
- Vintage Polo Shirt — Forest Green — $18.0
- Oversized College Crewneck — Faded Red — $21.0
- Suede Chelsea Boots — Tan — $44.0
- Silk Button-Down — Sage Green — $28.0
- Vintage Knit Vest — Argyle Brown/Cream — $25.0
- Baggy Carpenter Jeans — Dark Wash — $36.0
- Vintage Band Tee — Faded Grey — $19.0
- Bucket Hat — Reversible, Brown Plaid — $14.0
- Velvet Blazer — Emerald Green — $52.0
- Straight Leg Black Jeans — Faded — $30.0
- Denim Vest — Medium Wash, Studded — $27.0
- Mini Shoulder Bag — Tan Leather — $38.0

Outfit suggestion:

```
* **Y2K Streetwear Contrast:** Pair the pink-and-purple butterfly baby tee with your baggy dark-wash straight-leg jeans to balance the cropped silhouette with a relaxed, low-key bottom. Layer the slightly cropped vintage black denim jacket on top, and finish the look with your chunky white sneakers and the black crossbody bag. 
* **Model-Off-Duty Casual:** Tuck the baby tee into your wide-leg khaki trousers, defined by the brown leather belt to pull in the earth tones. Throw your oversized grey crewneck sweatshirt over your shoulders or wear it open, and anchor the outfit with your chunky white sneakers for an effortless, texture-mixed everyday vibe.
```

Fit card:

```
scored this adorable butterfly baby tee on depop for just $18 and I am obsessed. styling it with baggy dark denim and chunky sneakers for the ultimate y2k streetwear look.
```

- Character count (including spaces): 171

Trace:

```
[1] parse_query
      in:  vintage graphic tee under $30
      out: dict with keys: description, size, max_price
      →    parsed by model
[2] estimate_price
      in:  dict with keys: description, results
      out: dict with keys: typical_price, sample_size, rated
[3] select_item
      in:  10 results
      out: Y2K Baby Tee — Butterfly Print ($18.0, depop)
      →    selected first result
[4] suggest_outfit
      in:  dict with keys: item, wardrobe_items
      out: * **Y2K Streetwear Contrast:** Pair the pink-and-purple butterfly baby tee with your baggy dark-wash straight-…
[5] create_fit_card
      in:  dict with keys: item, outfit
      out: scored this adorable butterfly baby tee on depop for just $18 and I am obsessed. styling it with baggy dark de…
```

**Try 5**

- stopped early: no
- selected_item: Y2K Baby Tee — Butterfly Print ($18.0, depop)
- search_results: 10

- parsed_by: model — parsed: {'description': 'vintage graphic tee', 'size': None, 'max_price': 30.0}

- typical_price: 27.0 (sample_size 31)
- every search result rated: True (10 rated / 10 results)
- all labels valid: True

Labels (actual vs. 20% rule):

| id | title | price | deal | expected | match |
|---|---|---|---|---|---|
| lst_002 | Y2K Baby Tee — Butterfly Print | 18.0 | good deal | good deal | yes |
| lst_006 | Graphic Tee — 2003 Tour Bootleg Style | 24.0 | fair | fair | yes |
| lst_033 | Vintage Band Tee — Faded Grey | 19.0 | good deal | good deal | yes |
| lst_015 | Vintage Graphic Hoodie — Faded Black | 26.0 | fair | fair | yes |
| lst_003 | Oversized Flannel Shirt — Plaid Red/Black | 22.0 | fair | fair | yes |
| lst_012 | Oversized Crewneck Sweatshirt — Vintage Navy | 20.0 | good deal | good deal | yes |
| lst_013 | 90s Silk Slip Dress — Floral, Midi Length | 30.0 | fair | fair | yes |
| lst_014 | Leather Belt — Brown, Braided | 12.0 | good deal | good deal | yes |
| lst_016 | High-Waisted Denim Shorts — Cutoff | 24.0 | fair | fair | yes |
| lst_017 | Mesh Long-Sleeve Top — Black | 15.0 | good deal | good deal | yes |

Comparables for 'vintage graphic tee' (31):

- Vintage Levi's 501 Jeans — Medium Wash — $38.0
- Y2K Baby Tee — Butterfly Print — $18.0
- Oversized Flannel Shirt — Plaid Red/Black — $22.0
- 90s Track Jacket — Navy/White Stripe — $45.0
- Corduroy Wide-Leg Pants — Rust — $32.0
- Graphic Tee — 2003 Tour Bootleg Style — $24.0
- Denim Jacket — Light Wash, Cropped — $42.0
- Vintage Windbreaker — Color Block Purple/Teal — $40.0
- Low-Rise Cargo Pants — Khaki — $27.0
- Oversized Crewneck Sweatshirt — Vintage Navy — $20.0
- 90s Silk Slip Dress — Floral, Midi Length — $30.0
- Leather Belt — Brown, Braided — $12.0
- Vintage Graphic Hoodie — Faded Black — $26.0
- High-Waisted Denim Shorts — Cutoff — $24.0
- Mesh Long-Sleeve Top — Black — $15.0
- Vintage Linen Blazer — Cream — $38.0
- Henley Long Sleeve — Washed Burgundy — $16.0
- Straight Leg Khaki Trousers — Olive — $29.0
- 90s Leather Bomber — Black — $75.0
- Vintage Polo Shirt — Forest Green — $18.0
- Oversized College Crewneck — Faded Red — $21.0
- Suede Chelsea Boots — Tan — $44.0
- Silk Button-Down — Sage Green — $28.0
- Vintage Knit Vest — Argyle Brown/Cream — $25.0
- Baggy Carpenter Jeans — Dark Wash — $36.0
- Vintage Band Tee — Faded Grey — $19.0
- Bucket Hat — Reversible, Brown Plaid — $14.0
- Velvet Blazer — Emerald Green — $52.0
- Straight Leg Black Jeans — Faded — $30.0
- Denim Vest — Medium Wash, Studded — $27.0
- Mini Shoulder Bag — Tan Leather — $38.0

Outfit suggestion:

```
* **Y2K Streetwear Contrast:** Pair the pink-and-purple butterfly baby tee with your baggy dark-wash straight-leg jeans to balance the cropped silhouette with a relaxed, low-key bottom. Layer the slightly cropped vintage black denim jacket on top, and finish the look with your chunky white sneakers and the black crossbody bag. 
* **Model-Off-Duty Casual:** Tuck the baby tee into your wide-leg khaki trousers, defined by the brown leather belt to pull in the earth tones. Throw your oversized grey crewneck sweatshirt over your shoulders or wear it open, and anchor the outfit with your chunky white sneakers for an effortless, texture-mixed everyday vibe.
```

Fit card:

```
scored this y2k butterfly baby tee on depop for $18 and i'm obsessed. styling it with baggy dark denim and chunky sneakers for the ultimate street fit!
```

- Character count (including spaces): 151

Trace:

```
[1] parse_query
      in:  vintage graphic tee under $30
      out: dict with keys: description, size, max_price
      →    parsed by model
[2] estimate_price
      in:  dict with keys: description, results
      out: dict with keys: typical_price, sample_size, rated
[3] select_item
      in:  10 results
      out: Y2K Baby Tee — Butterfly Print ($18.0, depop)
      →    selected first result
[4] suggest_outfit
      in:  dict with keys: item, wardrobe_items
      out: * **Y2K Streetwear Contrast:** Pair the pink-and-purple butterfly baby tee with your baggy dark-wash straight-…
[5] create_fit_card
      in:  dict with keys: item, outfit
      out: scored this y2k butterfly baby tee on depop for $18 and i'm obsessed. styling it with baggy dark denim and chu…
```

### impossible query stops early

- Query: `designer ballgown size XXS under $5`
- Wardrobe: example

**Try 1**

- stopped early: yes — Nothing matched "designer ballgown" in size XXS under $5. You could raise your budget above $5, or drop the size filter (size XXS), or try broader or different words than "designer ballgown".
- selected_item: (none)
- search_results: 0

- parsed_by: model — parsed: {'description': 'designer ballgown', 'size': 'XXS', 'max_price': 5.0}

- price_estimate: (none)

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

**Try 2**

- stopped early: yes — Nothing matched "designer ballgown" in size XXS under $5. You could raise your budget above $5, or drop the size filter (size XXS), or try broader or different words than "designer ballgown".
- selected_item: (none)
- search_results: 0

- parsed_by: model — parsed: {'description': 'designer ballgown', 'size': 'XXS', 'max_price': 5.0}

- price_estimate: (none)

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

**Try 3**

- stopped early: yes — Nothing matched "designer ballgown" in size XXS under $5. You could raise your budget above $5, or drop the size filter (size XXS), or try broader or different words than "designer ballgown".
- selected_item: (none)
- search_results: 0

- parsed_by: model — parsed: {'description': 'designer ballgown', 'size': 'XXS', 'max_price': 5.0}

- price_estimate: (none)

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

**Try 4**

- stopped early: yes — Nothing matched "designer ballgown" in size XXS under $5. You could raise your budget above $5, or drop the size filter (size XXS), or try broader or different words than "designer ballgown".
- selected_item: (none)
- search_results: 0

- parsed_by: model — parsed: {'description': 'designer ballgown', 'size': 'XXS', 'max_price': 5.0}

- price_estimate: (none)

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

**Try 5**

- stopped early: yes — Nothing matched "designer ballgown" in size XXS under $5. You could raise your budget above $5, or drop the size filter (size XXS), or try broader or different words than "designer ballgown".
- selected_item: (none)
- search_results: 0

- parsed_by: model — parsed: {'description': 'designer ballgown', 'size': 'XXS', 'max_price': 5.0}

- price_estimate: (none)

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

### empty wardrobe

- Query: `denim jacket under $50`
- Wardrobe: empty

**Try 1**

- stopped early: no
- selected_item: Denim Jacket — Light Wash, Cropped ($42.0, poshmark)
- search_results: 7

- parsed_by: model — parsed: {'description': 'denim jacket', 'size': None, 'max_price': 50.0}

- typical_price: 35.5 (sample_size 8)
- every search result rated: True (7 rated / 7 results)
- all labels valid: True

Labels (actual vs. 20% rule):

| id | title | price | deal | expected | match |
|---|---|---|---|---|---|
| lst_007 | Denim Jacket — Light Wash, Cropped | 42.0 | fair | fair | yes |
| lst_001 | Vintage Levi's 501 Jeans — Medium Wash | 38.0 | fair | fair | yes |
| lst_004 | 90s Track Jacket — Navy/White Stripe | 45.0 | overpriced | overpriced | yes |
| lst_016 | High-Waisted Denim Shorts — Cutoff | 24.0 | good deal | good deal | yes |
| lst_037 | Straight Leg Black Jeans — Faded | 30.0 | fair | fair | yes |
| lst_038 | Denim Vest — Medium Wash, Studded | 27.0 | good deal | good deal | yes |
| lst_032 | Shacket — Olive Canvas | 33.0 | fair | fair | yes |

Comparables for 'denim jacket' (8):

- Vintage Levi's 501 Jeans — Medium Wash — $38.0
- 90s Track Jacket — Navy/White Stripe — $45.0
- Denim Jacket — Light Wash, Cropped — $42.0
- High-Waisted Denim Shorts — Cutoff — $24.0
- 90s Leather Bomber — Black — $75.0
- Shacket — Olive Canvas — $33.0
- Straight Leg Black Jeans — Faded — $30.0
- Denim Vest — Medium Wash, Studded — $27.0

Outfit suggestion:

```
* **Off-Duty Retro:** Throw the cropped jacket over a tucked-in, ribbed black tank top and high-waisted, wide-leg olive green cargo pants. Ground the proportions with chunky black platform loafers and a minimalist silver shoulder bag to balance the rugged denim.
* **Cozy Contrast:** Layer it on top of an oversized, moss-green knit turtleneck sweater so the hem peeks out the bottom, paired with a black pleated tennis skirt and sheer black tights. Finish the look with vintage-style canvas high-top sneakers and a beanie in a warm rust orange.
```

Fit card:

```
scored this cropped light wash denim jacket on Poshmark for $42 and the structured shoulders are everything. currently obsessed with throwing it over an oversized moss sweater and pleated skirt for that cozy contrast look.
```

- Character count (including spaces): 222

Trace:

```
[1] parse_query
      in:  denim jacket under $50
      out: dict with keys: description, size, max_price
      →    parsed by model
[2] estimate_price
      in:  dict with keys: description, results
      out: dict with keys: typical_price, sample_size, rated
[3] select_item
      in:  7 results
      out: Denim Jacket — Light Wash, Cropped ($42.0, poshmark)
      →    selected first result
[4] suggest_outfit
      in:  dict with keys: item, wardrobe_items
      out: * **Off-Duty Retro:** Throw the cropped jacket over a tucked-in, ribbed black tank top and high-waisted, wide-…
[5] create_fit_card
      in:  dict with keys: item, outfit
      out: scored this cropped light wash denim jacket on Poshmark for $42 and the structured shoulders are everything. c…
```

**Try 2**

- stopped early: no
- selected_item: Denim Jacket — Light Wash, Cropped ($42.0, poshmark)
- search_results: 7

- parsed_by: model — parsed: {'description': 'denim jacket', 'size': None, 'max_price': 50.0}

- typical_price: 35.5 (sample_size 8)
- every search result rated: True (7 rated / 7 results)
- all labels valid: True

Labels (actual vs. 20% rule):

| id | title | price | deal | expected | match |
|---|---|---|---|---|---|
| lst_007 | Denim Jacket — Light Wash, Cropped | 42.0 | fair | fair | yes |
| lst_001 | Vintage Levi's 501 Jeans — Medium Wash | 38.0 | fair | fair | yes |
| lst_004 | 90s Track Jacket — Navy/White Stripe | 45.0 | overpriced | overpriced | yes |
| lst_016 | High-Waisted Denim Shorts — Cutoff | 24.0 | good deal | good deal | yes |
| lst_037 | Straight Leg Black Jeans — Faded | 30.0 | fair | fair | yes |
| lst_038 | Denim Vest — Medium Wash, Studded | 27.0 | good deal | good deal | yes |
| lst_032 | Shacket — Olive Canvas | 33.0 | fair | fair | yes |

Comparables for 'denim jacket' (8):

- Vintage Levi's 501 Jeans — Medium Wash — $38.0
- 90s Track Jacket — Navy/White Stripe — $45.0
- Denim Jacket — Light Wash, Cropped — $42.0
- High-Waisted Denim Shorts — Cutoff — $24.0
- 90s Leather Bomber — Black — $75.0
- Shacket — Olive Canvas — $33.0
- Straight Leg Black Jeans — Faded — $30.0
- Denim Vest — Medium Wash, Studded — $27.0

Outfit suggestion:

```
* **Off-Duty Retro:** Throw the cropped jacket over a tucked-in, ribbed black tank top and high-waisted, wide-leg olive green cargo pants. Ground the proportions with chunky black platform loafers and a minimalist silver shoulder bag to balance the rugged denim.
* **Cozy Contrast:** Layer it on top of an oversized, moss-green knit turtleneck sweater so the hem peeks out the bottom, paired with a black pleated tennis skirt and sheer black tights. Finish the look with vintage-style canvas high-top sneakers and a beanie in a warm rust orange.
```

Fit card:

```
Found this vintage cropped denim jacket on Poshmark for $42 and I'm obsessed with the structured shoulders. Styled it like an off-duty retro look with cargos and platforms.
```

- Character count (including spaces): 172

Trace:

```
[1] parse_query
      in:  denim jacket under $50
      out: dict with keys: description, size, max_price
      →    parsed by model
[2] estimate_price
      in:  dict with keys: description, results
      out: dict with keys: typical_price, sample_size, rated
[3] select_item
      in:  7 results
      out: Denim Jacket — Light Wash, Cropped ($42.0, poshmark)
      →    selected first result
[4] suggest_outfit
      in:  dict with keys: item, wardrobe_items
      out: * **Off-Duty Retro:** Throw the cropped jacket over a tucked-in, ribbed black tank top and high-waisted, wide-…
[5] create_fit_card
      in:  dict with keys: item, outfit
      out: Found this vintage cropped denim jacket on Poshmark for $42 and I'm obsessed with the structured shoulders. St…
```

**Try 3**

- stopped early: no
- selected_item: Denim Jacket — Light Wash, Cropped ($42.0, poshmark)
- search_results: 7

- parsed_by: model — parsed: {'description': 'denim jacket', 'size': None, 'max_price': 50.0}

- typical_price: 35.5 (sample_size 8)
- every search result rated: True (7 rated / 7 results)
- all labels valid: True

Labels (actual vs. 20% rule):

| id | title | price | deal | expected | match |
|---|---|---|---|---|---|
| lst_007 | Denim Jacket — Light Wash, Cropped | 42.0 | fair | fair | yes |
| lst_001 | Vintage Levi's 501 Jeans — Medium Wash | 38.0 | fair | fair | yes |
| lst_004 | 90s Track Jacket — Navy/White Stripe | 45.0 | overpriced | overpriced | yes |
| lst_016 | High-Waisted Denim Shorts — Cutoff | 24.0 | good deal | good deal | yes |
| lst_037 | Straight Leg Black Jeans — Faded | 30.0 | fair | fair | yes |
| lst_038 | Denim Vest — Medium Wash, Studded | 27.0 | good deal | good deal | yes |
| lst_032 | Shacket — Olive Canvas | 33.0 | fair | fair | yes |

Comparables for 'denim jacket' (8):

- Vintage Levi's 501 Jeans — Medium Wash — $38.0
- 90s Track Jacket — Navy/White Stripe — $45.0
- Denim Jacket — Light Wash, Cropped — $42.0
- High-Waisted Denim Shorts — Cutoff — $24.0
- 90s Leather Bomber — Black — $75.0
- Shacket — Olive Canvas — $33.0
- Straight Leg Black Jeans — Faded — $30.0
- Denim Vest — Medium Wash, Studded — $27.0

Outfit suggestion:

```
* **Off-Duty Retro:** Throw the cropped jacket over a tucked-in, ribbed black tank top and high-waisted, wide-leg olive green cargo pants. Ground the proportions with chunky black platform loafers and a minimalist silver shoulder bag to balance the rugged denim.
* **Cozy Contrast:** Layer it on top of an oversized, moss-green knit turtleneck sweater so the hem peeks out the bottom, paired with a black pleated tennis skirt and sheer black tights. Finish the look with vintage-style canvas high-top sneakers and a beanie in a warm rust orange.
```

Fit card:

```
scored this cropped light wash denim jacket on Poshmark for $42 and the structured shoulders are everything. obsessed with throwing it over an oversized green knit turtleneck and pleated skirt for that cozy contrast look.
```

- Character count (including spaces): 221

Trace:

```
[1] parse_query
      in:  denim jacket under $50
      out: dict with keys: description, size, max_price
      →    parsed by model
[2] estimate_price
      in:  dict with keys: description, results
      out: dict with keys: typical_price, sample_size, rated
[3] select_item
      in:  7 results
      out: Denim Jacket — Light Wash, Cropped ($42.0, poshmark)
      →    selected first result
[4] suggest_outfit
      in:  dict with keys: item, wardrobe_items
      out: * **Off-Duty Retro:** Throw the cropped jacket over a tucked-in, ribbed black tank top and high-waisted, wide-…
[5] create_fit_card
      in:  dict with keys: item, outfit
      out: scored this cropped light wash denim jacket on Poshmark for $42 and the structured shoulders are everything. o…
```

**Try 4**

- stopped early: no
- selected_item: Denim Jacket — Light Wash, Cropped ($42.0, poshmark)
- search_results: 7

- parsed_by: model — parsed: {'description': 'denim jacket', 'size': None, 'max_price': 50.0}

- typical_price: 35.5 (sample_size 8)
- every search result rated: True (7 rated / 7 results)
- all labels valid: True

Labels (actual vs. 20% rule):

| id | title | price | deal | expected | match |
|---|---|---|---|---|---|
| lst_007 | Denim Jacket — Light Wash, Cropped | 42.0 | fair | fair | yes |
| lst_001 | Vintage Levi's 501 Jeans — Medium Wash | 38.0 | fair | fair | yes |
| lst_004 | 90s Track Jacket — Navy/White Stripe | 45.0 | overpriced | overpriced | yes |
| lst_016 | High-Waisted Denim Shorts — Cutoff | 24.0 | good deal | good deal | yes |
| lst_037 | Straight Leg Black Jeans — Faded | 30.0 | fair | fair | yes |
| lst_038 | Denim Vest — Medium Wash, Studded | 27.0 | good deal | good deal | yes |
| lst_032 | Shacket — Olive Canvas | 33.0 | fair | fair | yes |

Comparables for 'denim jacket' (8):

- Vintage Levi's 501 Jeans — Medium Wash — $38.0
- 90s Track Jacket — Navy/White Stripe — $45.0
- Denim Jacket — Light Wash, Cropped — $42.0
- High-Waisted Denim Shorts — Cutoff — $24.0
- 90s Leather Bomber — Black — $75.0
- Shacket — Olive Canvas — $33.0
- Straight Leg Black Jeans — Faded — $30.0
- Denim Vest — Medium Wash, Studded — $27.0

Outfit suggestion:

```
* **Off-Duty Retro:** Throw the cropped jacket over a tucked-in, ribbed black tank top and high-waisted, wide-leg olive green cargo pants. Ground the proportions with chunky black platform loafers and a minimalist silver shoulder bag to balance the rugged denim.
* **Cozy Contrast:** Layer it on top of an oversized, moss-green knit turtleneck sweater so the hem peeks out the bottom, paired with a black pleated tennis skirt and sheer black tights. Finish the look with vintage-style canvas high-top sneakers and a beanie in a warm rust orange.
```

Fit card:

```
Scored this cropped light wash denim jacket on Poshmark for $42 and I'm obsessed with the structured shoulders. Obsessed with styling it over an oversized moss turtleneck and pleated skirt for that cozy contrast look.
```

- Character count (including spaces): 217

Trace:

```
[1] parse_query
      in:  denim jacket under $50
      out: dict with keys: description, size, max_price
      →    parsed by model
[2] estimate_price
      in:  dict with keys: description, results
      out: dict with keys: typical_price, sample_size, rated
[3] select_item
      in:  7 results
      out: Denim Jacket — Light Wash, Cropped ($42.0, poshmark)
      →    selected first result
[4] suggest_outfit
      in:  dict with keys: item, wardrobe_items
      out: * **Off-Duty Retro:** Throw the cropped jacket over a tucked-in, ribbed black tank top and high-waisted, wide-…
[5] create_fit_card
      in:  dict with keys: item, outfit
      out: Scored this cropped light wash denim jacket on Poshmark for $42 and I'm obsessed with the structured shoulders…
```

**Try 5**

- stopped early: no
- selected_item: Denim Jacket — Light Wash, Cropped ($42.0, poshmark)
- search_results: 7

- parsed_by: model — parsed: {'description': 'denim jacket', 'size': None, 'max_price': 50.0}

- typical_price: 35.5 (sample_size 8)
- every search result rated: True (7 rated / 7 results)
- all labels valid: True

Labels (actual vs. 20% rule):

| id | title | price | deal | expected | match |
|---|---|---|---|---|---|
| lst_007 | Denim Jacket — Light Wash, Cropped | 42.0 | fair | fair | yes |
| lst_001 | Vintage Levi's 501 Jeans — Medium Wash | 38.0 | fair | fair | yes |
| lst_004 | 90s Track Jacket — Navy/White Stripe | 45.0 | overpriced | overpriced | yes |
| lst_016 | High-Waisted Denim Shorts — Cutoff | 24.0 | good deal | good deal | yes |
| lst_037 | Straight Leg Black Jeans — Faded | 30.0 | fair | fair | yes |
| lst_038 | Denim Vest — Medium Wash, Studded | 27.0 | good deal | good deal | yes |
| lst_032 | Shacket — Olive Canvas | 33.0 | fair | fair | yes |

Comparables for 'denim jacket' (8):

- Vintage Levi's 501 Jeans — Medium Wash — $38.0
- 90s Track Jacket — Navy/White Stripe — $45.0
- Denim Jacket — Light Wash, Cropped — $42.0
- High-Waisted Denim Shorts — Cutoff — $24.0
- 90s Leather Bomber — Black — $75.0
- Shacket — Olive Canvas — $33.0
- Straight Leg Black Jeans — Faded — $30.0
- Denim Vest — Medium Wash, Studded — $27.0

Outfit suggestion:

```
* **Off-Duty Retro:** Throw the cropped jacket over a tucked-in, ribbed black tank top and high-waisted, wide-leg olive green cargo pants. Ground the proportions with chunky black platform loafers and a minimalist silver shoulder bag to balance the rugged denim.
* **Cozy Contrast:** Layer it on top of an oversized, moss-green knit turtleneck sweater so the hem peeks out the bottom, paired with a black pleated tennis skirt and sheer black tights. Finish the look with vintage-style canvas high-top sneakers and a beanie in a warm rust orange.
```

Fit card:

```
Scored this cropped vintage denim jacket on Poshmark for $42 and it has the best structured shoulders. Obsessed with styling it over an oversized moss turtleneck and pleated skirt.
```

- Character count (including spaces): 180

Trace:

```
[1] parse_query
      in:  denim jacket under $50
      out: dict with keys: description, size, max_price
      →    parsed by model
[2] estimate_price
      in:  dict with keys: description, results
      out: dict with keys: typical_price, sample_size, rated
[3] select_item
      in:  7 results
      out: Denim Jacket — Light Wash, Cropped ($42.0, poshmark)
      →    selected first result
[4] suggest_outfit
      in:  dict with keys: item, wardrobe_items
      out: * **Off-Duty Retro:** Throw the cropped jacket over a tucked-in, ribbed black tank top and high-waisted, wide-…
[5] create_fit_card
      in:  dict with keys: item, outfit
      out: Scored this cropped vintage denim jacket on Poshmark for $42 and it has the best structured shoulders. Obsesse…
```

### search result carried into suggest_outfit

- Query: `denim jacket size S under $50`
- Wardrobe: example

**Try 1**

- stopped early: no
- selected_item: Denim Jacket — Light Wash, Cropped ($42.0, poshmark)
- search_results: 1

- parsed_by: model — parsed: {'description': 'denim jacket', 'size': 'S', 'max_price': 50.0}

- typical_price: 35.5 (sample_size 8)
- every search result rated: True (1 rated / 1 results)
- all labels valid: True

Labels (actual vs. 20% rule):

| id | title | price | deal | expected | match |
|---|---|---|---|---|---|
| lst_007 | Denim Jacket — Light Wash, Cropped | 42.0 | fair | fair | yes |

Comparables for 'denim jacket' (8):

- Vintage Levi's 501 Jeans — Medium Wash — $38.0
- 90s Track Jacket — Navy/White Stripe — $45.0
- Denim Jacket — Light Wash, Cropped — $42.0
- High-Waisted Denim Shorts — Cutoff — $24.0
- 90s Leather Bomber — Black — $75.0
- Shacket — Olive Canvas — $33.0
- Straight Leg Black Jeans — Faded — $30.0
- Denim Vest — Medium Wash, Studded — $27.0

Outfit suggestion:

```
* **The Double Denim Contrast:** Tuck the **white ribbed tank top** into the **baggy straight-leg jeans, dark wash**, secure it with the **brown leather belt**, and layer the light wash cropped denim jacket right over top to play with the two-tone indigo shades. Finish this streetwear-inspired look with the **chunky white sneakers** and the **black crossbody bag**.
* **The High-Contrast Neutral:** Pair the **wide-leg khaki trousers** with the **white ribbed tank top**, and wear the light wash cropped denim jacket open to highlight the high waist. Ground the earthy tones with the **black combat boots** and sling the **black crossbody bag** across your chest for an effortless finish.
```

Fit card:

```
Scored this cropped light wash denim jacket on Poshmark for $42 and I'm obsessed with the structured shoulders. Been living in it with baggy dark jeans for the ultimate double-denim look.
```

- Character count (including spaces): 187

Trace:

```
[1] parse_query
      in:  denim jacket size S under $50
      out: dict with keys: description, size, max_price
      →    parsed by model
[2] estimate_price
      in:  dict with keys: description, results
      out: dict with keys: typical_price, sample_size, rated
[3] select_item
      in:  1 results
      out: Denim Jacket — Light Wash, Cropped ($42.0, poshmark)
      →    selected first result
[4] suggest_outfit
      in:  dict with keys: item, wardrobe_items
      out: * **The Double Denim Contrast:** Tuck the **white ribbed tank top** into the **baggy straight-leg jeans, dark …
[5] create_fit_card
      in:  dict with keys: item, outfit
      out: Scored this cropped light wash denim jacket on Poshmark for $42 and I'm obsessed with the structured shoulders…
```

**Try 2**

- stopped early: no
- selected_item: Denim Jacket — Light Wash, Cropped ($42.0, poshmark)
- search_results: 1

- parsed_by: model — parsed: {'description': 'denim jacket', 'size': 'S', 'max_price': 50.0}

- typical_price: 35.5 (sample_size 8)
- every search result rated: True (1 rated / 1 results)
- all labels valid: True

Labels (actual vs. 20% rule):

| id | title | price | deal | expected | match |
|---|---|---|---|---|---|
| lst_007 | Denim Jacket — Light Wash, Cropped | 42.0 | fair | fair | yes |

Comparables for 'denim jacket' (8):

- Vintage Levi's 501 Jeans — Medium Wash — $38.0
- 90s Track Jacket — Navy/White Stripe — $45.0
- Denim Jacket — Light Wash, Cropped — $42.0
- High-Waisted Denim Shorts — Cutoff — $24.0
- 90s Leather Bomber — Black — $75.0
- Shacket — Olive Canvas — $33.0
- Straight Leg Black Jeans — Faded — $30.0
- Denim Vest — Medium Wash, Studded — $27.0

Outfit suggestion:

```
* **The Double Denim Contrast:** Tuck the **white ribbed tank top** into the **baggy straight-leg jeans, dark wash**, secure it with the **brown leather belt**, and layer the light wash cropped denim jacket right over top to play with the two-tone indigo shades. Finish this streetwear-inspired look with the **chunky white sneakers** and the **black crossbody bag**.
* **The High-Contrast Neutral:** Pair the **wide-leg khaki trousers** with the **white ribbed tank top**, and wear the light wash cropped denim jacket open to highlight the high waist. Ground the earthy tones with the **black combat boots** and sling the **black crossbody bag** across your chest for an effortless finish.
```

Fit card:

```
scored this cropped light wash denim jacket on poshmark for $42 and i am obsessed. love the structured shoulders. wearing it double denim today with dark wash jeans and chunky sneakers.
```

- Character count (including spaces): 185

Trace:

```
[1] parse_query
      in:  denim jacket size S under $50
      out: dict with keys: description, size, max_price
      →    parsed by model
[2] estimate_price
      in:  dict with keys: description, results
      out: dict with keys: typical_price, sample_size, rated
[3] select_item
      in:  1 results
      out: Denim Jacket — Light Wash, Cropped ($42.0, poshmark)
      →    selected first result
[4] suggest_outfit
      in:  dict with keys: item, wardrobe_items
      out: * **The Double Denim Contrast:** Tuck the **white ribbed tank top** into the **baggy straight-leg jeans, dark …
[5] create_fit_card
      in:  dict with keys: item, outfit
      out: scored this cropped light wash denim jacket on poshmark for $42 and i am obsessed. love the structured shoulde…
```

**Try 3**

- stopped early: no
- selected_item: Denim Jacket — Light Wash, Cropped ($42.0, poshmark)
- search_results: 1

- parsed_by: model — parsed: {'description': 'denim jacket', 'size': 'S', 'max_price': 50.0}

- typical_price: 35.5 (sample_size 8)
- every search result rated: True (1 rated / 1 results)
- all labels valid: True

Labels (actual vs. 20% rule):

| id | title | price | deal | expected | match |
|---|---|---|---|---|---|
| lst_007 | Denim Jacket — Light Wash, Cropped | 42.0 | fair | fair | yes |

Comparables for 'denim jacket' (8):

- Vintage Levi's 501 Jeans — Medium Wash — $38.0
- 90s Track Jacket — Navy/White Stripe — $45.0
- Denim Jacket — Light Wash, Cropped — $42.0
- High-Waisted Denim Shorts — Cutoff — $24.0
- 90s Leather Bomber — Black — $75.0
- Shacket — Olive Canvas — $33.0
- Straight Leg Black Jeans — Faded — $30.0
- Denim Vest — Medium Wash, Studded — $27.0

Outfit suggestion:

```
* **The Double Denim Contrast:** Tuck the **white ribbed tank top** into the **baggy straight-leg jeans, dark wash**, secure it with the **brown leather belt**, and layer the light wash cropped denim jacket right over top to play with the two-tone indigo shades. Finish this streetwear-inspired look with the **chunky white sneakers** and the **black crossbody bag**.
* **The High-Contrast Neutral:** Pair the **wide-leg khaki trousers** with the **white ribbed tank top**, and wear the light wash cropped denim jacket open to highlight the high waist. Ground the earthy tones with the **black combat boots** and sling the **black crossbody bag** across your chest for an effortless finish.
```

Fit card:

```
Scored this cropped light wash denim jacket on Poshmark for $42 and I’m obsessed with the structured shoulders. Perfect blank canvas for custom patches, but I love styling it with baggy dark wash jeans for that ultimate double denim streetwear look.
```

- Character count (including spaces): 249

Trace:

```
[1] parse_query
      in:  denim jacket size S under $50
      out: dict with keys: description, size, max_price
      →    parsed by model
[2] estimate_price
      in:  dict with keys: description, results
      out: dict with keys: typical_price, sample_size, rated
[3] select_item
      in:  1 results
      out: Denim Jacket — Light Wash, Cropped ($42.0, poshmark)
      →    selected first result
[4] suggest_outfit
      in:  dict with keys: item, wardrobe_items
      out: * **The Double Denim Contrast:** Tuck the **white ribbed tank top** into the **baggy straight-leg jeans, dark …
[5] create_fit_card
      in:  dict with keys: item, outfit
      out: Scored this cropped light wash denim jacket on Poshmark for $42 and I’m obsessed with the structured shoulders…
```

**Try 4**

- stopped early: no
- selected_item: Denim Jacket — Light Wash, Cropped ($42.0, poshmark)
- search_results: 1

- parsed_by: model — parsed: {'description': 'denim jacket', 'size': 'S', 'max_price': 50.0}

- typical_price: 35.5 (sample_size 8)
- every search result rated: True (1 rated / 1 results)
- all labels valid: True

Labels (actual vs. 20% rule):

| id | title | price | deal | expected | match |
|---|---|---|---|---|---|
| lst_007 | Denim Jacket — Light Wash, Cropped | 42.0 | fair | fair | yes |

Comparables for 'denim jacket' (8):

- Vintage Levi's 501 Jeans — Medium Wash — $38.0
- 90s Track Jacket — Navy/White Stripe — $45.0
- Denim Jacket — Light Wash, Cropped — $42.0
- High-Waisted Denim Shorts — Cutoff — $24.0
- 90s Leather Bomber — Black — $75.0
- Shacket — Olive Canvas — $33.0
- Straight Leg Black Jeans — Faded — $30.0
- Denim Vest — Medium Wash, Studded — $27.0

Outfit suggestion:

```
* **The Double Denim Contrast:** Tuck the **white ribbed tank top** into the **baggy straight-leg jeans, dark wash**, secure it with the **brown leather belt**, and layer the light wash cropped denim jacket right over top to play with the two-tone indigo shades. Finish this streetwear-inspired look with the **chunky white sneakers** and the **black crossbody bag**.
* **The High-Contrast Neutral:** Pair the **wide-leg khaki trousers** with the **white ribbed tank top**, and wear the light wash cropped denim jacket open to highlight the high waist. Ground the earthy tones with the **black combat boots** and sling the **black crossbody bag** across your chest for an effortless finish.
```

Fit card:

```
Scored this cropped light wash denim jacket on Poshmark for $42 and I'm obsessed with the structured shoulders. Obsessed with throwing it over baggy dark wash jeans for a full double-denim streetwear look.
```

- Character count (including spaces): 205

Trace:

```
[1] parse_query
      in:  denim jacket size S under $50
      out: dict with keys: description, size, max_price
      →    parsed by model
[2] estimate_price
      in:  dict with keys: description, results
      out: dict with keys: typical_price, sample_size, rated
[3] select_item
      in:  1 results
      out: Denim Jacket — Light Wash, Cropped ($42.0, poshmark)
      →    selected first result
[4] suggest_outfit
      in:  dict with keys: item, wardrobe_items
      out: * **The Double Denim Contrast:** Tuck the **white ribbed tank top** into the **baggy straight-leg jeans, dark …
[5] create_fit_card
      in:  dict with keys: item, outfit
      out: Scored this cropped light wash denim jacket on Poshmark for $42 and I'm obsessed with the structured shoulders…
```

**Try 5**

- stopped early: no
- selected_item: Denim Jacket — Light Wash, Cropped ($42.0, poshmark)
- search_results: 1

- parsed_by: model — parsed: {'description': 'denim jacket', 'size': 'S', 'max_price': 50.0}

- typical_price: 35.5 (sample_size 8)
- every search result rated: True (1 rated / 1 results)
- all labels valid: True

Labels (actual vs. 20% rule):

| id | title | price | deal | expected | match |
|---|---|---|---|---|---|
| lst_007 | Denim Jacket — Light Wash, Cropped | 42.0 | fair | fair | yes |

Comparables for 'denim jacket' (8):

- Vintage Levi's 501 Jeans — Medium Wash — $38.0
- 90s Track Jacket — Navy/White Stripe — $45.0
- Denim Jacket — Light Wash, Cropped — $42.0
- High-Waisted Denim Shorts — Cutoff — $24.0
- 90s Leather Bomber — Black — $75.0
- Shacket — Olive Canvas — $33.0
- Straight Leg Black Jeans — Faded — $30.0
- Denim Vest — Medium Wash, Studded — $27.0

Outfit suggestion:

```
* **The Double Denim Contrast:** Tuck the **white ribbed tank top** into the **baggy straight-leg jeans, dark wash**, secure it with the **brown leather belt**, and layer the light wash cropped denim jacket right over top to play with the two-tone indigo shades. Finish this streetwear-inspired look with the **chunky white sneakers** and the **black crossbody bag**.
* **The High-Contrast Neutral:** Pair the **wide-leg khaki trousers** with the **white ribbed tank top**, and wear the light wash cropped denim jacket open to highlight the high waist. Ground the earthy tones with the **black combat boots** and sling the **black crossbody bag** across your chest for an effortless finish.
```

Fit card:

```
Scored this cropped light-wash denim jacket on Poshmark for $42 and honestly obsessed with the structured shoulders. Obsessed with layering it over baggy dark denim for that two-tone streetwear vibe.
```

- Character count (including spaces): 199

Trace:

```
[1] parse_query
      in:  denim jacket size S under $50
      out: dict with keys: description, size, max_price
      →    parsed by model
[2] estimate_price
      in:  dict with keys: description, results
      out: dict with keys: typical_price, sample_size, rated
[3] select_item
      in:  1 results
      out: Denim Jacket — Light Wash, Cropped ($42.0, poshmark)
      →    selected first result
[4] suggest_outfit
      in:  dict with keys: item, wardrobe_items
      out: * **The Double Denim Contrast:** Tuck the **white ribbed tank top** into the **baggy straight-leg jeans, dark …
[5] create_fit_card
      in:  dict with keys: item, outfit
      out: Scored this cropped light-wash denim jacket on Poshmark for $42 and honestly obsessed with the structured shou…
```

### fit card under 280 chars, names item + outfit

- Query: `black leather bomber jacket under $80`
- Wardrobe: example

**Try 1**

- stopped early: no
- selected_item: 90s Leather Bomber — Black ($75.0, depop)
- search_results: 10

- parsed_by: model — parsed: {'description': 'black leather bomber jacket', 'size': None, 'max_price': 80.0}

- typical_price: 31.5 (sample_size 14)
- every search result rated: True (10 rated / 10 results)
- all labels valid: True

Labels (actual vs. 20% rule):

| id | title | price | deal | expected | match |
|---|---|---|---|---|---|
| lst_022 | 90s Leather Bomber — Black | 75.0 | overpriced | overpriced | yes |
| lst_009 | Platform Mary Janes — Black Patent | 55.0 | overpriced | overpriced | yes |
| lst_003 | Oversized Flannel Shirt — Plaid Red/Black | 22.0 | good deal | good deal | yes |
| lst_004 | 90s Track Jacket — Navy/White Stripe | 45.0 | overpriced | overpriced | yes |
| lst_007 | Denim Jacket — Light Wash, Cropped | 42.0 | overpriced | overpriced | yes |
| lst_014 | Leather Belt — Brown, Braided | 12.0 | good deal | good deal | yes |
| lst_015 | Vintage Graphic Hoodie — Faded Black | 26.0 | fair | fair | yes |
| lst_017 | Mesh Long-Sleeve Top — Black | 15.0 | good deal | good deal | yes |
| lst_026 | Biker Shorts — Black, Shiny | 14.0 | good deal | good deal | yes |
| lst_037 | Straight Leg Black Jeans — Faded | 30.0 | fair | fair | yes |

Comparables for 'black leather bomber jacket' (14):

- Oversized Flannel Shirt — Plaid Red/Black — $22.0
- 90s Track Jacket — Navy/White Stripe — $45.0
- Graphic Tee — 2003 Tour Bootleg Style — $24.0
- Denim Jacket — Light Wash, Cropped — $42.0
- Platform Mary Janes — Black Patent — $55.0
- Vintage Windbreaker — Color Block Purple/Teal — $40.0
- Leather Belt — Brown, Braided — $12.0
- Vintage Graphic Hoodie — Faded Black — $26.0
- Mesh Long-Sleeve Top — Black — $15.0
- 90s Leather Bomber — Black — $75.0
- Biker Shorts — Black, Shiny — $14.0
- Shacket — Olive Canvas — $33.0
- Straight Leg Black Jeans — Faded — $30.0
- Mini Shoulder Bag — Tan Leather — $38.0

Outfit suggestion:

```
* **Look 1 (90s Off-Duty Model):** Layer your white ribbed tank top tucked into the baggy straight-leg jeans (add the brown leather belt for contrast), and throw the black leather bomber on top. Finish with the chunky white sneakers and the black crossbody bag for an effortless, boxy-meets-fitted silhouette. 
* **Look 2 (Grunge Streetwear):** Wear the black cropped zip hoodie underneath the black leather bomber so the hood lays flat over the collar. Pair with the baggy straight-leg jeans and black combat boots for a monochrome texture-play that leans into the jacket's vintage grunge roots.
```

Fit card:

```
scored this vintage leather bomber for $75 on depop and i’m obsessed. it has that perfect 90s boxy fit. looks so good thrown over a hoodie with combat boots for major grunge energy.
```

- Character count (including spaces): 181

Trace:

```
[1] parse_query
      in:  black leather bomber jacket under $80
      out: dict with keys: description, size, max_price
      →    parsed by model
[2] estimate_price
      in:  dict with keys: description, results
      out: dict with keys: typical_price, sample_size, rated
[3] select_item
      in:  10 results
      out: 90s Leather Bomber — Black ($75.0, depop)
      →    selected first result
[4] suggest_outfit
      in:  dict with keys: item, wardrobe_items
      out: * **Look 1 (90s Off-Duty Model):** Layer your white ribbed tank top tucked into the baggy straight-leg jeans (…
[5] create_fit_card
      in:  dict with keys: item, outfit
      out: scored this vintage leather bomber for $75 on depop and i’m obsessed. it has that perfect 90s boxy fit. looks …
```

**Try 2**

- stopped early: no
- selected_item: 90s Leather Bomber — Black ($75.0, depop)
- search_results: 10

- parsed_by: model — parsed: {'description': 'black leather bomber jacket', 'size': None, 'max_price': 80.0}

- typical_price: 31.5 (sample_size 14)
- every search result rated: True (10 rated / 10 results)
- all labels valid: True

Labels (actual vs. 20% rule):

| id | title | price | deal | expected | match |
|---|---|---|---|---|---|
| lst_022 | 90s Leather Bomber — Black | 75.0 | overpriced | overpriced | yes |
| lst_009 | Platform Mary Janes — Black Patent | 55.0 | overpriced | overpriced | yes |
| lst_003 | Oversized Flannel Shirt — Plaid Red/Black | 22.0 | good deal | good deal | yes |
| lst_004 | 90s Track Jacket — Navy/White Stripe | 45.0 | overpriced | overpriced | yes |
| lst_007 | Denim Jacket — Light Wash, Cropped | 42.0 | overpriced | overpriced | yes |
| lst_014 | Leather Belt — Brown, Braided | 12.0 | good deal | good deal | yes |
| lst_015 | Vintage Graphic Hoodie — Faded Black | 26.0 | fair | fair | yes |
| lst_017 | Mesh Long-Sleeve Top — Black | 15.0 | good deal | good deal | yes |
| lst_026 | Biker Shorts — Black, Shiny | 14.0 | good deal | good deal | yes |
| lst_037 | Straight Leg Black Jeans — Faded | 30.0 | fair | fair | yes |

Comparables for 'black leather bomber jacket' (14):

- Oversized Flannel Shirt — Plaid Red/Black — $22.0
- 90s Track Jacket — Navy/White Stripe — $45.0
- Graphic Tee — 2003 Tour Bootleg Style — $24.0
- Denim Jacket — Light Wash, Cropped — $42.0
- Platform Mary Janes — Black Patent — $55.0
- Vintage Windbreaker — Color Block Purple/Teal — $40.0
- Leather Belt — Brown, Braided — $12.0
- Vintage Graphic Hoodie — Faded Black — $26.0
- Mesh Long-Sleeve Top — Black — $15.0
- 90s Leather Bomber — Black — $75.0
- Biker Shorts — Black, Shiny — $14.0
- Shacket — Olive Canvas — $33.0
- Straight Leg Black Jeans — Faded — $30.0
- Mini Shoulder Bag — Tan Leather — $38.0

Outfit suggestion:

```
* **Look 1 (90s Off-Duty Model):** Layer your white ribbed tank top tucked into the baggy straight-leg jeans (add the brown leather belt for contrast), and throw the black leather bomber on top. Finish with the chunky white sneakers and the black crossbody bag for an effortless, boxy-meets-fitted silhouette. 
* **Look 2 (Grunge Streetwear):** Wear the black cropped zip hoodie underneath the black leather bomber so the hood lays flat over the collar. Pair with the baggy straight-leg jeans and black combat boots for a monochrome texture-play that leans into the jacket's vintage grunge roots.
```

Fit card:

```
Finally scored the ultimate 90s leather bomber on Depop for $75. It has the best broken-in creases. Wearing it boxy over a zip hoodie and combat boots for max grunge energy.
```

- Character count (including spaces): 173

Trace:

```
[1] parse_query
      in:  black leather bomber jacket under $80
      out: dict with keys: description, size, max_price
      →    parsed by model
[2] estimate_price
      in:  dict with keys: description, results
      out: dict with keys: typical_price, sample_size, rated
[3] select_item
      in:  10 results
      out: 90s Leather Bomber — Black ($75.0, depop)
      →    selected first result
[4] suggest_outfit
      in:  dict with keys: item, wardrobe_items
      out: * **Look 1 (90s Off-Duty Model):** Layer your white ribbed tank top tucked into the baggy straight-leg jeans (…
[5] create_fit_card
      in:  dict with keys: item, outfit
      out: Finally scored the ultimate 90s leather bomber on Depop for $75. It has the best broken-in creases. Wearing it…
```

**Try 3**

- stopped early: no
- selected_item: 90s Leather Bomber — Black ($75.0, depop)
- search_results: 10

- parsed_by: model — parsed: {'description': 'black leather bomber jacket', 'size': None, 'max_price': 80.0}

- typical_price: 31.5 (sample_size 14)
- every search result rated: True (10 rated / 10 results)
- all labels valid: True

Labels (actual vs. 20% rule):

| id | title | price | deal | expected | match |
|---|---|---|---|---|---|
| lst_022 | 90s Leather Bomber — Black | 75.0 | overpriced | overpriced | yes |
| lst_009 | Platform Mary Janes — Black Patent | 55.0 | overpriced | overpriced | yes |
| lst_003 | Oversized Flannel Shirt — Plaid Red/Black | 22.0 | good deal | good deal | yes |
| lst_004 | 90s Track Jacket — Navy/White Stripe | 45.0 | overpriced | overpriced | yes |
| lst_007 | Denim Jacket — Light Wash, Cropped | 42.0 | overpriced | overpriced | yes |
| lst_014 | Leather Belt — Brown, Braided | 12.0 | good deal | good deal | yes |
| lst_015 | Vintage Graphic Hoodie — Faded Black | 26.0 | fair | fair | yes |
| lst_017 | Mesh Long-Sleeve Top — Black | 15.0 | good deal | good deal | yes |
| lst_026 | Biker Shorts — Black, Shiny | 14.0 | good deal | good deal | yes |
| lst_037 | Straight Leg Black Jeans — Faded | 30.0 | fair | fair | yes |

Comparables for 'black leather bomber jacket' (14):

- Oversized Flannel Shirt — Plaid Red/Black — $22.0
- 90s Track Jacket — Navy/White Stripe — $45.0
- Graphic Tee — 2003 Tour Bootleg Style — $24.0
- Denim Jacket — Light Wash, Cropped — $42.0
- Platform Mary Janes — Black Patent — $55.0
- Vintage Windbreaker — Color Block Purple/Teal — $40.0
- Leather Belt — Brown, Braided — $12.0
- Vintage Graphic Hoodie — Faded Black — $26.0
- Mesh Long-Sleeve Top — Black — $15.0
- 90s Leather Bomber — Black — $75.0
- Biker Shorts — Black, Shiny — $14.0
- Shacket — Olive Canvas — $33.0
- Straight Leg Black Jeans — Faded — $30.0
- Mini Shoulder Bag — Tan Leather — $38.0

Outfit suggestion:

```
* **Look 1 (90s Off-Duty Model):** Layer your white ribbed tank top tucked into the baggy straight-leg jeans (add the brown leather belt for contrast), and throw the black leather bomber on top. Finish with the chunky white sneakers and the black crossbody bag for an effortless, boxy-meets-fitted silhouette. 
* **Look 2 (Grunge Streetwear):** Wear the black cropped zip hoodie underneath the black leather bomber so the hood lays flat over the collar. Pair with the baggy straight-leg jeans and black combat boots for a monochrome texture-play that leans into the jacket's vintage grunge roots.
```

Fit card:

```
scored this vintage leather bomber on depop for $75 and honestly haven’t taken it off since. obsessed with styling it over a baggy hoodie and combat boots for full grunge energy.
```

- Character count (including spaces): 178

Trace:

```
[1] parse_query
      in:  black leather bomber jacket under $80
      out: dict with keys: description, size, max_price
      →    parsed by model
[2] estimate_price
      in:  dict with keys: description, results
      out: dict with keys: typical_price, sample_size, rated
[3] select_item
      in:  10 results
      out: 90s Leather Bomber — Black ($75.0, depop)
      →    selected first result
[4] suggest_outfit
      in:  dict with keys: item, wardrobe_items
      out: * **Look 1 (90s Off-Duty Model):** Layer your white ribbed tank top tucked into the baggy straight-leg jeans (…
[5] create_fit_card
      in:  dict with keys: item, outfit
      out: scored this vintage leather bomber on depop for $75 and honestly haven’t taken it off since. obsessed with sty…
```

**Try 4**

- stopped early: no
- selected_item: 90s Leather Bomber — Black ($75.0, depop)
- search_results: 10

- parsed_by: model — parsed: {'description': 'black leather bomber jacket', 'size': None, 'max_price': 80.0}

- typical_price: 31.5 (sample_size 14)
- every search result rated: True (10 rated / 10 results)
- all labels valid: True

Labels (actual vs. 20% rule):

| id | title | price | deal | expected | match |
|---|---|---|---|---|---|
| lst_022 | 90s Leather Bomber — Black | 75.0 | overpriced | overpriced | yes |
| lst_009 | Platform Mary Janes — Black Patent | 55.0 | overpriced | overpriced | yes |
| lst_003 | Oversized Flannel Shirt — Plaid Red/Black | 22.0 | good deal | good deal | yes |
| lst_004 | 90s Track Jacket — Navy/White Stripe | 45.0 | overpriced | overpriced | yes |
| lst_007 | Denim Jacket — Light Wash, Cropped | 42.0 | overpriced | overpriced | yes |
| lst_014 | Leather Belt — Brown, Braided | 12.0 | good deal | good deal | yes |
| lst_015 | Vintage Graphic Hoodie — Faded Black | 26.0 | fair | fair | yes |
| lst_017 | Mesh Long-Sleeve Top — Black | 15.0 | good deal | good deal | yes |
| lst_026 | Biker Shorts — Black, Shiny | 14.0 | good deal | good deal | yes |
| lst_037 | Straight Leg Black Jeans — Faded | 30.0 | fair | fair | yes |

Comparables for 'black leather bomber jacket' (14):

- Oversized Flannel Shirt — Plaid Red/Black — $22.0
- 90s Track Jacket — Navy/White Stripe — $45.0
- Graphic Tee — 2003 Tour Bootleg Style — $24.0
- Denim Jacket — Light Wash, Cropped — $42.0
- Platform Mary Janes — Black Patent — $55.0
- Vintage Windbreaker — Color Block Purple/Teal — $40.0
- Leather Belt — Brown, Braided — $12.0
- Vintage Graphic Hoodie — Faded Black — $26.0
- Mesh Long-Sleeve Top — Black — $15.0
- 90s Leather Bomber — Black — $75.0
- Biker Shorts — Black, Shiny — $14.0
- Shacket — Olive Canvas — $33.0
- Straight Leg Black Jeans — Faded — $30.0
- Mini Shoulder Bag — Tan Leather — $38.0

Outfit suggestion:

```
* **Look 1 (90s Off-Duty Model):** Layer your white ribbed tank top tucked into the baggy straight-leg jeans (add the brown leather belt for contrast), and throw the black leather bomber on top. Finish with the chunky white sneakers and the black crossbody bag for an effortless, boxy-meets-fitted silhouette. 
* **Look 2 (Grunge Streetwear):** Wear the black cropped zip hoodie underneath the black leather bomber so the hood lays flat over the collar. Pair with the baggy straight-leg jeans and black combat boots for a monochrome texture-play that leans into the jacket's vintage grunge roots.
```

Fit card:

```
Found this holy grail 90s leather bomber on Depop for $75. Obsessed with how the boxy fit looks over a cropped hoodie and combat boots for total grunge vibes.
```

- Character count (including spaces): 158

Trace:

```
[1] parse_query
      in:  black leather bomber jacket under $80
      out: dict with keys: description, size, max_price
      →    parsed by model
[2] estimate_price
      in:  dict with keys: description, results
      out: dict with keys: typical_price, sample_size, rated
[3] select_item
      in:  10 results
      out: 90s Leather Bomber — Black ($75.0, depop)
      →    selected first result
[4] suggest_outfit
      in:  dict with keys: item, wardrobe_items
      out: * **Look 1 (90s Off-Duty Model):** Layer your white ribbed tank top tucked into the baggy straight-leg jeans (…
[5] create_fit_card
      in:  dict with keys: item, outfit
      out: Found this holy grail 90s leather bomber on Depop for $75. Obsessed with how the boxy fit looks over a cropped…
```

**Try 5**

- stopped early: no
- selected_item: 90s Leather Bomber — Black ($75.0, depop)
- search_results: 10

- parsed_by: model — parsed: {'description': 'black leather bomber jacket', 'size': None, 'max_price': 80.0}

- typical_price: 31.5 (sample_size 14)
- every search result rated: True (10 rated / 10 results)
- all labels valid: True

Labels (actual vs. 20% rule):

| id | title | price | deal | expected | match |
|---|---|---|---|---|---|
| lst_022 | 90s Leather Bomber — Black | 75.0 | overpriced | overpriced | yes |
| lst_009 | Platform Mary Janes — Black Patent | 55.0 | overpriced | overpriced | yes |
| lst_003 | Oversized Flannel Shirt — Plaid Red/Black | 22.0 | good deal | good deal | yes |
| lst_004 | 90s Track Jacket — Navy/White Stripe | 45.0 | overpriced | overpriced | yes |
| lst_007 | Denim Jacket — Light Wash, Cropped | 42.0 | overpriced | overpriced | yes |
| lst_014 | Leather Belt — Brown, Braided | 12.0 | good deal | good deal | yes |
| lst_015 | Vintage Graphic Hoodie — Faded Black | 26.0 | fair | fair | yes |
| lst_017 | Mesh Long-Sleeve Top — Black | 15.0 | good deal | good deal | yes |
| lst_026 | Biker Shorts — Black, Shiny | 14.0 | good deal | good deal | yes |
| lst_037 | Straight Leg Black Jeans — Faded | 30.0 | fair | fair | yes |

Comparables for 'black leather bomber jacket' (14):

- Oversized Flannel Shirt — Plaid Red/Black — $22.0
- 90s Track Jacket — Navy/White Stripe — $45.0
- Graphic Tee — 2003 Tour Bootleg Style — $24.0
- Denim Jacket — Light Wash, Cropped — $42.0
- Platform Mary Janes — Black Patent — $55.0
- Vintage Windbreaker — Color Block Purple/Teal — $40.0
- Leather Belt — Brown, Braided — $12.0
- Vintage Graphic Hoodie — Faded Black — $26.0
- Mesh Long-Sleeve Top — Black — $15.0
- 90s Leather Bomber — Black — $75.0
- Biker Shorts — Black, Shiny — $14.0
- Shacket — Olive Canvas — $33.0
- Straight Leg Black Jeans — Faded — $30.0
- Mini Shoulder Bag — Tan Leather — $38.0

Outfit suggestion:

```
* **Look 1 (90s Off-Duty Model):** Layer your white ribbed tank top tucked into the baggy straight-leg jeans (add the brown leather belt for contrast), and throw the black leather bomber on top. Finish with the chunky white sneakers and the black crossbody bag for an effortless, boxy-meets-fitted silhouette. 
* **Look 2 (Grunge Streetwear):** Wear the black cropped zip hoodie underneath the black leather bomber so the hood lays flat over the collar. Pair with the baggy straight-leg jeans and black combat boots for a monochrome texture-play that leans into the jacket's vintage grunge roots.
```

Fit card:

```
scored this 90s leather bomber on depop for $75 and honestly haven't taken it off since. obsessed with styling it over a baggy hoodie and combat boots for full grunge mode.
```

- Character count (including spaces): 172

Trace:

```
[1] parse_query
      in:  black leather bomber jacket under $80
      out: dict with keys: description, size, max_price
      →    parsed by model
[2] estimate_price
      in:  dict with keys: description, results
      out: dict with keys: typical_price, sample_size, rated
[3] select_item
      in:  10 results
      out: 90s Leather Bomber — Black ($75.0, depop)
      →    selected first result
[4] suggest_outfit
      in:  dict with keys: item, wardrobe_items
      out: * **Look 1 (90s Off-Duty Model):** Layer your white ribbed tank top tucked into the baggy straight-leg jeans (…
[5] create_fit_card
      in:  dict with keys: item, outfit
      out: scored this 90s leather bomber on depop for $75 and honestly haven't taken it off since. obsessed with styling…
```

### regex fallback when model unreachable

- Query: `silk slip dress size M under $40`
- Wardrobe: example

**Try 1**

- stopped early: no
- selected_item: 90s Silk Slip Dress — Floral, Midi Length ($30.0, depop)
- search_results: 2

- parsed_by: regex — parsed: {'description': 'silk slip dress', 'size': 'M', 'max_price': 40.0}

- typical_price: None (sample_size 2)
- every search result rated: True (2 rated / 2 results)
- all labels valid: True

Labels (actual vs. 20% rule):

| id | title | price | deal | expected | match |
|---|---|---|---|---|---|
| lst_013 | 90s Silk Slip Dress — Floral, Midi Length | 30.0 | unknown | unknown | yes |
| lst_029 | Silk Button-Down — Sage Green | 28.0 | unknown | unknown | yes |

Comparables for 'silk slip dress' (2):

- 90s Silk Slip Dress — Floral, Midi Length — $30.0
- Silk Button-Down — Sage Green — $28.0

Outfit suggestion:

```
* **The 90s Grunge Contrast:** Layer your oversized grey crewneck sweatshirt right over the floral slip dress to turn it into a skirt. Pair with black combat boots and the black crossbody bag for a casual, textured look that balances the feminine print. 
* **The Streetwear Layer:** Wear the slip dress over your white ribbed tank top, and throw the black cropped zip hoodie on top, left unzipped to frame the neckline. Finish with chunky white sneakers for an effortless, sporty-vintage vibe.
```

Fit card:

```
Found this dreamy 90s floral slip dress on Depop for just $30. Obsessed with styling it under an oversized grey crewneck and combat boots for that grungy, textured look.
```

- Character count (including spaces): 169

Trace:

```
[1] parse_query
      in:  silk slip dress size M under $40
      out: dict with keys: description, size, max_price
      →    parsed by regex
[2] estimate_price
      in:  dict with keys: description, results
      out: dict with keys: typical_price, sample_size, rated
[3] select_item
      in:  2 results
      out: 90s Silk Slip Dress — Floral, Midi Length ($30.0, depop)
      →    selected first result
[4] suggest_outfit
      in:  dict with keys: item, wardrobe_items
      out: * **The 90s Grunge Contrast:** Layer your oversized grey crewneck sweatshirt right over the floral slip dress …
[5] create_fit_card
      in:  dict with keys: item, outfit
      out: Found this dreamy 90s floral slip dress on Depop for just $30. Obsessed with styling it under an oversized gre…
```

**Try 2**

- stopped early: no
- selected_item: 90s Silk Slip Dress — Floral, Midi Length ($30.0, depop)
- search_results: 2

- parsed_by: regex — parsed: {'description': 'silk slip dress', 'size': 'M', 'max_price': 40.0}

- typical_price: None (sample_size 2)
- every search result rated: True (2 rated / 2 results)
- all labels valid: True

Labels (actual vs. 20% rule):

| id | title | price | deal | expected | match |
|---|---|---|---|---|---|
| lst_013 | 90s Silk Slip Dress — Floral, Midi Length | 30.0 | unknown | unknown | yes |
| lst_029 | Silk Button-Down — Sage Green | 28.0 | unknown | unknown | yes |

Comparables for 'silk slip dress' (2):

- 90s Silk Slip Dress — Floral, Midi Length — $30.0
- Silk Button-Down — Sage Green — $28.0

Outfit suggestion:

```
* **The 90s Grunge Contrast:** Layer your oversized grey crewneck sweatshirt right over the floral slip dress to turn it into a skirt. Pair with black combat boots and the black crossbody bag for a casual, textured look that balances the feminine print. 
* **The Streetwear Layer:** Wear the slip dress over your white ribbed tank top, and throw the black cropped zip hoodie on top, left unzipped to frame the neckline. Finish with chunky white sneakers for an effortless, sporty-vintage vibe.
```

Fit card:

```
found this dream 90s floral slip on depop for just 30 bucks. obsessed with styling it grunge-core with an oversized grey crewneck and beat-up combat boots.
```

- Character count (including spaces): 155

Trace:

```
[1] parse_query
      in:  silk slip dress size M under $40
      out: dict with keys: description, size, max_price
      →    parsed by regex
[2] estimate_price
      in:  dict with keys: description, results
      out: dict with keys: typical_price, sample_size, rated
[3] select_item
      in:  2 results
      out: 90s Silk Slip Dress — Floral, Midi Length ($30.0, depop)
      →    selected first result
[4] suggest_outfit
      in:  dict with keys: item, wardrobe_items
      out: * **The 90s Grunge Contrast:** Layer your oversized grey crewneck sweatshirt right over the floral slip dress …
[5] create_fit_card
      in:  dict with keys: item, outfit
      out: found this dream 90s floral slip on depop for just 30 bucks. obsessed with styling it grunge-core with an over…
```

**Try 3**

- stopped early: no
- selected_item: 90s Silk Slip Dress — Floral, Midi Length ($30.0, depop)
- search_results: 2

- parsed_by: regex — parsed: {'description': 'silk slip dress', 'size': 'M', 'max_price': 40.0}

- typical_price: None (sample_size 2)
- every search result rated: True (2 rated / 2 results)
- all labels valid: True

Labels (actual vs. 20% rule):

| id | title | price | deal | expected | match |
|---|---|---|---|---|---|
| lst_013 | 90s Silk Slip Dress — Floral, Midi Length | 30.0 | unknown | unknown | yes |
| lst_029 | Silk Button-Down — Sage Green | 28.0 | unknown | unknown | yes |

Comparables for 'silk slip dress' (2):

- 90s Silk Slip Dress — Floral, Midi Length — $30.0
- Silk Button-Down — Sage Green — $28.0

Outfit suggestion:

```
* **The 90s Grunge Contrast:** Layer your oversized grey crewneck sweatshirt right over the floral slip dress to turn it into a skirt. Pair with black combat boots and the black crossbody bag for a casual, textured look that balances the feminine print. 
* **The Streetwear Layer:** Wear the slip dress over your white ribbed tank top, and throw the black cropped zip hoodie on top, left unzipped to frame the neckline. Finish with chunky white sneakers for an effortless, sporty-vintage vibe.
```

Fit card:

```
scored this dreamy 90s floral slip dress for just $30 on depop. obsessed with styling it grunge-style with an oversized grey crewneck and combat boots!
```

- Character count (including spaces): 151

Trace:

```
[1] parse_query
      in:  silk slip dress size M under $40
      out: dict with keys: description, size, max_price
      →    parsed by regex
[2] estimate_price
      in:  dict with keys: description, results
      out: dict with keys: typical_price, sample_size, rated
[3] select_item
      in:  2 results
      out: 90s Silk Slip Dress — Floral, Midi Length ($30.0, depop)
      →    selected first result
[4] suggest_outfit
      in:  dict with keys: item, wardrobe_items
      out: * **The 90s Grunge Contrast:** Layer your oversized grey crewneck sweatshirt right over the floral slip dress …
[5] create_fit_card
      in:  dict with keys: item, outfit
      out: scored this dreamy 90s floral slip dress for just $30 on depop. obsessed with styling it grunge-style with an …
```

**Try 4**

- stopped early: no
- selected_item: 90s Silk Slip Dress — Floral, Midi Length ($30.0, depop)
- search_results: 2

- parsed_by: regex — parsed: {'description': 'silk slip dress', 'size': 'M', 'max_price': 40.0}

- typical_price: None (sample_size 2)
- every search result rated: True (2 rated / 2 results)
- all labels valid: True

Labels (actual vs. 20% rule):

| id | title | price | deal | expected | match |
|---|---|---|---|---|---|
| lst_013 | 90s Silk Slip Dress — Floral, Midi Length | 30.0 | unknown | unknown | yes |
| lst_029 | Silk Button-Down — Sage Green | 28.0 | unknown | unknown | yes |

Comparables for 'silk slip dress' (2):

- 90s Silk Slip Dress — Floral, Midi Length — $30.0
- Silk Button-Down — Sage Green — $28.0

Outfit suggestion:

```
* **The 90s Grunge Contrast:** Layer your oversized grey crewneck sweatshirt right over the floral slip dress to turn it into a skirt. Pair with black combat boots and the black crossbody bag for a casual, textured look that balances the feminine print. 
* **The Streetwear Layer:** Wear the slip dress over your white ribbed tank top, and throw the black cropped zip hoodie on top, left unzipped to frame the neckline. Finish with chunky white sneakers for an effortless, sporty-vintage vibe.
```

Fit card:

```
scored this gorgeous 90s floral slip dress for just $30 on depop. obsessed with styling it grunge-style with an oversized crewneck and chunky boots!
```

- Character count (including spaces): 148

Trace:

```
[1] parse_query
      in:  silk slip dress size M under $40
      out: dict with keys: description, size, max_price
      →    parsed by regex
[2] estimate_price
      in:  dict with keys: description, results
      out: dict with keys: typical_price, sample_size, rated
[3] select_item
      in:  2 results
      out: 90s Silk Slip Dress — Floral, Midi Length ($30.0, depop)
      →    selected first result
[4] suggest_outfit
      in:  dict with keys: item, wardrobe_items
      out: * **The 90s Grunge Contrast:** Layer your oversized grey crewneck sweatshirt right over the floral slip dress …
[5] create_fit_card
      in:  dict with keys: item, outfit
      out: scored this gorgeous 90s floral slip dress for just $30 on depop. obsessed with styling it grunge-style with a…
```

**Try 5**

- stopped early: no
- selected_item: 90s Silk Slip Dress — Floral, Midi Length ($30.0, depop)
- search_results: 2

- parsed_by: regex — parsed: {'description': 'silk slip dress', 'size': 'M', 'max_price': 40.0}

- typical_price: None (sample_size 2)
- every search result rated: True (2 rated / 2 results)
- all labels valid: True

Labels (actual vs. 20% rule):

| id | title | price | deal | expected | match |
|---|---|---|---|---|---|
| lst_013 | 90s Silk Slip Dress — Floral, Midi Length | 30.0 | unknown | unknown | yes |
| lst_029 | Silk Button-Down — Sage Green | 28.0 | unknown | unknown | yes |

Comparables for 'silk slip dress' (2):

- 90s Silk Slip Dress — Floral, Midi Length — $30.0
- Silk Button-Down — Sage Green — $28.0

Outfit suggestion:

```
* **The 90s Grunge Contrast:** Layer your oversized grey crewneck sweatshirt right over the floral slip dress to turn it into a skirt. Pair with black combat boots and the black crossbody bag for a casual, textured look that balances the feminine print. 
* **The Streetwear Layer:** Wear the slip dress over your white ribbed tank top, and throw the black cropped zip hoodie on top, left unzipped to frame the neckline. Finish with chunky white sneakers for an effortless, sporty-vintage vibe.
```

Fit card:

```
Scored this gorgeous 90s floral silk slip dress for only $30.00 on Depop. Obsessed with styling it grunge-style with an oversized crewneck and chunky combat boots!
```

- Character count (including spaces): 163

Trace:

```
[1] parse_query
      in:  silk slip dress size M under $40
      out: dict with keys: description, size, max_price
      →    parsed by regex
[2] estimate_price
      in:  dict with keys: description, results
      out: dict with keys: typical_price, sample_size, rated
[3] select_item
      in:  2 results
      out: 90s Silk Slip Dress — Floral, Midi Length ($30.0, depop)
      →    selected first result
[4] suggest_outfit
      in:  dict with keys: item, wardrobe_items
      out: * **The 90s Grunge Contrast:** Layer your oversized grey crewneck sweatshirt right over the floral slip dress …
[5] create_fit_card
      in:  dict with keys: item, outfit
      out: Scored this gorgeous 90s floral silk slip dress for only $30.00 on Depop. Obsessed with styling it grunge-styl…
```

### every listing gets a label

- Query: `vintage graphic tee under $30`
- Wardrobe: example

**Try 1**

- stopped early: no
- selected_item: Y2K Baby Tee — Butterfly Print ($18.0, depop)
- search_results: 10

- parsed_by: model — parsed: {'description': 'vintage graphic tee', 'size': None, 'max_price': 30.0}

- typical_price: 27.0 (sample_size 31)
- every search result rated: True (10 rated / 10 results)
- all labels valid: True

Labels (actual vs. 20% rule):

| id | title | price | deal | expected | match |
|---|---|---|---|---|---|
| lst_002 | Y2K Baby Tee — Butterfly Print | 18.0 | good deal | good deal | yes |
| lst_006 | Graphic Tee — 2003 Tour Bootleg Style | 24.0 | fair | fair | yes |
| lst_033 | Vintage Band Tee — Faded Grey | 19.0 | good deal | good deal | yes |
| lst_015 | Vintage Graphic Hoodie — Faded Black | 26.0 | fair | fair | yes |
| lst_003 | Oversized Flannel Shirt — Plaid Red/Black | 22.0 | fair | fair | yes |
| lst_012 | Oversized Crewneck Sweatshirt — Vintage Navy | 20.0 | good deal | good deal | yes |
| lst_013 | 90s Silk Slip Dress — Floral, Midi Length | 30.0 | fair | fair | yes |
| lst_014 | Leather Belt — Brown, Braided | 12.0 | good deal | good deal | yes |
| lst_016 | High-Waisted Denim Shorts — Cutoff | 24.0 | fair | fair | yes |
| lst_017 | Mesh Long-Sleeve Top — Black | 15.0 | good deal | good deal | yes |

Comparables for 'vintage graphic tee' (31):

- Vintage Levi's 501 Jeans — Medium Wash — $38.0
- Y2K Baby Tee — Butterfly Print — $18.0
- Oversized Flannel Shirt — Plaid Red/Black — $22.0
- 90s Track Jacket — Navy/White Stripe — $45.0
- Corduroy Wide-Leg Pants — Rust — $32.0
- Graphic Tee — 2003 Tour Bootleg Style — $24.0
- Denim Jacket — Light Wash, Cropped — $42.0
- Vintage Windbreaker — Color Block Purple/Teal — $40.0
- Low-Rise Cargo Pants — Khaki — $27.0
- Oversized Crewneck Sweatshirt — Vintage Navy — $20.0
- 90s Silk Slip Dress — Floral, Midi Length — $30.0
- Leather Belt — Brown, Braided — $12.0
- Vintage Graphic Hoodie — Faded Black — $26.0
- High-Waisted Denim Shorts — Cutoff — $24.0
- Mesh Long-Sleeve Top — Black — $15.0
- Vintage Linen Blazer — Cream — $38.0
- Henley Long Sleeve — Washed Burgundy — $16.0
- Straight Leg Khaki Trousers — Olive — $29.0
- 90s Leather Bomber — Black — $75.0
- Vintage Polo Shirt — Forest Green — $18.0
- Oversized College Crewneck — Faded Red — $21.0
- Suede Chelsea Boots — Tan — $44.0
- Silk Button-Down — Sage Green — $28.0
- Vintage Knit Vest — Argyle Brown/Cream — $25.0
- Baggy Carpenter Jeans — Dark Wash — $36.0
- Vintage Band Tee — Faded Grey — $19.0
- Bucket Hat — Reversible, Brown Plaid — $14.0
- Velvet Blazer — Emerald Green — $52.0
- Straight Leg Black Jeans — Faded — $30.0
- Denim Vest — Medium Wash, Studded — $27.0
- Mini Shoulder Bag — Tan Leather — $38.0

Outfit suggestion:

```
* **Y2K Streetwear Contrast:** Pair the pink-and-purple butterfly baby tee with your baggy dark-wash straight-leg jeans to balance the cropped silhouette with a relaxed, low-key bottom. Layer the slightly cropped vintage black denim jacket on top, and finish the look with your chunky white sneakers and the black crossbody bag. 
* **Model-Off-Duty Casual:** Tuck the baby tee into your wide-leg khaki trousers, defined by the brown leather belt to pull in the earth tones. Throw your oversized grey crewneck sweatshirt over your shoulders or wear it open, and anchor the outfit with your chunky white sneakers for an effortless, texture-mixed everyday vibe.
```

Fit card:

```
Scored this pink and purple butterfly baby tee for $18 on Depop and I am obsessed. Styled it with baggy dark denim and chunky sneakers for the ultimate Y2K streetwear vibe.
```

- Character count (including spaces): 172

Trace:

```
[1] parse_query
      in:  vintage graphic tee under $30
      out: dict with keys: description, size, max_price
      →    parsed by model
[2] estimate_price
      in:  dict with keys: description, results
      out: dict with keys: typical_price, sample_size, rated
[3] select_item
      in:  10 results
      out: Y2K Baby Tee — Butterfly Print ($18.0, depop)
      →    selected first result
[4] suggest_outfit
      in:  dict with keys: item, wardrobe_items
      out: * **Y2K Streetwear Contrast:** Pair the pink-and-purple butterfly baby tee with your baggy dark-wash straight-…
[5] create_fit_card
      in:  dict with keys: item, outfit
      out: Scored this pink and purple butterfly baby tee for $18 on Depop and I am obsessed. Styled it with baggy dark d…
```

**Try 2**

- stopped early: no
- selected_item: Y2K Baby Tee — Butterfly Print ($18.0, depop)
- search_results: 10

- parsed_by: model — parsed: {'description': 'vintage graphic tee', 'size': None, 'max_price': 30.0}

- typical_price: 27.0 (sample_size 31)
- every search result rated: True (10 rated / 10 results)
- all labels valid: True

Labels (actual vs. 20% rule):

| id | title | price | deal | expected | match |
|---|---|---|---|---|---|
| lst_002 | Y2K Baby Tee — Butterfly Print | 18.0 | good deal | good deal | yes |
| lst_006 | Graphic Tee — 2003 Tour Bootleg Style | 24.0 | fair | fair | yes |
| lst_033 | Vintage Band Tee — Faded Grey | 19.0 | good deal | good deal | yes |
| lst_015 | Vintage Graphic Hoodie — Faded Black | 26.0 | fair | fair | yes |
| lst_003 | Oversized Flannel Shirt — Plaid Red/Black | 22.0 | fair | fair | yes |
| lst_012 | Oversized Crewneck Sweatshirt — Vintage Navy | 20.0 | good deal | good deal | yes |
| lst_013 | 90s Silk Slip Dress — Floral, Midi Length | 30.0 | fair | fair | yes |
| lst_014 | Leather Belt — Brown, Braided | 12.0 | good deal | good deal | yes |
| lst_016 | High-Waisted Denim Shorts — Cutoff | 24.0 | fair | fair | yes |
| lst_017 | Mesh Long-Sleeve Top — Black | 15.0 | good deal | good deal | yes |

Comparables for 'vintage graphic tee' (31):

- Vintage Levi's 501 Jeans — Medium Wash — $38.0
- Y2K Baby Tee — Butterfly Print — $18.0
- Oversized Flannel Shirt — Plaid Red/Black — $22.0
- 90s Track Jacket — Navy/White Stripe — $45.0
- Corduroy Wide-Leg Pants — Rust — $32.0
- Graphic Tee — 2003 Tour Bootleg Style — $24.0
- Denim Jacket — Light Wash, Cropped — $42.0
- Vintage Windbreaker — Color Block Purple/Teal — $40.0
- Low-Rise Cargo Pants — Khaki — $27.0
- Oversized Crewneck Sweatshirt — Vintage Navy — $20.0
- 90s Silk Slip Dress — Floral, Midi Length — $30.0
- Leather Belt — Brown, Braided — $12.0
- Vintage Graphic Hoodie — Faded Black — $26.0
- High-Waisted Denim Shorts — Cutoff — $24.0
- Mesh Long-Sleeve Top — Black — $15.0
- Vintage Linen Blazer — Cream — $38.0
- Henley Long Sleeve — Washed Burgundy — $16.0
- Straight Leg Khaki Trousers — Olive — $29.0
- 90s Leather Bomber — Black — $75.0
- Vintage Polo Shirt — Forest Green — $18.0
- Oversized College Crewneck — Faded Red — $21.0
- Suede Chelsea Boots — Tan — $44.0
- Silk Button-Down — Sage Green — $28.0
- Vintage Knit Vest — Argyle Brown/Cream — $25.0
- Baggy Carpenter Jeans — Dark Wash — $36.0
- Vintage Band Tee — Faded Grey — $19.0
- Bucket Hat — Reversible, Brown Plaid — $14.0
- Velvet Blazer — Emerald Green — $52.0
- Straight Leg Black Jeans — Faded — $30.0
- Denim Vest — Medium Wash, Studded — $27.0
- Mini Shoulder Bag — Tan Leather — $38.0

Outfit suggestion:

```
* **Y2K Streetwear Contrast:** Pair the pink-and-purple butterfly baby tee with your baggy dark-wash straight-leg jeans to balance the cropped silhouette with a relaxed, low-key bottom. Layer the slightly cropped vintage black denim jacket on top, and finish the look with your chunky white sneakers and the black crossbody bag. 
* **Model-Off-Duty Casual:** Tuck the baby tee into your wide-leg khaki trousers, defined by the brown leather belt to pull in the earth tones. Throw your oversized grey crewneck sweatshirt over your shoulders or wear it open, and anchor the outfit with your chunky white sneakers for an effortless, texture-mixed everyday vibe.
```

Fit card:

```
scored this absolute dream of a butterfly baby tee on depop for eighteen dollars. obsessed with styling it y2k streetwear style with baggy jeans and a denim jacket.
```

- Character count (including spaces): 164

Trace:

```
[1] parse_query
      in:  vintage graphic tee under $30
      out: dict with keys: description, size, max_price
      →    parsed by model
[2] estimate_price
      in:  dict with keys: description, results
      out: dict with keys: typical_price, sample_size, rated
[3] select_item
      in:  10 results
      out: Y2K Baby Tee — Butterfly Print ($18.0, depop)
      →    selected first result
[4] suggest_outfit
      in:  dict with keys: item, wardrobe_items
      out: * **Y2K Streetwear Contrast:** Pair the pink-and-purple butterfly baby tee with your baggy dark-wash straight-…
[5] create_fit_card
      in:  dict with keys: item, outfit
      out: scored this absolute dream of a butterfly baby tee on depop for eighteen dollars. obsessed with styling it y2k…
```

**Try 3**

- stopped early: no
- selected_item: Y2K Baby Tee — Butterfly Print ($18.0, depop)
- search_results: 10

- parsed_by: model — parsed: {'description': 'vintage graphic tee', 'size': None, 'max_price': 30.0}

- typical_price: 27.0 (sample_size 31)
- every search result rated: True (10 rated / 10 results)
- all labels valid: True

Labels (actual vs. 20% rule):

| id | title | price | deal | expected | match |
|---|---|---|---|---|---|
| lst_002 | Y2K Baby Tee — Butterfly Print | 18.0 | good deal | good deal | yes |
| lst_006 | Graphic Tee — 2003 Tour Bootleg Style | 24.0 | fair | fair | yes |
| lst_033 | Vintage Band Tee — Faded Grey | 19.0 | good deal | good deal | yes |
| lst_015 | Vintage Graphic Hoodie — Faded Black | 26.0 | fair | fair | yes |
| lst_003 | Oversized Flannel Shirt — Plaid Red/Black | 22.0 | fair | fair | yes |
| lst_012 | Oversized Crewneck Sweatshirt — Vintage Navy | 20.0 | good deal | good deal | yes |
| lst_013 | 90s Silk Slip Dress — Floral, Midi Length | 30.0 | fair | fair | yes |
| lst_014 | Leather Belt — Brown, Braided | 12.0 | good deal | good deal | yes |
| lst_016 | High-Waisted Denim Shorts — Cutoff | 24.0 | fair | fair | yes |
| lst_017 | Mesh Long-Sleeve Top — Black | 15.0 | good deal | good deal | yes |

Comparables for 'vintage graphic tee' (31):

- Vintage Levi's 501 Jeans — Medium Wash — $38.0
- Y2K Baby Tee — Butterfly Print — $18.0
- Oversized Flannel Shirt — Plaid Red/Black — $22.0
- 90s Track Jacket — Navy/White Stripe — $45.0
- Corduroy Wide-Leg Pants — Rust — $32.0
- Graphic Tee — 2003 Tour Bootleg Style — $24.0
- Denim Jacket — Light Wash, Cropped — $42.0
- Vintage Windbreaker — Color Block Purple/Teal — $40.0
- Low-Rise Cargo Pants — Khaki — $27.0
- Oversized Crewneck Sweatshirt — Vintage Navy — $20.0
- 90s Silk Slip Dress — Floral, Midi Length — $30.0
- Leather Belt — Brown, Braided — $12.0
- Vintage Graphic Hoodie — Faded Black — $26.0
- High-Waisted Denim Shorts — Cutoff — $24.0
- Mesh Long-Sleeve Top — Black — $15.0
- Vintage Linen Blazer — Cream — $38.0
- Henley Long Sleeve — Washed Burgundy — $16.0
- Straight Leg Khaki Trousers — Olive — $29.0
- 90s Leather Bomber — Black — $75.0
- Vintage Polo Shirt — Forest Green — $18.0
- Oversized College Crewneck — Faded Red — $21.0
- Suede Chelsea Boots — Tan — $44.0
- Silk Button-Down — Sage Green — $28.0
- Vintage Knit Vest — Argyle Brown/Cream — $25.0
- Baggy Carpenter Jeans — Dark Wash — $36.0
- Vintage Band Tee — Faded Grey — $19.0
- Bucket Hat — Reversible, Brown Plaid — $14.0
- Velvet Blazer — Emerald Green — $52.0
- Straight Leg Black Jeans — Faded — $30.0
- Denim Vest — Medium Wash, Studded — $27.0
- Mini Shoulder Bag — Tan Leather — $38.0

Outfit suggestion:

```
* **Y2K Streetwear Contrast:** Pair the pink-and-purple butterfly baby tee with your baggy dark-wash straight-leg jeans to balance the cropped silhouette with a relaxed, low-key bottom. Layer the slightly cropped vintage black denim jacket on top, and finish the look with your chunky white sneakers and the black crossbody bag. 
* **Model-Off-Duty Casual:** Tuck the baby tee into your wide-leg khaki trousers, defined by the brown leather belt to pull in the earth tones. Throw your oversized grey crewneck sweatshirt over your shoulders or wear it open, and anchor the outfit with your chunky white sneakers for an effortless, texture-mixed everyday vibe.
```

Fit card:

```
scored this cute y2k butterfly baby tee for $18 on depop and i’m obsessed. obsessed with how it looks paired with baggy dark jeans and chunky sneakers for an effortless street fit.
```

- Character count (including spaces): 180

Trace:

```
[1] parse_query
      in:  vintage graphic tee under $30
      out: dict with keys: description, size, max_price
      →    parsed by model
[2] estimate_price
      in:  dict with keys: description, results
      out: dict with keys: typical_price, sample_size, rated
[3] select_item
      in:  10 results
      out: Y2K Baby Tee — Butterfly Print ($18.0, depop)
      →    selected first result
[4] suggest_outfit
      in:  dict with keys: item, wardrobe_items
      out: * **Y2K Streetwear Contrast:** Pair the pink-and-purple butterfly baby tee with your baggy dark-wash straight-…
[5] create_fit_card
      in:  dict with keys: item, outfit
      out: scored this cute y2k butterfly baby tee for $18 on depop and i’m obsessed. obsessed with how it looks paired w…
```

**Try 4**

- stopped early: no
- selected_item: Y2K Baby Tee — Butterfly Print ($18.0, depop)
- search_results: 10

- parsed_by: model — parsed: {'description': 'vintage graphic tee', 'size': None, 'max_price': 30.0}

- typical_price: 27.0 (sample_size 31)
- every search result rated: True (10 rated / 10 results)
- all labels valid: True

Labels (actual vs. 20% rule):

| id | title | price | deal | expected | match |
|---|---|---|---|---|---|
| lst_002 | Y2K Baby Tee — Butterfly Print | 18.0 | good deal | good deal | yes |
| lst_006 | Graphic Tee — 2003 Tour Bootleg Style | 24.0 | fair | fair | yes |
| lst_033 | Vintage Band Tee — Faded Grey | 19.0 | good deal | good deal | yes |
| lst_015 | Vintage Graphic Hoodie — Faded Black | 26.0 | fair | fair | yes |
| lst_003 | Oversized Flannel Shirt — Plaid Red/Black | 22.0 | fair | fair | yes |
| lst_012 | Oversized Crewneck Sweatshirt — Vintage Navy | 20.0 | good deal | good deal | yes |
| lst_013 | 90s Silk Slip Dress — Floral, Midi Length | 30.0 | fair | fair | yes |
| lst_014 | Leather Belt — Brown, Braided | 12.0 | good deal | good deal | yes |
| lst_016 | High-Waisted Denim Shorts — Cutoff | 24.0 | fair | fair | yes |
| lst_017 | Mesh Long-Sleeve Top — Black | 15.0 | good deal | good deal | yes |

Comparables for 'vintage graphic tee' (31):

- Vintage Levi's 501 Jeans — Medium Wash — $38.0
- Y2K Baby Tee — Butterfly Print — $18.0
- Oversized Flannel Shirt — Plaid Red/Black — $22.0
- 90s Track Jacket — Navy/White Stripe — $45.0
- Corduroy Wide-Leg Pants — Rust — $32.0
- Graphic Tee — 2003 Tour Bootleg Style — $24.0
- Denim Jacket — Light Wash, Cropped — $42.0
- Vintage Windbreaker — Color Block Purple/Teal — $40.0
- Low-Rise Cargo Pants — Khaki — $27.0
- Oversized Crewneck Sweatshirt — Vintage Navy — $20.0
- 90s Silk Slip Dress — Floral, Midi Length — $30.0
- Leather Belt — Brown, Braided — $12.0
- Vintage Graphic Hoodie — Faded Black — $26.0
- High-Waisted Denim Shorts — Cutoff — $24.0
- Mesh Long-Sleeve Top — Black — $15.0
- Vintage Linen Blazer — Cream — $38.0
- Henley Long Sleeve — Washed Burgundy — $16.0
- Straight Leg Khaki Trousers — Olive — $29.0
- 90s Leather Bomber — Black — $75.0
- Vintage Polo Shirt — Forest Green — $18.0
- Oversized College Crewneck — Faded Red — $21.0
- Suede Chelsea Boots — Tan — $44.0
- Silk Button-Down — Sage Green — $28.0
- Vintage Knit Vest — Argyle Brown/Cream — $25.0
- Baggy Carpenter Jeans — Dark Wash — $36.0
- Vintage Band Tee — Faded Grey — $19.0
- Bucket Hat — Reversible, Brown Plaid — $14.0
- Velvet Blazer — Emerald Green — $52.0
- Straight Leg Black Jeans — Faded — $30.0
- Denim Vest — Medium Wash, Studded — $27.0
- Mini Shoulder Bag — Tan Leather — $38.0

Outfit suggestion:

```
* **Y2K Streetwear Contrast:** Pair the pink-and-purple butterfly baby tee with your baggy dark-wash straight-leg jeans to balance the cropped silhouette with a relaxed, low-key bottom. Layer the slightly cropped vintage black denim jacket on top, and finish the look with your chunky white sneakers and the black crossbody bag. 
* **Model-Off-Duty Casual:** Tuck the baby tee into your wide-leg khaki trousers, defined by the brown leather belt to pull in the earth tones. Throw your oversized grey crewneck sweatshirt over your shoulders or wear it open, and anchor the outfit with your chunky white sneakers for an effortless, texture-mixed everyday vibe.
```

Fit card:

```
Obsessed with this Y2K butterfly baby tee I just scored on Depop for $18! Styled it with baggy dark denim and chunky sneakers for the ultimate model-off-duty vibe.
```

- Character count (including spaces): 163

Trace:

```
[1] parse_query
      in:  vintage graphic tee under $30
      out: dict with keys: description, size, max_price
      →    parsed by model
[2] estimate_price
      in:  dict with keys: description, results
      out: dict with keys: typical_price, sample_size, rated
[3] select_item
      in:  10 results
      out: Y2K Baby Tee — Butterfly Print ($18.0, depop)
      →    selected first result
[4] suggest_outfit
      in:  dict with keys: item, wardrobe_items
      out: * **Y2K Streetwear Contrast:** Pair the pink-and-purple butterfly baby tee with your baggy dark-wash straight-…
[5] create_fit_card
      in:  dict with keys: item, outfit
      out: Obsessed with this Y2K butterfly baby tee I just scored on Depop for $18! Styled it with baggy dark denim and …
```

**Try 5**

- stopped early: no
- selected_item: Y2K Baby Tee — Butterfly Print ($18.0, depop)
- search_results: 10

- parsed_by: model — parsed: {'description': 'vintage graphic tee', 'size': None, 'max_price': 30.0}

- typical_price: 27.0 (sample_size 31)
- every search result rated: True (10 rated / 10 results)
- all labels valid: True

Labels (actual vs. 20% rule):

| id | title | price | deal | expected | match |
|---|---|---|---|---|---|
| lst_002 | Y2K Baby Tee — Butterfly Print | 18.0 | good deal | good deal | yes |
| lst_006 | Graphic Tee — 2003 Tour Bootleg Style | 24.0 | fair | fair | yes |
| lst_033 | Vintage Band Tee — Faded Grey | 19.0 | good deal | good deal | yes |
| lst_015 | Vintage Graphic Hoodie — Faded Black | 26.0 | fair | fair | yes |
| lst_003 | Oversized Flannel Shirt — Plaid Red/Black | 22.0 | fair | fair | yes |
| lst_012 | Oversized Crewneck Sweatshirt — Vintage Navy | 20.0 | good deal | good deal | yes |
| lst_013 | 90s Silk Slip Dress — Floral, Midi Length | 30.0 | fair | fair | yes |
| lst_014 | Leather Belt — Brown, Braided | 12.0 | good deal | good deal | yes |
| lst_016 | High-Waisted Denim Shorts — Cutoff | 24.0 | fair | fair | yes |
| lst_017 | Mesh Long-Sleeve Top — Black | 15.0 | good deal | good deal | yes |

Comparables for 'vintage graphic tee' (31):

- Vintage Levi's 501 Jeans — Medium Wash — $38.0
- Y2K Baby Tee — Butterfly Print — $18.0
- Oversized Flannel Shirt — Plaid Red/Black — $22.0
- 90s Track Jacket — Navy/White Stripe — $45.0
- Corduroy Wide-Leg Pants — Rust — $32.0
- Graphic Tee — 2003 Tour Bootleg Style — $24.0
- Denim Jacket — Light Wash, Cropped — $42.0
- Vintage Windbreaker — Color Block Purple/Teal — $40.0
- Low-Rise Cargo Pants — Khaki — $27.0
- Oversized Crewneck Sweatshirt — Vintage Navy — $20.0
- 90s Silk Slip Dress — Floral, Midi Length — $30.0
- Leather Belt — Brown, Braided — $12.0
- Vintage Graphic Hoodie — Faded Black — $26.0
- High-Waisted Denim Shorts — Cutoff — $24.0
- Mesh Long-Sleeve Top — Black — $15.0
- Vintage Linen Blazer — Cream — $38.0
- Henley Long Sleeve — Washed Burgundy — $16.0
- Straight Leg Khaki Trousers — Olive — $29.0
- 90s Leather Bomber — Black — $75.0
- Vintage Polo Shirt — Forest Green — $18.0
- Oversized College Crewneck — Faded Red — $21.0
- Suede Chelsea Boots — Tan — $44.0
- Silk Button-Down — Sage Green — $28.0
- Vintage Knit Vest — Argyle Brown/Cream — $25.0
- Baggy Carpenter Jeans — Dark Wash — $36.0
- Vintage Band Tee — Faded Grey — $19.0
- Bucket Hat — Reversible, Brown Plaid — $14.0
- Velvet Blazer — Emerald Green — $52.0
- Straight Leg Black Jeans — Faded — $30.0
- Denim Vest — Medium Wash, Studded — $27.0
- Mini Shoulder Bag — Tan Leather — $38.0

Outfit suggestion:

```
* **Y2K Streetwear Contrast:** Pair the pink-and-purple butterfly baby tee with your baggy dark-wash straight-leg jeans to balance the cropped silhouette with a relaxed, low-key bottom. Layer the slightly cropped vintage black denim jacket on top, and finish the look with your chunky white sneakers and the black crossbody bag. 
* **Model-Off-Duty Casual:** Tuck the baby tee into your wide-leg khaki trousers, defined by the brown leather belt to pull in the earth tones. Throw your oversized grey crewneck sweatshirt over your shoulders or wear it open, and anchor the outfit with your chunky white sneakers for an effortless, texture-mixed everyday vibe.
```

Fit card:

```
Found this adorable Y2K butterfly baby tee on Depop for just $18. Styled it with baggy dark denim and chunky sneakers for the ultimate model-off-duty streetwear look.
```

- Character count (including spaces): 166

Trace:

```
[1] parse_query
      in:  vintage graphic tee under $30
      out: dict with keys: description, size, max_price
      →    parsed by model
[2] estimate_price
      in:  dict with keys: description, results
      out: dict with keys: typical_price, sample_size, rated
[3] select_item
      in:  10 results
      out: Y2K Baby Tee — Butterfly Print ($18.0, depop)
      →    selected first result
[4] suggest_outfit
      in:  dict with keys: item, wardrobe_items
      out: * **Y2K Streetwear Contrast:** Pair the pink-and-purple butterfly baby tee with your baggy dark-wash straight-…
[5] create_fit_card
      in:  dict with keys: item, outfit
      out: Found this adorable Y2K butterfly baby tee on Depop for just $18. Styled it with baggy dark denim and chunky s…
```

### label matches the 20% rule

- Query: `black leather bomber jacket under $80`
- Wardrobe: example

**Try 1**

- stopped early: no
- selected_item: 90s Leather Bomber — Black ($75.0, depop)
- search_results: 10

- parsed_by: model — parsed: {'description': 'black leather bomber jacket', 'size': None, 'max_price': 80.0}

- typical_price: 31.5 (sample_size 14)
- every search result rated: True (10 rated / 10 results)
- all labels valid: True

Labels (actual vs. 20% rule):

| id | title | price | deal | expected | match |
|---|---|---|---|---|---|
| lst_022 | 90s Leather Bomber — Black | 75.0 | overpriced | overpriced | yes |
| lst_009 | Platform Mary Janes — Black Patent | 55.0 | overpriced | overpriced | yes |
| lst_003 | Oversized Flannel Shirt — Plaid Red/Black | 22.0 | good deal | good deal | yes |
| lst_004 | 90s Track Jacket — Navy/White Stripe | 45.0 | overpriced | overpriced | yes |
| lst_007 | Denim Jacket — Light Wash, Cropped | 42.0 | overpriced | overpriced | yes |
| lst_014 | Leather Belt — Brown, Braided | 12.0 | good deal | good deal | yes |
| lst_015 | Vintage Graphic Hoodie — Faded Black | 26.0 | fair | fair | yes |
| lst_017 | Mesh Long-Sleeve Top — Black | 15.0 | good deal | good deal | yes |
| lst_026 | Biker Shorts — Black, Shiny | 14.0 | good deal | good deal | yes |
| lst_037 | Straight Leg Black Jeans — Faded | 30.0 | fair | fair | yes |

Comparables for 'black leather bomber jacket' (14):

- Oversized Flannel Shirt — Plaid Red/Black — $22.0
- 90s Track Jacket — Navy/White Stripe — $45.0
- Graphic Tee — 2003 Tour Bootleg Style — $24.0
- Denim Jacket — Light Wash, Cropped — $42.0
- Platform Mary Janes — Black Patent — $55.0
- Vintage Windbreaker — Color Block Purple/Teal — $40.0
- Leather Belt — Brown, Braided — $12.0
- Vintage Graphic Hoodie — Faded Black — $26.0
- Mesh Long-Sleeve Top — Black — $15.0
- 90s Leather Bomber — Black — $75.0
- Biker Shorts — Black, Shiny — $14.0
- Shacket — Olive Canvas — $33.0
- Straight Leg Black Jeans — Faded — $30.0
- Mini Shoulder Bag — Tan Leather — $38.0

Outfit suggestion:

```
* **Look 1 (90s Off-Duty Model):** Layer your white ribbed tank top tucked into the baggy straight-leg jeans (add the brown leather belt for contrast), and throw the black leather bomber on top. Finish with the chunky white sneakers and the black crossbody bag for an effortless, boxy-meets-fitted silhouette. 
* **Look 2 (Grunge Streetwear):** Wear the black cropped zip hoodie underneath the black leather bomber so the hood lays flat over the collar. Pair with the baggy straight-leg jeans and black combat boots for a monochrome texture-play that leans into the jacket's vintage grunge roots.
```

Fit card:

```
scored this 90s leather bomber on depop for $75 and it’s officially my entire personality. obsessed with throwing it over a baggy hoodie and combat boots for that grungy, lived-in look.
```

- Character count (including spaces): 185

Trace:

```
[1] parse_query
      in:  black leather bomber jacket under $80
      out: dict with keys: description, size, max_price
      →    parsed by model
[2] estimate_price
      in:  dict with keys: description, results
      out: dict with keys: typical_price, sample_size, rated
[3] select_item
      in:  10 results
      out: 90s Leather Bomber — Black ($75.0, depop)
      →    selected first result
[4] suggest_outfit
      in:  dict with keys: item, wardrobe_items
      out: * **Look 1 (90s Off-Duty Model):** Layer your white ribbed tank top tucked into the baggy straight-leg jeans (…
[5] create_fit_card
      in:  dict with keys: item, outfit
      out: scored this 90s leather bomber on depop for $75 and it’s officially my entire personality. obsessed with throw…
```

**Try 2**

- stopped early: no
- selected_item: 90s Leather Bomber — Black ($75.0, depop)
- search_results: 10

- parsed_by: model — parsed: {'description': 'black leather bomber jacket', 'size': None, 'max_price': 80.0}

- typical_price: 31.5 (sample_size 14)
- every search result rated: True (10 rated / 10 results)
- all labels valid: True

Labels (actual vs. 20% rule):

| id | title | price | deal | expected | match |
|---|---|---|---|---|---|
| lst_022 | 90s Leather Bomber — Black | 75.0 | overpriced | overpriced | yes |
| lst_009 | Platform Mary Janes — Black Patent | 55.0 | overpriced | overpriced | yes |
| lst_003 | Oversized Flannel Shirt — Plaid Red/Black | 22.0 | good deal | good deal | yes |
| lst_004 | 90s Track Jacket — Navy/White Stripe | 45.0 | overpriced | overpriced | yes |
| lst_007 | Denim Jacket — Light Wash, Cropped | 42.0 | overpriced | overpriced | yes |
| lst_014 | Leather Belt — Brown, Braided | 12.0 | good deal | good deal | yes |
| lst_015 | Vintage Graphic Hoodie — Faded Black | 26.0 | fair | fair | yes |
| lst_017 | Mesh Long-Sleeve Top — Black | 15.0 | good deal | good deal | yes |
| lst_026 | Biker Shorts — Black, Shiny | 14.0 | good deal | good deal | yes |
| lst_037 | Straight Leg Black Jeans — Faded | 30.0 | fair | fair | yes |

Comparables for 'black leather bomber jacket' (14):

- Oversized Flannel Shirt — Plaid Red/Black — $22.0
- 90s Track Jacket — Navy/White Stripe — $45.0
- Graphic Tee — 2003 Tour Bootleg Style — $24.0
- Denim Jacket — Light Wash, Cropped — $42.0
- Platform Mary Janes — Black Patent — $55.0
- Vintage Windbreaker — Color Block Purple/Teal — $40.0
- Leather Belt — Brown, Braided — $12.0
- Vintage Graphic Hoodie — Faded Black — $26.0
- Mesh Long-Sleeve Top — Black — $15.0
- 90s Leather Bomber — Black — $75.0
- Biker Shorts — Black, Shiny — $14.0
- Shacket — Olive Canvas — $33.0
- Straight Leg Black Jeans — Faded — $30.0
- Mini Shoulder Bag — Tan Leather — $38.0

Outfit suggestion:

```
* **Look 1 (90s Off-Duty Model):** Layer your white ribbed tank top tucked into the baggy straight-leg jeans (add the brown leather belt for contrast), and throw the black leather bomber on top. Finish with the chunky white sneakers and the black crossbody bag for an effortless, boxy-meets-fitted silhouette. 
* **Look 2 (Grunge Streetwear):** Wear the black cropped zip hoodie underneath the black leather bomber so the hood lays flat over the collar. Pair with the baggy straight-leg jeans and black combat boots for a monochrome texture-play that leans into the jacket's vintage grunge roots.
```

Fit card:

```
scored this insanely good 90s leather bomber on depop for $75 and honestly haven’t taken it off since. obsessed with throwing it over a hoodie and combat boots for total grunge energy.
```

- Character count (including spaces): 184

Trace:

```
[1] parse_query
      in:  black leather bomber jacket under $80
      out: dict with keys: description, size, max_price
      →    parsed by model
[2] estimate_price
      in:  dict with keys: description, results
      out: dict with keys: typical_price, sample_size, rated
[3] select_item
      in:  10 results
      out: 90s Leather Bomber — Black ($75.0, depop)
      →    selected first result
[4] suggest_outfit
      in:  dict with keys: item, wardrobe_items
      out: * **Look 1 (90s Off-Duty Model):** Layer your white ribbed tank top tucked into the baggy straight-leg jeans (…
[5] create_fit_card
      in:  dict with keys: item, outfit
      out: scored this insanely good 90s leather bomber on depop for $75 and honestly haven’t taken it off since. obsesse…
```

**Try 3**

- stopped early: no
- selected_item: 90s Leather Bomber — Black ($75.0, depop)
- search_results: 10

- parsed_by: model — parsed: {'description': 'black leather bomber jacket', 'size': None, 'max_price': 80.0}

- typical_price: 31.5 (sample_size 14)
- every search result rated: True (10 rated / 10 results)
- all labels valid: True

Labels (actual vs. 20% rule):

| id | title | price | deal | expected | match |
|---|---|---|---|---|---|
| lst_022 | 90s Leather Bomber — Black | 75.0 | overpriced | overpriced | yes |
| lst_009 | Platform Mary Janes — Black Patent | 55.0 | overpriced | overpriced | yes |
| lst_003 | Oversized Flannel Shirt — Plaid Red/Black | 22.0 | good deal | good deal | yes |
| lst_004 | 90s Track Jacket — Navy/White Stripe | 45.0 | overpriced | overpriced | yes |
| lst_007 | Denim Jacket — Light Wash, Cropped | 42.0 | overpriced | overpriced | yes |
| lst_014 | Leather Belt — Brown, Braided | 12.0 | good deal | good deal | yes |
| lst_015 | Vintage Graphic Hoodie — Faded Black | 26.0 | fair | fair | yes |
| lst_017 | Mesh Long-Sleeve Top — Black | 15.0 | good deal | good deal | yes |
| lst_026 | Biker Shorts — Black, Shiny | 14.0 | good deal | good deal | yes |
| lst_037 | Straight Leg Black Jeans — Faded | 30.0 | fair | fair | yes |

Comparables for 'black leather bomber jacket' (14):

- Oversized Flannel Shirt — Plaid Red/Black — $22.0
- 90s Track Jacket — Navy/White Stripe — $45.0
- Graphic Tee — 2003 Tour Bootleg Style — $24.0
- Denim Jacket — Light Wash, Cropped — $42.0
- Platform Mary Janes — Black Patent — $55.0
- Vintage Windbreaker — Color Block Purple/Teal — $40.0
- Leather Belt — Brown, Braided — $12.0
- Vintage Graphic Hoodie — Faded Black — $26.0
- Mesh Long-Sleeve Top — Black — $15.0
- 90s Leather Bomber — Black — $75.0
- Biker Shorts — Black, Shiny — $14.0
- Shacket — Olive Canvas — $33.0
- Straight Leg Black Jeans — Faded — $30.0
- Mini Shoulder Bag — Tan Leather — $38.0

Outfit suggestion:

```
* **Look 1 (90s Off-Duty Model):** Layer your white ribbed tank top tucked into the baggy straight-leg jeans (add the brown leather belt for contrast), and throw the black leather bomber on top. Finish with the chunky white sneakers and the black crossbody bag for an effortless, boxy-meets-fitted silhouette. 
* **Look 2 (Grunge Streetwear):** Wear the black cropped zip hoodie underneath the black leather bomber so the hood lays flat over the collar. Pair with the baggy straight-leg jeans and black combat boots for a monochrome texture-play that leans into the jacket's vintage grunge roots.
```

Fit card:

```
scored this 90s leather bomber on depop for $75 and honestly haven't taken it off since. obsessed with styling it over a baggy hoodie for that effortless grunge look.
```

- Character count (including spaces): 166

Trace:

```
[1] parse_query
      in:  black leather bomber jacket under $80
      out: dict with keys: description, size, max_price
      →    parsed by model
[2] estimate_price
      in:  dict with keys: description, results
      out: dict with keys: typical_price, sample_size, rated
[3] select_item
      in:  10 results
      out: 90s Leather Bomber — Black ($75.0, depop)
      →    selected first result
[4] suggest_outfit
      in:  dict with keys: item, wardrobe_items
      out: * **Look 1 (90s Off-Duty Model):** Layer your white ribbed tank top tucked into the baggy straight-leg jeans (…
[5] create_fit_card
      in:  dict with keys: item, outfit
      out: scored this 90s leather bomber on depop for $75 and honestly haven't taken it off since. obsessed with styling…
```

**Try 4**

- stopped early: no
- selected_item: 90s Leather Bomber — Black ($75.0, depop)
- search_results: 10

- parsed_by: model — parsed: {'description': 'black leather bomber jacket', 'size': None, 'max_price': 80.0}

- typical_price: 31.5 (sample_size 14)
- every search result rated: True (10 rated / 10 results)
- all labels valid: True

Labels (actual vs. 20% rule):

| id | title | price | deal | expected | match |
|---|---|---|---|---|---|
| lst_022 | 90s Leather Bomber — Black | 75.0 | overpriced | overpriced | yes |
| lst_009 | Platform Mary Janes — Black Patent | 55.0 | overpriced | overpriced | yes |
| lst_003 | Oversized Flannel Shirt — Plaid Red/Black | 22.0 | good deal | good deal | yes |
| lst_004 | 90s Track Jacket — Navy/White Stripe | 45.0 | overpriced | overpriced | yes |
| lst_007 | Denim Jacket — Light Wash, Cropped | 42.0 | overpriced | overpriced | yes |
| lst_014 | Leather Belt — Brown, Braided | 12.0 | good deal | good deal | yes |
| lst_015 | Vintage Graphic Hoodie — Faded Black | 26.0 | fair | fair | yes |
| lst_017 | Mesh Long-Sleeve Top — Black | 15.0 | good deal | good deal | yes |
| lst_026 | Biker Shorts — Black, Shiny | 14.0 | good deal | good deal | yes |
| lst_037 | Straight Leg Black Jeans — Faded | 30.0 | fair | fair | yes |

Comparables for 'black leather bomber jacket' (14):

- Oversized Flannel Shirt — Plaid Red/Black — $22.0
- 90s Track Jacket — Navy/White Stripe — $45.0
- Graphic Tee — 2003 Tour Bootleg Style — $24.0
- Denim Jacket — Light Wash, Cropped — $42.0
- Platform Mary Janes — Black Patent — $55.0
- Vintage Windbreaker — Color Block Purple/Teal — $40.0
- Leather Belt — Brown, Braided — $12.0
- Vintage Graphic Hoodie — Faded Black — $26.0
- Mesh Long-Sleeve Top — Black — $15.0
- 90s Leather Bomber — Black — $75.0
- Biker Shorts — Black, Shiny — $14.0
- Shacket — Olive Canvas — $33.0
- Straight Leg Black Jeans — Faded — $30.0
- Mini Shoulder Bag — Tan Leather — $38.0

Outfit suggestion:

```
* **Look 1 (90s Off-Duty Model):** Layer your white ribbed tank top tucked into the baggy straight-leg jeans (add the brown leather belt for contrast), and throw the black leather bomber on top. Finish with the chunky white sneakers and the black crossbody bag for an effortless, boxy-meets-fitted silhouette. 
* **Look 2 (Grunge Streetwear):** Wear the black cropped zip hoodie underneath the black leather bomber so the hood lays flat over the collar. Pair with the baggy straight-leg jeans and black combat boots for a monochrome texture-play that leans into the jacket's vintage grunge roots.
```

Fit card:

```
scored this 90s leather bomber on depop for $75 and honestly haven't taken it off since. obsessed with styling it over a baggy hoodie for that effortless grunge look.
```

- Character count (including spaces): 166

Trace:

```
[1] parse_query
      in:  black leather bomber jacket under $80
      out: dict with keys: description, size, max_price
      →    parsed by model
[2] estimate_price
      in:  dict with keys: description, results
      out: dict with keys: typical_price, sample_size, rated
[3] select_item
      in:  10 results
      out: 90s Leather Bomber — Black ($75.0, depop)
      →    selected first result
[4] suggest_outfit
      in:  dict with keys: item, wardrobe_items
      out: * **Look 1 (90s Off-Duty Model):** Layer your white ribbed tank top tucked into the baggy straight-leg jeans (…
[5] create_fit_card
      in:  dict with keys: item, outfit
      out: scored this 90s leather bomber on depop for $75 and honestly haven't taken it off since. obsessed with styling…
```

**Try 5**

- stopped early: no
- selected_item: 90s Leather Bomber — Black ($75.0, depop)
- search_results: 10

- parsed_by: model — parsed: {'description': 'black leather bomber jacket', 'size': None, 'max_price': 80.0}

- typical_price: 31.5 (sample_size 14)
- every search result rated: True (10 rated / 10 results)
- all labels valid: True

Labels (actual vs. 20% rule):

| id | title | price | deal | expected | match |
|---|---|---|---|---|---|
| lst_022 | 90s Leather Bomber — Black | 75.0 | overpriced | overpriced | yes |
| lst_009 | Platform Mary Janes — Black Patent | 55.0 | overpriced | overpriced | yes |
| lst_003 | Oversized Flannel Shirt — Plaid Red/Black | 22.0 | good deal | good deal | yes |
| lst_004 | 90s Track Jacket — Navy/White Stripe | 45.0 | overpriced | overpriced | yes |
| lst_007 | Denim Jacket — Light Wash, Cropped | 42.0 | overpriced | overpriced | yes |
| lst_014 | Leather Belt — Brown, Braided | 12.0 | good deal | good deal | yes |
| lst_015 | Vintage Graphic Hoodie — Faded Black | 26.0 | fair | fair | yes |
| lst_017 | Mesh Long-Sleeve Top — Black | 15.0 | good deal | good deal | yes |
| lst_026 | Biker Shorts — Black, Shiny | 14.0 | good deal | good deal | yes |
| lst_037 | Straight Leg Black Jeans — Faded | 30.0 | fair | fair | yes |

Comparables for 'black leather bomber jacket' (14):

- Oversized Flannel Shirt — Plaid Red/Black — $22.0
- 90s Track Jacket — Navy/White Stripe — $45.0
- Graphic Tee — 2003 Tour Bootleg Style — $24.0
- Denim Jacket — Light Wash, Cropped — $42.0
- Platform Mary Janes — Black Patent — $55.0
- Vintage Windbreaker — Color Block Purple/Teal — $40.0
- Leather Belt — Brown, Braided — $12.0
- Vintage Graphic Hoodie — Faded Black — $26.0
- Mesh Long-Sleeve Top — Black — $15.0
- 90s Leather Bomber — Black — $75.0
- Biker Shorts — Black, Shiny — $14.0
- Shacket — Olive Canvas — $33.0
- Straight Leg Black Jeans — Faded — $30.0
- Mini Shoulder Bag — Tan Leather — $38.0

Outfit suggestion:

```
* **Look 1 (90s Off-Duty Model):** Layer your white ribbed tank top tucked into the baggy straight-leg jeans (add the brown leather belt for contrast), and throw the black leather bomber on top. Finish with the chunky white sneakers and the black crossbody bag for an effortless, boxy-meets-fitted silhouette. 
* **Look 2 (Grunge Streetwear):** Wear the black cropped zip hoodie underneath the black leather bomber so the hood lays flat over the collar. Pair with the baggy straight-leg jeans and black combat boots for a monochrome texture-play that leans into the jacket's vintage grunge roots.
```

Fit card:

```
Found my dream 90s leather bomber on depop for $75! Obsessed with the worn-in creases. Styled it with a hoodie and combat boots for total grunge energy.
```

- Character count (including spaces): 152

Trace:

```
[1] parse_query
      in:  black leather bomber jacket under $80
      out: dict with keys: description, size, max_price
      →    parsed by model
[2] estimate_price
      in:  dict with keys: description, results
      out: dict with keys: typical_price, sample_size, rated
[3] select_item
      in:  10 results
      out: 90s Leather Bomber — Black ($75.0, depop)
      →    selected first result
[4] suggest_outfit
      in:  dict with keys: item, wardrobe_items
      out: * **Look 1 (90s Off-Duty Model):** Layer your white ribbed tank top tucked into the baggy straight-leg jeans (…
[5] create_fit_card
      in:  dict with keys: item, outfit
      out: Found my dream 90s leather bomber on depop for $75! Obsessed with the worn-in creases. Styled it with a hoodie…
```

### too few comparables -> all unknown

- Query: `corduroy pants under $100`
- Wardrobe: example

**Try 1**

- stopped early: no
- selected_item: Corduroy Wide-Leg Pants — Rust ($32.0, depop)
- search_results: 2

- parsed_by: model — parsed: {'description': 'corduroy pants', 'size': None, 'max_price': 100.0}

- typical_price: None (sample_size 2)
- every search result rated: True (2 rated / 2 results)
- all labels valid: True

Labels (actual vs. 20% rule):

| id | title | price | deal | expected | match |
|---|---|---|---|---|---|
| lst_005 | Corduroy Wide-Leg Pants — Rust | 32.0 | unknown | unknown | yes |
| lst_011 | Low-Rise Cargo Pants — Khaki | 27.0 | unknown | unknown | yes |

Comparables for 'corduroy pants' (2):

- Corduroy Wide-Leg Pants — Rust — $32.0
- Low-Rise Cargo Pants — Khaki — $27.0

Outfit suggestion:

```
* Tuck your **white ribbed tank top** into the high-waisted rust cords, add the **brown leather belt**, and layer the **vintage black denim jacket** on top. Finish the look with **black combat boots** and the **black crossbody bag** for an easy 70s-meets-grunge vibe. 

* Lean into the cozy earth tones by pairing the rust cords with the **oversized grey crewneck sweatshirt** worn slouchy and untucked, accented by the **brown leather belt** peeking out from underneath if tucked loosely in front. Slip on the **chunky white sneakers** and wear the **black crossbody bag** for a comfortable, textured everyday outfit.
```

Fit card:

```
scored these vintage rust cords on depop for $32 and they are so good. obsessed with styling them slouchy with a big grey crewneck for the ultimate cozy fall fit.
```

- Character count (including spaces): 162

Trace:

```
[1] parse_query
      in:  corduroy pants under $100
      out: dict with keys: description, size, max_price
      →    parsed by model
[2] estimate_price
      in:  dict with keys: description, results
      out: dict with keys: typical_price, sample_size, rated
[3] select_item
      in:  2 results
      out: Corduroy Wide-Leg Pants — Rust ($32.0, depop)
      →    selected first result
[4] suggest_outfit
      in:  dict with keys: item, wardrobe_items
      out: * Tuck your **white ribbed tank top** into the high-waisted rust cords, add the **brown leather belt**, and la…
[5] create_fit_card
      in:  dict with keys: item, outfit
      out: scored these vintage rust cords on depop for $32 and they are so good. obsessed with styling them slouchy with…
```

**Try 2**

- stopped early: no
- selected_item: Corduroy Wide-Leg Pants — Rust ($32.0, depop)
- search_results: 2

- parsed_by: model — parsed: {'description': 'corduroy pants', 'size': None, 'max_price': 100.0}

- typical_price: None (sample_size 2)
- every search result rated: True (2 rated / 2 results)
- all labels valid: True

Labels (actual vs. 20% rule):

| id | title | price | deal | expected | match |
|---|---|---|---|---|---|
| lst_005 | Corduroy Wide-Leg Pants — Rust | 32.0 | unknown | unknown | yes |
| lst_011 | Low-Rise Cargo Pants — Khaki | 27.0 | unknown | unknown | yes |

Comparables for 'corduroy pants' (2):

- Corduroy Wide-Leg Pants — Rust — $32.0
- Low-Rise Cargo Pants — Khaki — $27.0

Outfit suggestion:

```
* Tuck your **white ribbed tank top** into the high-waisted rust cords, add the **brown leather belt**, and layer the **vintage black denim jacket** on top. Finish the look with **black combat boots** and the **black crossbody bag** for an easy 70s-meets-grunge vibe. 

* Lean into the cozy earth tones by pairing the rust cords with the **oversized grey crewneck sweatshirt** worn slouchy and untucked, accented by the **brown leather belt** peeking out from underneath if tucked loosely in front. Slip on the **chunky white sneakers** and wear the **black crossbody bag** for a comfortable, textured everyday outfit.
```

Fit card:

```
Scored these vintage rust cords on Depop for $32 and I'm obsessed. Paired them with a white tank, black denim, and combat boots for a 70s grunge moment.
```

- Character count (including spaces): 152

Trace:

```
[1] parse_query
      in:  corduroy pants under $100
      out: dict with keys: description, size, max_price
      →    parsed by model
[2] estimate_price
      in:  dict with keys: description, results
      out: dict with keys: typical_price, sample_size, rated
[3] select_item
      in:  2 results
      out: Corduroy Wide-Leg Pants — Rust ($32.0, depop)
      →    selected first result
[4] suggest_outfit
      in:  dict with keys: item, wardrobe_items
      out: * Tuck your **white ribbed tank top** into the high-waisted rust cords, add the **brown leather belt**, and la…
[5] create_fit_card
      in:  dict with keys: item, outfit
      out: Scored these vintage rust cords on Depop for $32 and I'm obsessed. Paired them with a white tank, black denim,…
```

**Try 3**

- stopped early: no
- selected_item: Corduroy Wide-Leg Pants — Rust ($32.0, depop)
- search_results: 2

- parsed_by: model — parsed: {'description': 'corduroy pants', 'size': None, 'max_price': 100.0}

- typical_price: None (sample_size 2)
- every search result rated: True (2 rated / 2 results)
- all labels valid: True

Labels (actual vs. 20% rule):

| id | title | price | deal | expected | match |
|---|---|---|---|---|---|
| lst_005 | Corduroy Wide-Leg Pants — Rust | 32.0 | unknown | unknown | yes |
| lst_011 | Low-Rise Cargo Pants — Khaki | 27.0 | unknown | unknown | yes |

Comparables for 'corduroy pants' (2):

- Corduroy Wide-Leg Pants — Rust — $32.0
- Low-Rise Cargo Pants — Khaki — $27.0

Outfit suggestion:

```
* Tuck your **white ribbed tank top** into the high-waisted rust cords, add the **brown leather belt**, and layer the **vintage black denim jacket** on top. Finish the look with **black combat boots** and the **black crossbody bag** for an easy 70s-meets-grunge vibe. 

* Lean into the cozy earth tones by pairing the rust cords with the **oversized grey crewneck sweatshirt** worn slouchy and untucked, accented by the **brown leather belt** peeking out from underneath if tucked loosely in front. Slip on the **chunky white sneakers** and wear the **black crossbody bag** for a comfortable, textured everyday outfit.
```

Fit card:

```
Scored these rust cords on Depop for $32 and I am obsessed. Wore them with a chunky crewneck and sneakers for the coziest 70s grunge vibe.
```

- Character count (including spaces): 138

Trace:

```
[1] parse_query
      in:  corduroy pants under $100
      out: dict with keys: description, size, max_price
      →    parsed by model
[2] estimate_price
      in:  dict with keys: description, results
      out: dict with keys: typical_price, sample_size, rated
[3] select_item
      in:  2 results
      out: Corduroy Wide-Leg Pants — Rust ($32.0, depop)
      →    selected first result
[4] suggest_outfit
      in:  dict with keys: item, wardrobe_items
      out: * Tuck your **white ribbed tank top** into the high-waisted rust cords, add the **brown leather belt**, and la…
[5] create_fit_card
      in:  dict with keys: item, outfit
      out: Scored these rust cords on Depop for $32 and I am obsessed. Wore them with a chunky crewneck and sneakers for …
```

**Try 4**

- stopped early: no
- selected_item: Corduroy Wide-Leg Pants — Rust ($32.0, depop)
- search_results: 2

- parsed_by: model — parsed: {'description': 'corduroy pants', 'size': None, 'max_price': 100.0}

- typical_price: None (sample_size 2)
- every search result rated: True (2 rated / 2 results)
- all labels valid: True

Labels (actual vs. 20% rule):

| id | title | price | deal | expected | match |
|---|---|---|---|---|---|
| lst_005 | Corduroy Wide-Leg Pants — Rust | 32.0 | unknown | unknown | yes |
| lst_011 | Low-Rise Cargo Pants — Khaki | 27.0 | unknown | unknown | yes |

Comparables for 'corduroy pants' (2):

- Corduroy Wide-Leg Pants — Rust — $32.0
- Low-Rise Cargo Pants — Khaki — $27.0

Outfit suggestion:

```
* Tuck your **white ribbed tank top** into the high-waisted rust cords, add the **brown leather belt**, and layer the **vintage black denim jacket** on top. Finish the look with **black combat boots** and the **black crossbody bag** for an easy 70s-meets-grunge vibe. 

* Lean into the cozy earth tones by pairing the rust cords with the **oversized grey crewneck sweatshirt** worn slouchy and untucked, accented by the **brown leather belt** peeking out from underneath if tucked loosely in front. Slip on the **chunky white sneakers** and wear the **black crossbody bag** for a comfortable, textured everyday outfit.
```

Fit card:

```
scored these dreamy rust cords on depop for $32 and i am obsessed. giving major 70s grunge with my black denim jacket and combat boots, or total cozy vibes with an oversized crewneck.
```

- Character count (including spaces): 183

Trace:

```
[1] parse_query
      in:  corduroy pants under $100
      out: dict with keys: description, size, max_price
      →    parsed by model
[2] estimate_price
      in:  dict with keys: description, results
      out: dict with keys: typical_price, sample_size, rated
[3] select_item
      in:  2 results
      out: Corduroy Wide-Leg Pants — Rust ($32.0, depop)
      →    selected first result
[4] suggest_outfit
      in:  dict with keys: item, wardrobe_items
      out: * Tuck your **white ribbed tank top** into the high-waisted rust cords, add the **brown leather belt**, and la…
[5] create_fit_card
      in:  dict with keys: item, outfit
      out: scored these dreamy rust cords on depop for $32 and i am obsessed. giving major 70s grunge with my black denim…
```

**Try 5**

- stopped early: no
- selected_item: Corduroy Wide-Leg Pants — Rust ($32.0, depop)
- search_results: 2

- parsed_by: model — parsed: {'description': 'corduroy pants', 'size': None, 'max_price': 100.0}

- typical_price: None (sample_size 2)
- every search result rated: True (2 rated / 2 results)
- all labels valid: True

Labels (actual vs. 20% rule):

| id | title | price | deal | expected | match |
|---|---|---|---|---|---|
| lst_005 | Corduroy Wide-Leg Pants — Rust | 32.0 | unknown | unknown | yes |
| lst_011 | Low-Rise Cargo Pants — Khaki | 27.0 | unknown | unknown | yes |

Comparables for 'corduroy pants' (2):

- Corduroy Wide-Leg Pants — Rust — $32.0
- Low-Rise Cargo Pants — Khaki — $27.0

Outfit suggestion:

```
* Tuck your **white ribbed tank top** into the high-waisted rust cords, add the **brown leather belt**, and layer the **vintage black denim jacket** on top. Finish the look with **black combat boots** and the **black crossbody bag** for an easy 70s-meets-grunge vibe. 

* Lean into the cozy earth tones by pairing the rust cords with the **oversized grey crewneck sweatshirt** worn slouchy and untucked, accented by the **brown leather belt** peeking out from underneath if tucked loosely in front. Slip on the **chunky white sneakers** and wear the **black crossbody bag** for a comfortable, textured everyday outfit.
```

Fit card:

```
Snagged these rust wide-leg cords on Depop for $32 and they are so good. Paired them with a vintage denim jacket and combat boots for that 70s grunge feel.
```

- Character count (including spaces): 155

Trace:

```
[1] parse_query
      in:  corduroy pants under $100
      out: dict with keys: description, size, max_price
      →    parsed by model
[2] estimate_price
      in:  dict with keys: description, results
      out: dict with keys: typical_price, sample_size, rated
[3] select_item
      in:  2 results
      out: Corduroy Wide-Leg Pants — Rust ($32.0, depop)
      →    selected first result
[4] suggest_outfit
      in:  dict with keys: item, wardrobe_items
      out: * Tuck your **white ribbed tank top** into the high-waisted rust cords, add the **brown leather belt**, and la…
[5] create_fit_card
      in:  dict with keys: item, outfit
      out: Snagged these rust wide-leg cords on Depop for $32 and they are so good. Paired them with a vintage denim jack…
```

### comparables are the same category

- Query: `vintage graphic tee under $30`
- Wardrobe: example

**Try 1**

- stopped early: no
- selected_item: Y2K Baby Tee — Butterfly Print ($18.0, depop)
- search_results: 10

- parsed_by: model — parsed: {'description': 'vintage graphic tee', 'size': None, 'max_price': 30.0}

- typical_price: 27.0 (sample_size 31)
- every search result rated: True (10 rated / 10 results)
- all labels valid: True

Labels (actual vs. 20% rule):

| id | title | price | deal | expected | match |
|---|---|---|---|---|---|
| lst_002 | Y2K Baby Tee — Butterfly Print | 18.0 | good deal | good deal | yes |
| lst_006 | Graphic Tee — 2003 Tour Bootleg Style | 24.0 | fair | fair | yes |
| lst_033 | Vintage Band Tee — Faded Grey | 19.0 | good deal | good deal | yes |
| lst_015 | Vintage Graphic Hoodie — Faded Black | 26.0 | fair | fair | yes |
| lst_003 | Oversized Flannel Shirt — Plaid Red/Black | 22.0 | fair | fair | yes |
| lst_012 | Oversized Crewneck Sweatshirt — Vintage Navy | 20.0 | good deal | good deal | yes |
| lst_013 | 90s Silk Slip Dress — Floral, Midi Length | 30.0 | fair | fair | yes |
| lst_014 | Leather Belt — Brown, Braided | 12.0 | good deal | good deal | yes |
| lst_016 | High-Waisted Denim Shorts — Cutoff | 24.0 | fair | fair | yes |
| lst_017 | Mesh Long-Sleeve Top — Black | 15.0 | good deal | good deal | yes |

Comparables for 'vintage graphic tee' (31):

- Vintage Levi's 501 Jeans — Medium Wash — $38.0
- Y2K Baby Tee — Butterfly Print — $18.0
- Oversized Flannel Shirt — Plaid Red/Black — $22.0
- 90s Track Jacket — Navy/White Stripe — $45.0
- Corduroy Wide-Leg Pants — Rust — $32.0
- Graphic Tee — 2003 Tour Bootleg Style — $24.0
- Denim Jacket — Light Wash, Cropped — $42.0
- Vintage Windbreaker — Color Block Purple/Teal — $40.0
- Low-Rise Cargo Pants — Khaki — $27.0
- Oversized Crewneck Sweatshirt — Vintage Navy — $20.0
- 90s Silk Slip Dress — Floral, Midi Length — $30.0
- Leather Belt — Brown, Braided — $12.0
- Vintage Graphic Hoodie — Faded Black — $26.0
- High-Waisted Denim Shorts — Cutoff — $24.0
- Mesh Long-Sleeve Top — Black — $15.0
- Vintage Linen Blazer — Cream — $38.0
- Henley Long Sleeve — Washed Burgundy — $16.0
- Straight Leg Khaki Trousers — Olive — $29.0
- 90s Leather Bomber — Black — $75.0
- Vintage Polo Shirt — Forest Green — $18.0
- Oversized College Crewneck — Faded Red — $21.0
- Suede Chelsea Boots — Tan — $44.0
- Silk Button-Down — Sage Green — $28.0
- Vintage Knit Vest — Argyle Brown/Cream — $25.0
- Baggy Carpenter Jeans — Dark Wash — $36.0
- Vintage Band Tee — Faded Grey — $19.0
- Bucket Hat — Reversible, Brown Plaid — $14.0
- Velvet Blazer — Emerald Green — $52.0
- Straight Leg Black Jeans — Faded — $30.0
- Denim Vest — Medium Wash, Studded — $27.0
- Mini Shoulder Bag — Tan Leather — $38.0

Outfit suggestion:

```
* **Y2K Streetwear Contrast:** Pair the pink-and-purple butterfly baby tee with your baggy dark-wash straight-leg jeans to balance the cropped silhouette with a relaxed, low-key bottom. Layer the slightly cropped vintage black denim jacket on top, and finish the look with your chunky white sneakers and the black crossbody bag. 
* **Model-Off-Duty Casual:** Tuck the baby tee into your wide-leg khaki trousers, defined by the brown leather belt to pull in the earth tones. Throw your oversized grey crewneck sweatshirt over your shoulders or wear it open, and anchor the outfit with your chunky white sneakers for an effortless, texture-mixed everyday vibe.
```

Fit card:

```
scored this dreamy y2k butterfly baby tee on depop for just 18 dollars! totally obsessed with styling it casual with wide-leg trousers and a chunky sweater.
```

- Character count (including spaces): 156

Trace:

```
[1] parse_query
      in:  vintage graphic tee under $30
      out: dict with keys: description, size, max_price
      →    parsed by model
[2] estimate_price
      in:  dict with keys: description, results
      out: dict with keys: typical_price, sample_size, rated
[3] select_item
      in:  10 results
      out: Y2K Baby Tee — Butterfly Print ($18.0, depop)
      →    selected first result
[4] suggest_outfit
      in:  dict with keys: item, wardrobe_items
      out: * **Y2K Streetwear Contrast:** Pair the pink-and-purple butterfly baby tee with your baggy dark-wash straight-…
[5] create_fit_card
      in:  dict with keys: item, outfit
      out: scored this dreamy y2k butterfly baby tee on depop for just 18 dollars! totally obsessed with styling it casua…
```

**Try 2**

- stopped early: no
- selected_item: Y2K Baby Tee — Butterfly Print ($18.0, depop)
- search_results: 10

- parsed_by: model — parsed: {'description': 'vintage graphic tee', 'size': None, 'max_price': 30.0}

- typical_price: 27.0 (sample_size 31)
- every search result rated: True (10 rated / 10 results)
- all labels valid: True

Labels (actual vs. 20% rule):

| id | title | price | deal | expected | match |
|---|---|---|---|---|---|
| lst_002 | Y2K Baby Tee — Butterfly Print | 18.0 | good deal | good deal | yes |
| lst_006 | Graphic Tee — 2003 Tour Bootleg Style | 24.0 | fair | fair | yes |
| lst_033 | Vintage Band Tee — Faded Grey | 19.0 | good deal | good deal | yes |
| lst_015 | Vintage Graphic Hoodie — Faded Black | 26.0 | fair | fair | yes |
| lst_003 | Oversized Flannel Shirt — Plaid Red/Black | 22.0 | fair | fair | yes |
| lst_012 | Oversized Crewneck Sweatshirt — Vintage Navy | 20.0 | good deal | good deal | yes |
| lst_013 | 90s Silk Slip Dress — Floral, Midi Length | 30.0 | fair | fair | yes |
| lst_014 | Leather Belt — Brown, Braided | 12.0 | good deal | good deal | yes |
| lst_016 | High-Waisted Denim Shorts — Cutoff | 24.0 | fair | fair | yes |
| lst_017 | Mesh Long-Sleeve Top — Black | 15.0 | good deal | good deal | yes |

Comparables for 'vintage graphic tee' (31):

- Vintage Levi's 501 Jeans — Medium Wash — $38.0
- Y2K Baby Tee — Butterfly Print — $18.0
- Oversized Flannel Shirt — Plaid Red/Black — $22.0
- 90s Track Jacket — Navy/White Stripe — $45.0
- Corduroy Wide-Leg Pants — Rust — $32.0
- Graphic Tee — 2003 Tour Bootleg Style — $24.0
- Denim Jacket — Light Wash, Cropped — $42.0
- Vintage Windbreaker — Color Block Purple/Teal — $40.0
- Low-Rise Cargo Pants — Khaki — $27.0
- Oversized Crewneck Sweatshirt — Vintage Navy — $20.0
- 90s Silk Slip Dress — Floral, Midi Length — $30.0
- Leather Belt — Brown, Braided — $12.0
- Vintage Graphic Hoodie — Faded Black — $26.0
- High-Waisted Denim Shorts — Cutoff — $24.0
- Mesh Long-Sleeve Top — Black — $15.0
- Vintage Linen Blazer — Cream — $38.0
- Henley Long Sleeve — Washed Burgundy — $16.0
- Straight Leg Khaki Trousers — Olive — $29.0
- 90s Leather Bomber — Black — $75.0
- Vintage Polo Shirt — Forest Green — $18.0
- Oversized College Crewneck — Faded Red — $21.0
- Suede Chelsea Boots — Tan — $44.0
- Silk Button-Down — Sage Green — $28.0
- Vintage Knit Vest — Argyle Brown/Cream — $25.0
- Baggy Carpenter Jeans — Dark Wash — $36.0
- Vintage Band Tee — Faded Grey — $19.0
- Bucket Hat — Reversible, Brown Plaid — $14.0
- Velvet Blazer — Emerald Green — $52.0
- Straight Leg Black Jeans — Faded — $30.0
- Denim Vest — Medium Wash, Studded — $27.0
- Mini Shoulder Bag — Tan Leather — $38.0

Outfit suggestion:

```
* **Y2K Streetwear Contrast:** Pair the pink-and-purple butterfly baby tee with your baggy dark-wash straight-leg jeans to balance the cropped silhouette with a relaxed, low-key bottom. Layer the slightly cropped vintage black denim jacket on top, and finish the look with your chunky white sneakers and the black crossbody bag. 
* **Model-Off-Duty Casual:** Tuck the baby tee into your wide-leg khaki trousers, defined by the brown leather belt to pull in the earth tones. Throw your oversized grey crewneck sweatshirt over your shoulders or wear it open, and anchor the outfit with your chunky white sneakers for an effortless, texture-mixed everyday vibe.
```

Fit card:

```
scored this y2k butterfly baby tee on depop for $18 and i'm obsessed. styling it with baggy dark denim and chunky sneakers for the ultimate street fit.
```

- Character count (including spaces): 151

Trace:

```
[1] parse_query
      in:  vintage graphic tee under $30
      out: dict with keys: description, size, max_price
      →    parsed by model
[2] estimate_price
      in:  dict with keys: description, results
      out: dict with keys: typical_price, sample_size, rated
[3] select_item
      in:  10 results
      out: Y2K Baby Tee — Butterfly Print ($18.0, depop)
      →    selected first result
[4] suggest_outfit
      in:  dict with keys: item, wardrobe_items
      out: * **Y2K Streetwear Contrast:** Pair the pink-and-purple butterfly baby tee with your baggy dark-wash straight-…
[5] create_fit_card
      in:  dict with keys: item, outfit
      out: scored this y2k butterfly baby tee on depop for $18 and i'm obsessed. styling it with baggy dark denim and chu…
```

**Try 3**

- stopped early: no
- selected_item: Y2K Baby Tee — Butterfly Print ($18.0, depop)
- search_results: 10

- parsed_by: model — parsed: {'description': 'vintage graphic tee', 'size': None, 'max_price': 30.0}

- typical_price: 27.0 (sample_size 31)
- every search result rated: True (10 rated / 10 results)
- all labels valid: True

Labels (actual vs. 20% rule):

| id | title | price | deal | expected | match |
|---|---|---|---|---|---|
| lst_002 | Y2K Baby Tee — Butterfly Print | 18.0 | good deal | good deal | yes |
| lst_006 | Graphic Tee — 2003 Tour Bootleg Style | 24.0 | fair | fair | yes |
| lst_033 | Vintage Band Tee — Faded Grey | 19.0 | good deal | good deal | yes |
| lst_015 | Vintage Graphic Hoodie — Faded Black | 26.0 | fair | fair | yes |
| lst_003 | Oversized Flannel Shirt — Plaid Red/Black | 22.0 | fair | fair | yes |
| lst_012 | Oversized Crewneck Sweatshirt — Vintage Navy | 20.0 | good deal | good deal | yes |
| lst_013 | 90s Silk Slip Dress — Floral, Midi Length | 30.0 | fair | fair | yes |
| lst_014 | Leather Belt — Brown, Braided | 12.0 | good deal | good deal | yes |
| lst_016 | High-Waisted Denim Shorts — Cutoff | 24.0 | fair | fair | yes |
| lst_017 | Mesh Long-Sleeve Top — Black | 15.0 | good deal | good deal | yes |

Comparables for 'vintage graphic tee' (31):

- Vintage Levi's 501 Jeans — Medium Wash — $38.0
- Y2K Baby Tee — Butterfly Print — $18.0
- Oversized Flannel Shirt — Plaid Red/Black — $22.0
- 90s Track Jacket — Navy/White Stripe — $45.0
- Corduroy Wide-Leg Pants — Rust — $32.0
- Graphic Tee — 2003 Tour Bootleg Style — $24.0
- Denim Jacket — Light Wash, Cropped — $42.0
- Vintage Windbreaker — Color Block Purple/Teal — $40.0
- Low-Rise Cargo Pants — Khaki — $27.0
- Oversized Crewneck Sweatshirt — Vintage Navy — $20.0
- 90s Silk Slip Dress — Floral, Midi Length — $30.0
- Leather Belt — Brown, Braided — $12.0
- Vintage Graphic Hoodie — Faded Black — $26.0
- High-Waisted Denim Shorts — Cutoff — $24.0
- Mesh Long-Sleeve Top — Black — $15.0
- Vintage Linen Blazer — Cream — $38.0
- Henley Long Sleeve — Washed Burgundy — $16.0
- Straight Leg Khaki Trousers — Olive — $29.0
- 90s Leather Bomber — Black — $75.0
- Vintage Polo Shirt — Forest Green — $18.0
- Oversized College Crewneck — Faded Red — $21.0
- Suede Chelsea Boots — Tan — $44.0
- Silk Button-Down — Sage Green — $28.0
- Vintage Knit Vest — Argyle Brown/Cream — $25.0
- Baggy Carpenter Jeans — Dark Wash — $36.0
- Vintage Band Tee — Faded Grey — $19.0
- Bucket Hat — Reversible, Brown Plaid — $14.0
- Velvet Blazer — Emerald Green — $52.0
- Straight Leg Black Jeans — Faded — $30.0
- Denim Vest — Medium Wash, Studded — $27.0
- Mini Shoulder Bag — Tan Leather — $38.0

Outfit suggestion:

```
* **Y2K Streetwear Contrast:** Pair the pink-and-purple butterfly baby tee with your baggy dark-wash straight-leg jeans to balance the cropped silhouette with a relaxed, low-key bottom. Layer the slightly cropped vintage black denim jacket on top, and finish the look with your chunky white sneakers and the black crossbody bag. 
* **Model-Off-Duty Casual:** Tuck the baby tee into your wide-leg khaki trousers, defined by the brown leather belt to pull in the earth tones. Throw your oversized grey crewneck sweatshirt over your shoulders or wear it open, and anchor the outfit with your chunky white sneakers for an effortless, texture-mixed everyday vibe.
```

Fit card:

```
scored this little butterfly baby tee on depop for just 18 and i am obsessed. styling it with baggy dark denim and chunky sneakers for the ultimate y2k streetwear look.
```

- Character count (including spaces): 168

Trace:

```
[1] parse_query
      in:  vintage graphic tee under $30
      out: dict with keys: description, size, max_price
      →    parsed by model
[2] estimate_price
      in:  dict with keys: description, results
      out: dict with keys: typical_price, sample_size, rated
[3] select_item
      in:  10 results
      out: Y2K Baby Tee — Butterfly Print ($18.0, depop)
      →    selected first result
[4] suggest_outfit
      in:  dict with keys: item, wardrobe_items
      out: * **Y2K Streetwear Contrast:** Pair the pink-and-purple butterfly baby tee with your baggy dark-wash straight-…
[5] create_fit_card
      in:  dict with keys: item, outfit
      out: scored this little butterfly baby tee on depop for just 18 and i am obsessed. styling it with baggy dark denim…
```

**Try 4**

- stopped early: no
- selected_item: Y2K Baby Tee — Butterfly Print ($18.0, depop)
- search_results: 10

- parsed_by: model — parsed: {'description': 'vintage graphic tee', 'size': None, 'max_price': 30.0}

- typical_price: 27.0 (sample_size 31)
- every search result rated: True (10 rated / 10 results)
- all labels valid: True

Labels (actual vs. 20% rule):

| id | title | price | deal | expected | match |
|---|---|---|---|---|---|
| lst_002 | Y2K Baby Tee — Butterfly Print | 18.0 | good deal | good deal | yes |
| lst_006 | Graphic Tee — 2003 Tour Bootleg Style | 24.0 | fair | fair | yes |
| lst_033 | Vintage Band Tee — Faded Grey | 19.0 | good deal | good deal | yes |
| lst_015 | Vintage Graphic Hoodie — Faded Black | 26.0 | fair | fair | yes |
| lst_003 | Oversized Flannel Shirt — Plaid Red/Black | 22.0 | fair | fair | yes |
| lst_012 | Oversized Crewneck Sweatshirt — Vintage Navy | 20.0 | good deal | good deal | yes |
| lst_013 | 90s Silk Slip Dress — Floral, Midi Length | 30.0 | fair | fair | yes |
| lst_014 | Leather Belt — Brown, Braided | 12.0 | good deal | good deal | yes |
| lst_016 | High-Waisted Denim Shorts — Cutoff | 24.0 | fair | fair | yes |
| lst_017 | Mesh Long-Sleeve Top — Black | 15.0 | good deal | good deal | yes |

Comparables for 'vintage graphic tee' (31):

- Vintage Levi's 501 Jeans — Medium Wash — $38.0
- Y2K Baby Tee — Butterfly Print — $18.0
- Oversized Flannel Shirt — Plaid Red/Black — $22.0
- 90s Track Jacket — Navy/White Stripe — $45.0
- Corduroy Wide-Leg Pants — Rust — $32.0
- Graphic Tee — 2003 Tour Bootleg Style — $24.0
- Denim Jacket — Light Wash, Cropped — $42.0
- Vintage Windbreaker — Color Block Purple/Teal — $40.0
- Low-Rise Cargo Pants — Khaki — $27.0
- Oversized Crewneck Sweatshirt — Vintage Navy — $20.0
- 90s Silk Slip Dress — Floral, Midi Length — $30.0
- Leather Belt — Brown, Braided — $12.0
- Vintage Graphic Hoodie — Faded Black — $26.0
- High-Waisted Denim Shorts — Cutoff — $24.0
- Mesh Long-Sleeve Top — Black — $15.0
- Vintage Linen Blazer — Cream — $38.0
- Henley Long Sleeve — Washed Burgundy — $16.0
- Straight Leg Khaki Trousers — Olive — $29.0
- 90s Leather Bomber — Black — $75.0
- Vintage Polo Shirt — Forest Green — $18.0
- Oversized College Crewneck — Faded Red — $21.0
- Suede Chelsea Boots — Tan — $44.0
- Silk Button-Down — Sage Green — $28.0
- Vintage Knit Vest — Argyle Brown/Cream — $25.0
- Baggy Carpenter Jeans — Dark Wash — $36.0
- Vintage Band Tee — Faded Grey — $19.0
- Bucket Hat — Reversible, Brown Plaid — $14.0
- Velvet Blazer — Emerald Green — $52.0
- Straight Leg Black Jeans — Faded — $30.0
- Denim Vest — Medium Wash, Studded — $27.0
- Mini Shoulder Bag — Tan Leather — $38.0

Outfit suggestion:

```
* **Y2K Streetwear Contrast:** Pair the pink-and-purple butterfly baby tee with your baggy dark-wash straight-leg jeans to balance the cropped silhouette with a relaxed, low-key bottom. Layer the slightly cropped vintage black denim jacket on top, and finish the look with your chunky white sneakers and the black crossbody bag. 
* **Model-Off-Duty Casual:** Tuck the baby tee into your wide-leg khaki trousers, defined by the brown leather belt to pull in the earth tones. Throw your oversized grey crewneck sweatshirt over your shoulders or wear it open, and anchor the outfit with your chunky white sneakers for an effortless, texture-mixed everyday vibe.
```

Fit card:

```
scored this y2k butterfly baby tee on depop for just $18 and i'm obsessed. styling it with baggy dark denim and chunky sneakers for the ultimate street fit.
```

- Character count (including spaces): 156

Trace:

```
[1] parse_query
      in:  vintage graphic tee under $30
      out: dict with keys: description, size, max_price
      →    parsed by model
[2] estimate_price
      in:  dict with keys: description, results
      out: dict with keys: typical_price, sample_size, rated
[3] select_item
      in:  10 results
      out: Y2K Baby Tee — Butterfly Print ($18.0, depop)
      →    selected first result
[4] suggest_outfit
      in:  dict with keys: item, wardrobe_items
      out: * **Y2K Streetwear Contrast:** Pair the pink-and-purple butterfly baby tee with your baggy dark-wash straight-…
[5] create_fit_card
      in:  dict with keys: item, outfit
      out: scored this y2k butterfly baby tee on depop for just $18 and i'm obsessed. styling it with baggy dark denim an…
```

**Try 5**

- stopped early: no
- selected_item: Y2K Baby Tee — Butterfly Print ($18.0, depop)
- search_results: 10

- parsed_by: model — parsed: {'description': 'vintage graphic tee', 'size': None, 'max_price': 30.0}

- typical_price: 27.0 (sample_size 31)
- every search result rated: True (10 rated / 10 results)
- all labels valid: True

Labels (actual vs. 20% rule):

| id | title | price | deal | expected | match |
|---|---|---|---|---|---|
| lst_002 | Y2K Baby Tee — Butterfly Print | 18.0 | good deal | good deal | yes |
| lst_006 | Graphic Tee — 2003 Tour Bootleg Style | 24.0 | fair | fair | yes |
| lst_033 | Vintage Band Tee — Faded Grey | 19.0 | good deal | good deal | yes |
| lst_015 | Vintage Graphic Hoodie — Faded Black | 26.0 | fair | fair | yes |
| lst_003 | Oversized Flannel Shirt — Plaid Red/Black | 22.0 | fair | fair | yes |
| lst_012 | Oversized Crewneck Sweatshirt — Vintage Navy | 20.0 | good deal | good deal | yes |
| lst_013 | 90s Silk Slip Dress — Floral, Midi Length | 30.0 | fair | fair | yes |
| lst_014 | Leather Belt — Brown, Braided | 12.0 | good deal | good deal | yes |
| lst_016 | High-Waisted Denim Shorts — Cutoff | 24.0 | fair | fair | yes |
| lst_017 | Mesh Long-Sleeve Top — Black | 15.0 | good deal | good deal | yes |

Comparables for 'vintage graphic tee' (31):

- Vintage Levi's 501 Jeans — Medium Wash — $38.0
- Y2K Baby Tee — Butterfly Print — $18.0
- Oversized Flannel Shirt — Plaid Red/Black — $22.0
- 90s Track Jacket — Navy/White Stripe — $45.0
- Corduroy Wide-Leg Pants — Rust — $32.0
- Graphic Tee — 2003 Tour Bootleg Style — $24.0
- Denim Jacket — Light Wash, Cropped — $42.0
- Vintage Windbreaker — Color Block Purple/Teal — $40.0
- Low-Rise Cargo Pants — Khaki — $27.0
- Oversized Crewneck Sweatshirt — Vintage Navy — $20.0
- 90s Silk Slip Dress — Floral, Midi Length — $30.0
- Leather Belt — Brown, Braided — $12.0
- Vintage Graphic Hoodie — Faded Black — $26.0
- High-Waisted Denim Shorts — Cutoff — $24.0
- Mesh Long-Sleeve Top — Black — $15.0
- Vintage Linen Blazer — Cream — $38.0
- Henley Long Sleeve — Washed Burgundy — $16.0
- Straight Leg Khaki Trousers — Olive — $29.0
- 90s Leather Bomber — Black — $75.0
- Vintage Polo Shirt — Forest Green — $18.0
- Oversized College Crewneck — Faded Red — $21.0
- Suede Chelsea Boots — Tan — $44.0
- Silk Button-Down — Sage Green — $28.0
- Vintage Knit Vest — Argyle Brown/Cream — $25.0
- Baggy Carpenter Jeans — Dark Wash — $36.0
- Vintage Band Tee — Faded Grey — $19.0
- Bucket Hat — Reversible, Brown Plaid — $14.0
- Velvet Blazer — Emerald Green — $52.0
- Straight Leg Black Jeans — Faded — $30.0
- Denim Vest — Medium Wash, Studded — $27.0
- Mini Shoulder Bag — Tan Leather — $38.0

Outfit suggestion:

```
* **Y2K Streetwear Contrast:** Pair the pink-and-purple butterfly baby tee with your baggy dark-wash straight-leg jeans to balance the cropped silhouette with a relaxed, low-key bottom. Layer the slightly cropped vintage black denim jacket on top, and finish the look with your chunky white sneakers and the black crossbody bag. 
* **Model-Off-Duty Casual:** Tuck the baby tee into your wide-leg khaki trousers, defined by the brown leather belt to pull in the earth tones. Throw your oversized grey crewneck sweatshirt over your shoulders or wear it open, and anchor the outfit with your chunky white sneakers for an effortless, texture-mixed everyday vibe.
```

Fit card:

```
scored this y2k butterfly baby tee on depop for $18 and i'm obsessed. styling it with baggy dark denim and chunky sneakers for the ultimate off-duty look.
```

- Character count (including spaces): 154

Trace:

```
[1] parse_query
      in:  vintage graphic tee under $30
      out: dict with keys: description, size, max_price
      →    parsed by model
[2] estimate_price
      in:  dict with keys: description, results
      out: dict with keys: typical_price, sample_size, rated
[3] select_item
      in:  10 results
      out: Y2K Baby Tee — Butterfly Print ($18.0, depop)
      →    selected first result
[4] suggest_outfit
      in:  dict with keys: item, wardrobe_items
      out: * **Y2K Streetwear Contrast:** Pair the pink-and-purple butterfly baby tee with your baggy dark-wash straight-…
[5] create_fit_card
      in:  dict with keys: item, outfit
      out: scored this y2k butterfly baby tee on depop for $18 and i'm obsessed. styling it with baggy dark denim and chu…
```

### price estimation failure doesn't break the run

- Query: `denim jacket size S under $50`
- Wardrobe: example

**Try 1**

- stopped early: no
- selected_item: Denim Jacket — Light Wash, Cropped ($42.0, poshmark)
- search_results: 1

- parsed_by: model — parsed: {'description': 'denim jacket', 'size': 'S', 'max_price': 50.0}

- typical_price: None (sample_size 0)
- every search result rated: True (1 rated / 1 results)
- all labels valid: True

Labels (actual vs. 20% rule):

| id | title | price | deal | expected | match |
|---|---|---|---|---|---|
| lst_007 | Denim Jacket — Light Wash, Cropped | 42.0 | unknown | unknown | yes |

Comparables for 'denim jacket' (8):

- Vintage Levi's 501 Jeans — Medium Wash — $38.0
- 90s Track Jacket — Navy/White Stripe — $45.0
- Denim Jacket — Light Wash, Cropped — $42.0
- High-Waisted Denim Shorts — Cutoff — $24.0
- 90s Leather Bomber — Black — $75.0
- Shacket — Olive Canvas — $33.0
- Straight Leg Black Jeans — Faded — $30.0
- Denim Vest — Medium Wash, Studded — $27.0

Outfit suggestion:

```
* **The Double Denim Contrast:** Tuck the **white ribbed tank top** into the **baggy straight-leg jeans, dark wash**, secure it with the **brown leather belt**, and layer the light wash cropped denim jacket right over top to play with the two-tone indigo shades. Finish this streetwear-inspired look with the **chunky white sneakers** and the **black crossbody bag**.
* **The High-Contrast Neutral:** Pair the **wide-leg khaki trousers** with the **white ribbed tank top**, and wear the light wash cropped denim jacket open to highlight the high waist. Ground the earthy tones with the **black combat boots** and sling the **black crossbody bag** across your chest for an effortless finish.
```

Fit card:

```
Scored this cropped light wash denim jacket on Poshmark for $42 and I’m obsessed with the structured shoulders. Perfect blank canvas for throwing over baggy dark wash jeans for a double denim moment.
```

- Character count (including spaces): 199

Trace:

```
[1] parse_query
      in:  denim jacket size S under $50
      out: dict with keys: description, size, max_price
      →    parsed by model
[2] estimate_price
      in:  dict with keys: description, results
      out: dict with keys: typical_price, sample_size, rated
      →    estimate_price failed (RuntimeError: simulated: estimate_price failed), labels set to unknown
[3] select_item
      in:  1 results
      out: Denim Jacket — Light Wash, Cropped ($42.0, poshmark)
      →    selected first result
[4] suggest_outfit
      in:  dict with keys: item, wardrobe_items
      out: * **The Double Denim Contrast:** Tuck the **white ribbed tank top** into the **baggy straight-leg jeans, dark …
[5] create_fit_card
      in:  dict with keys: item, outfit
      out: Scored this cropped light wash denim jacket on Poshmark for $42 and I’m obsessed with the structured shoulders…
```

**Try 2**

- stopped early: no
- selected_item: Denim Jacket — Light Wash, Cropped ($42.0, poshmark)
- search_results: 1

- parsed_by: model — parsed: {'description': 'denim jacket', 'size': 'S', 'max_price': 50.0}

- typical_price: None (sample_size 0)
- every search result rated: True (1 rated / 1 results)
- all labels valid: True

Labels (actual vs. 20% rule):

| id | title | price | deal | expected | match |
|---|---|---|---|---|---|
| lst_007 | Denim Jacket — Light Wash, Cropped | 42.0 | unknown | unknown | yes |

Comparables for 'denim jacket' (8):

- Vintage Levi's 501 Jeans — Medium Wash — $38.0
- 90s Track Jacket — Navy/White Stripe — $45.0
- Denim Jacket — Light Wash, Cropped — $42.0
- High-Waisted Denim Shorts — Cutoff — $24.0
- 90s Leather Bomber — Black — $75.0
- Shacket — Olive Canvas — $33.0
- Straight Leg Black Jeans — Faded — $30.0
- Denim Vest — Medium Wash, Studded — $27.0

Outfit suggestion:

```
* **The Double Denim Contrast:** Tuck the **white ribbed tank top** into the **baggy straight-leg jeans, dark wash**, secure it with the **brown leather belt**, and layer the light wash cropped denim jacket right over top to play with the two-tone indigo shades. Finish this streetwear-inspired look with the **chunky white sneakers** and the **black crossbody bag**.
* **The High-Contrast Neutral:** Pair the **wide-leg khaki trousers** with the **white ribbed tank top**, and wear the light wash cropped denim jacket open to highlight the high waist. Ground the earthy tones with the **black combat boots** and sling the **black crossbody bag** across your chest for an effortless finish.
```

Fit card:

```
Found this cropped denim jacket on Poshmark for $42 and I'm obsessed with the structured shoulders. Been living in it with dark baggy jeans for that perfect double-denim streetwear look.
```

- Character count (including spaces): 186

Trace:

```
[1] parse_query
      in:  denim jacket size S under $50
      out: dict with keys: description, size, max_price
      →    parsed by model
[2] estimate_price
      in:  dict with keys: description, results
      out: dict with keys: typical_price, sample_size, rated
      →    estimate_price failed (RuntimeError: simulated: estimate_price failed), labels set to unknown
[3] select_item
      in:  1 results
      out: Denim Jacket — Light Wash, Cropped ($42.0, poshmark)
      →    selected first result
[4] suggest_outfit
      in:  dict with keys: item, wardrobe_items
      out: * **The Double Denim Contrast:** Tuck the **white ribbed tank top** into the **baggy straight-leg jeans, dark …
[5] create_fit_card
      in:  dict with keys: item, outfit
      out: Found this cropped denim jacket on Poshmark for $42 and I'm obsessed with the structured shoulders. Been livin…
```

**Try 3**

- stopped early: no
- selected_item: Denim Jacket — Light Wash, Cropped ($42.0, poshmark)
- search_results: 1

- parsed_by: model — parsed: {'description': 'denim jacket', 'size': 'S', 'max_price': 50.0}

- typical_price: None (sample_size 0)
- every search result rated: True (1 rated / 1 results)
- all labels valid: True

Labels (actual vs. 20% rule):

| id | title | price | deal | expected | match |
|---|---|---|---|---|---|
| lst_007 | Denim Jacket — Light Wash, Cropped | 42.0 | unknown | unknown | yes |

Comparables for 'denim jacket' (8):

- Vintage Levi's 501 Jeans — Medium Wash — $38.0
- 90s Track Jacket — Navy/White Stripe — $45.0
- Denim Jacket — Light Wash, Cropped — $42.0
- High-Waisted Denim Shorts — Cutoff — $24.0
- 90s Leather Bomber — Black — $75.0
- Shacket — Olive Canvas — $33.0
- Straight Leg Black Jeans — Faded — $30.0
- Denim Vest — Medium Wash, Studded — $27.0

Outfit suggestion:

```
* **The Double Denim Contrast:** Tuck the **white ribbed tank top** into the **baggy straight-leg jeans, dark wash**, secure it with the **brown leather belt**, and layer the light wash cropped denim jacket right over top to play with the two-tone indigo shades. Finish this streetwear-inspired look with the **chunky white sneakers** and the **black crossbody bag**.
* **The High-Contrast Neutral:** Pair the **wide-leg khaki trousers** with the **white ribbed tank top**, and wear the light wash cropped denim jacket open to highlight the high waist. Ground the earthy tones with the **black combat boots** and sling the **black crossbody bag** across your chest for an effortless finish.
```

Fit card:

```
Scored this light wash cropped denim jacket on Poshmark for $42 and I’m obsessed. The structured shoulders look so good with baggy dark denim for a double-denim moment.
```

- Character count (including spaces): 168

Trace:

```
[1] parse_query
      in:  denim jacket size S under $50
      out: dict with keys: description, size, max_price
      →    parsed by model
[2] estimate_price
      in:  dict with keys: description, results
      out: dict with keys: typical_price, sample_size, rated
      →    estimate_price failed (RuntimeError: simulated: estimate_price failed), labels set to unknown
[3] select_item
      in:  1 results
      out: Denim Jacket — Light Wash, Cropped ($42.0, poshmark)
      →    selected first result
[4] suggest_outfit
      in:  dict with keys: item, wardrobe_items
      out: * **The Double Denim Contrast:** Tuck the **white ribbed tank top** into the **baggy straight-leg jeans, dark …
[5] create_fit_card
      in:  dict with keys: item, outfit
      out: Scored this light wash cropped denim jacket on Poshmark for $42 and I’m obsessed. The structured shoulders loo…
```

**Try 4**

- stopped early: no
- selected_item: Denim Jacket — Light Wash, Cropped ($42.0, poshmark)
- search_results: 1

- parsed_by: model — parsed: {'description': 'denim jacket', 'size': 'S', 'max_price': 50.0}

- typical_price: None (sample_size 0)
- every search result rated: True (1 rated / 1 results)
- all labels valid: True

Labels (actual vs. 20% rule):

| id | title | price | deal | expected | match |
|---|---|---|---|---|---|
| lst_007 | Denim Jacket — Light Wash, Cropped | 42.0 | unknown | unknown | yes |

Comparables for 'denim jacket' (8):

- Vintage Levi's 501 Jeans — Medium Wash — $38.0
- 90s Track Jacket — Navy/White Stripe — $45.0
- Denim Jacket — Light Wash, Cropped — $42.0
- High-Waisted Denim Shorts — Cutoff — $24.0
- 90s Leather Bomber — Black — $75.0
- Shacket — Olive Canvas — $33.0
- Straight Leg Black Jeans — Faded — $30.0
- Denim Vest — Medium Wash, Studded — $27.0

Outfit suggestion:

```
* **The Double Denim Contrast:** Tuck the **white ribbed tank top** into the **baggy straight-leg jeans, dark wash**, secure it with the **brown leather belt**, and layer the light wash cropped denim jacket right over top to play with the two-tone indigo shades. Finish this streetwear-inspired look with the **chunky white sneakers** and the **black crossbody bag**.
* **The High-Contrast Neutral:** Pair the **wide-leg khaki trousers** with the **white ribbed tank top**, and wear the light wash cropped denim jacket open to highlight the high waist. Ground the earthy tones with the **black combat boots** and sling the **black crossbody bag** across your chest for an effortless finish.
```

Fit card:

```
Finally found the perfect cropped light wash denim jacket on Poshmark for $42. Obsessed with how the structured shoulders look paired with baggy dark denim for double denim.
```

- Character count (including spaces): 173

Trace:

```
[1] parse_query
      in:  denim jacket size S under $50
      out: dict with keys: description, size, max_price
      →    parsed by model
[2] estimate_price
      in:  dict with keys: description, results
      out: dict with keys: typical_price, sample_size, rated
      →    estimate_price failed (RuntimeError: simulated: estimate_price failed), labels set to unknown
[3] select_item
      in:  1 results
      out: Denim Jacket — Light Wash, Cropped ($42.0, poshmark)
      →    selected first result
[4] suggest_outfit
      in:  dict with keys: item, wardrobe_items
      out: * **The Double Denim Contrast:** Tuck the **white ribbed tank top** into the **baggy straight-leg jeans, dark …
[5] create_fit_card
      in:  dict with keys: item, outfit
      out: Finally found the perfect cropped light wash denim jacket on Poshmark for $42. Obsessed with how the structure…
```

**Try 5**

- stopped early: no
- selected_item: Denim Jacket — Light Wash, Cropped ($42.0, poshmark)
- search_results: 1

- parsed_by: model — parsed: {'description': 'denim jacket', 'size': 'S', 'max_price': 50.0}

- typical_price: None (sample_size 0)
- every search result rated: True (1 rated / 1 results)
- all labels valid: True

Labels (actual vs. 20% rule):

| id | title | price | deal | expected | match |
|---|---|---|---|---|---|
| lst_007 | Denim Jacket — Light Wash, Cropped | 42.0 | unknown | unknown | yes |

Comparables for 'denim jacket' (8):

- Vintage Levi's 501 Jeans — Medium Wash — $38.0
- 90s Track Jacket — Navy/White Stripe — $45.0
- Denim Jacket — Light Wash, Cropped — $42.0
- High-Waisted Denim Shorts — Cutoff — $24.0
- 90s Leather Bomber — Black — $75.0
- Shacket — Olive Canvas — $33.0
- Straight Leg Black Jeans — Faded — $30.0
- Denim Vest — Medium Wash, Studded — $27.0

Outfit suggestion:

```
* **The Double Denim Contrast:** Tuck the **white ribbed tank top** into the **baggy straight-leg jeans, dark wash**, secure it with the **brown leather belt**, and layer the light wash cropped denim jacket right over top to play with the two-tone indigo shades. Finish this streetwear-inspired look with the **chunky white sneakers** and the **black crossbody bag**.
* **The High-Contrast Neutral:** Pair the **wide-leg khaki trousers** with the **white ribbed tank top**, and wear the light wash cropped denim jacket open to highlight the high waist. Ground the earthy tones with the **black combat boots** and sling the **black crossbody bag** across your chest for an effortless finish.
```

Fit card:

```
Scored this cropped light wash denim jacket on Poshmark for $42 and I’m obsessed. The structured shoulders look so good with baggy dark jeans for a full double-denim fit.
```

- Character count (including spaces): 170

Trace:

```
[1] parse_query
      in:  denim jacket size S under $50
      out: dict with keys: description, size, max_price
      →    parsed by model
[2] estimate_price
      in:  dict with keys: description, results
      out: dict with keys: typical_price, sample_size, rated
      →    estimate_price failed (RuntimeError: simulated: estimate_price failed), labels set to unknown
[3] select_item
      in:  1 results
      out: Denim Jacket — Light Wash, Cropped ($42.0, poshmark)
      →    selected first result
[4] suggest_outfit
      in:  dict with keys: item, wardrobe_items
      out: * **The Double Denim Contrast:** Tuck the **white ribbed tank top** into the **baggy straight-leg jeans, dark …
[5] create_fit_card
      in:  dict with keys: item, outfit
      out: Scored this cropped light wash denim jacket on Poshmark for $42 and I’m obsessed. The structured shoulders loo…
```
