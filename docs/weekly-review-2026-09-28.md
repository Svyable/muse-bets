# Weekly review 2026-09-28 — full numbers

Scope: 24 settled v3-schema entries (top-level tier + source; legs carry pick, market, odds, confidence, approach, result). 4 entries skipped silently: 3 off-schema (Sven's 9/16 8-leg, 9/17 prop 7-leg, 9/19 2-pick — legs lack odds/confidence) and 1 pending (9/28 single-lean MNF leg). Dedupe: legs counted once per unique (date, matchup, pick) — e.g. 9/25 CWS ML logged in 3 tiers counts once. Ticket stats are NOT deduped. All odds @1u flat.

CLV semantics (per the 9/21 correction): ML — beat when booked odds numerically exceed closing odds (favorite: less juice; dog: bigger payout). Spread — beat when booked line numerically exceeds the closing line on the picked side (favorite laying fewer, dog getting more; closing spread logged in closing_odds is read as a line when |x|<=40). Total — over: beat when booked line < close; under: beat when booked line > close. Push when equal. 9/21's 5b/6l/1p is not directly comparable: several closes (Nationals ML, Astros +100 push) were backfilled into the ledger after that review.

## Tickets @1u

| tier | W-L | net | ROI |
|---|---|---|---|
| steady | 2-3 | -1.67u | -33.3% |
| balanced | 1-8 | -5.35u | -59.4% |
| lottery | 0-9 | -9.00u | -100.0% |
| single | 1-0 | +0.71u | +71.4% |
| **all** | **3-21** | **-15.30u** | **-63.8%** |

Sven's own (off-schema, ticket-level only — not re-scored): sven-8-leg 0-1 (legs 5-3), sven-prop-7-leg 1-0 (legs 7-0, +$12,278.17 real), sven-2-pick 0-1 (legs 1-1).

This week alone (settled since 9/21 review, entries dated 9/22-9/27): tickets 2-8 (-6.86u); unique legs 11-11 (50.0%); CLV 2b/4l/2p.

## Legs: 54 unique, 26-28 (48.1%)

By sport: NFL 12-10 (54.5%, n=22) | MLB 12-14 (46.2%, n=26) | CFB 2-4 (33.3%, n=6). No sport at the 50-leg bar — no cuts.

By market: moneyline 12-8 (60.0%) | spread 11-13 (45.8%) | total 3-7 (30.0%, preliminary).

By home/away (sides only, totals with null home_away excluded): away 17-9 (65.4%) | home 6-13 (31.6%). Home n=19 — one leg short of the 20 bar; watched.

## Calibration (logged confidence)

| bucket | n | stated avg | actual | gap |
|---|---|---|---|---|
| <50 | 20 | 43.0% | 50.0% | -7.0pp |
| 50-59 | 25 | 55.1% | 48.0% | +7.1pp |
| 60-69 | 9 | 62.8% | 44.4% | +18.3pp |
| 70+ | 0 | — | — | — |

<50 and 50-59 buckets are at the 20-leg eligibility bar. 60-69 is preliminary.

## CLV: 21 evaluable unique legs — 8 beat / 9 lost / 4 push (47.1% excl. pushes)

Beats: Padres ML 9/17 (-164 vs -196), Bills -4.5 9/17 (-4.5 vs -5.5), Mariners -1.5 9/18 (-118 vs -125 juice), Cubs ML 9/19 (-139 vs -146), Nationals ML 9/19 (+109 vs +104), NYG/LAR U48.5 9/21 (48.5 vs 47.5), Rays ML 9/23 (+128 vs +116), Astros ML 9/26 (-146 vs -162).
Losses: Blue Jays ML 9/18, Houston +7.5 9/18 (+7.5 vs +8), Mariners ML 9/19 (-163 vs -154), SC -4 9/19, Colorado ML 9/19, Giants ML 9/23, CLE/BOS O7.5 9/23 (7.5 vs 6.5), Guardians ML 9/26, Padres ML 9/26 (-116 vs -115).
Pushes: Astros +100 9/18, WSH/DET O8.5 9/21, STL/MIL O7.5 9/26, TB/PHI U6.5 9/26.

## Approach vs approach (primary approach = first component)

| approach | n | W-L | hit | CLV |
|---|---|---|---|---|
| situational | 20 | 9-11 | 45.0% | 3b/4l (42.9%) |
| model-edge | 10 | 6-4 | 60.0% | 4b/2l (66.7%) |
| fpi-value | 6 | 3-3 | 50.0% | n/a |
| line-movement | 5 | 3-2 | 60.0% | 0b/2l |
| brand-tax fade | 4 | 2-2 | 50.0% | 1b/0l |
| fpi-chalk | 3 | 0-3 | 0.0% | n/a |
| model-value | 2 | 1-1 | 50.0% | 0b/1l |
| mild-value | 2 | 1-1 | 50.0% | n/a |
| structural | 1 | 1-0 | 100% | n/a |
| dip-buy | 1 | 0-1 | 0.0% | n/a |

Only situational is at the 20-leg approach bar.

## Brand-tax (spread/ML sides only; totals excluded — brand tax is a side-pricing phenomenon)

Backing marquee (NYY, LAD, CHC, BOS, KC, DAL, PHI, NYG, LAL, GSW): 2-2 (Chiefs -6.5 L, Cowboys -3.5 W, Cubs ML W, Phillies ML L).
Fading marquee: 6-2 (Titans +7 W, Colts +6.5 W, Rays ML 9/22 W, Rays ML 9/23 L, Guardians ML 9/25 W, Orioles ML 9/25 W, Guardians ML 9/26 W, Dolphins +10.5 L).
Preliminary (n<20) but directionally supportive of the fade lean.

## Dip-buy: n=1 (Syracuse +10.5, L). No verdict.

## Method notes
- Script: /tmp/weekly_review.py (scratch; rerun against the ledger to reproduce).
- CLV evaluable set differs from the 9/21 review's 12 because closes were backfilled after 9/21; this review's numbers are computed on current ledger state.
- The 9/21 review's 66 settled legs were raw (non-deduped); this review uses the dedupe rule introduced in that review (54 unique).
