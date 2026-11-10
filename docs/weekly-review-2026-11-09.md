# Weekly review 2026-11-09 — full numbers

Scope: 114 settled v3-schema entries; 306 unique settled legs (150-152, 49.7%, pushes excluded).
3 entries skipped silently (off-schema — all three are Sven's own ticket-level entries, unchanged since 10/28).
Dedupe: one count per unique (date, matchup, pick).
Ticket stats NOT deduped. Flat 1u. Script: hidden_files/weekly_review_2026_11_09.py
(adapted from the 11/02 script; week window = settled ≥ 2026-11-03).

## Headline

First positive week on legs in a while: 23 legs settled since 11/03, 13-10 (56.5%),
+4.87u at flat 1u singles — driven by NHL 5-2 (+1.80u) and NBA dogs 5-6 (+2.66u).
The staked set went 1-1 (-0.38u) on the two legs that settled: the Seahawks ML loss
is a transition leg (staked Nov 2 at 6am, before the 11/02 rule-1 slice-first rule
landed that afternoon — and under current rules it would fail three ways: home side,
8.1% claimed edge, single-model), while the Giants ML win was properly slice-qualified
(NFL away side, 4.5% edge). All staked legs now 21-25 (45.7%, -4.79u).
Two pre-committed checks resolve this week: the non-NFL re-open condition is MET
(trailing-20 11-9, 55.0% hit AND CLV 6b/2l, 75% — but on only 8 evaluable closes,
12 of 20 missing, so the re-open is scoped, not blanket — see rule 1), and the
haircut re-audit due today says the haircut STAYS (60-69 bucket gap +27.1pp at n=41).
CLV capture improved sharply (43.5% missing this week vs 84.6% last week) but is still
the seventh straight flag, concentrated in the paper tier (NBA 5/11, NHL 5/7 missing;
NFL 0/5). Dogfood trailing-20 top-5 recovered to exactly 12-8 (60.0%) — at the
structural-change line, not under it.

## Legs by sport

NFL 39-26 (60.0%, n=67) — still best sport; trailing-20 10-10 (50.0%), still under
the 55% re-open line, but rule 1 already replaced NFL-overall concentration with the
slices. NFL away 16-7 (69.6%, n=24), trailing-20 13-6 (68.4%). NFL home 6-14 (30.0%,
n=21) — worse than last week (5-12). NFL totals 16-5 (76.2%, n=21), trailing-20
15-5 (75.0%) — the strongest pocket in the ledger. | NHL 46-39 (54.1%, n=86),
trailing-20 12-8 (60.0%) — the only non-NFL sport above breakeven at scale. |
CFB 25-25 (50.0%, n=51) + NCAAF 2-6 (25.0%, n=8) = combined 27-31 (46.6%, n=59)
— the label split is STILL not normalized, fourth flag. | MLB 20-30 (40.0%, n=50),
unchanged (no MLB in season). | NBA 12-18 (40.0%, n=30) — crossed the n=20 entry
bar and FAILS graduation (trailing-20 9-11, 45.0% < 55%); stays a watched newcomer,
paper-only. | WNBA 6-8 (42.9%, n=14).

Non-NFL combined: trailing-20 11-9 (55.0%) on results; CLV 6b/2l on 8 evaluable,
12 missing — the re-open condition is met on the evaluable base, thin as it is.

## Legs by market / home-away

Moneyline 83-76 (52.2%, n=159) best; spread 36-39 (48.0%, n=78); totals 31-37
(45.6%, n=69) — still a tale of two sports (NFL totals 16-5 vs MLB totals 3-13).
Home/away (sides only): away 67-56 (54.5%, n=124) vs home 51-59 (46.4%, n=112) —
split persists; home 6% bar stays.

## Calibration (logged confidence; haircut in force since 10/26 for raw ≥60)

| bucket | n | stated | actual | gap |
|---|---|---|---|---|
| <50 | 62 | 43.5% | 52.5% | -8.9pp (dogs conservative-or-better — fine) |
| 50-59 | 196 | 54.9% | 49.7% | +5.2pp (just above the 5pp bar) |
| 60-69 | 41 | 63.7% | 36.6% | +27.1pp — haircut stays (re-audit due today) |
| 70+ | 7 | 72.0% | 100.0% | -28.0pp (tiny n) |

This week's subset (settled ≥11/03): 60-69 bucket 2-1 (66.7%, n=3) — first positive
subset since the haircut was reinstated, but n=3, preliminary; it does not move the
full-sample verdict. Next re-audit 11/23.

## CLV (corrected spread semantics)

Overall: beat 47 / lost 34 / push 66 / missing 159 (51.9% missing) — 58.0% excl
pushes, up from 56.3%, on a still-thin evaluable base. This week: beat 7 / lost 3 /
push 3 / missing 10 (43.5% missing, down from 84.6%). By sport this week: NFL 0/5
missing, NBA 5/11, NHL 5/7. The capture failure is now entirely the paper tier —
and NHL's 5/7 missing this week means, under the 11/02 rule-4 gate, no new NHL card
may be logged until those closes are backfilled or each is flagged with its source
documented as unavailable. Seventh straight flag, but improving.

## Approach vs approach (flat 1u singles)

model-value n=219, 110-106 (50.9%), CLV 60%, ROI -2.87u — the workhorse is still a
coin flip at scale (hit rate ticked above 50% for the first time, ROI still negative);
this week it was again the ONLY approach logged (23/23 legs, 13-10, +4.87u).
situational n=36, 16-19 (45.7%), CLV 60% — no new legs this week; dual trigger still
not met (trailing-20 hit 47.4% ≤50% met, CLV 75% not <50%). line-movement n=13,
5-8 (38.5%), CLV 0% — failing both metrics but still n=13 <20, no new legs.
model-edge n=15, 7-8 (46.7%), CLV 71% — mixed, preliminary. brand-tax fade
(approach field) n=9, 6-3 (66.7%), ROI +6.40u — preliminary, best ROI. fpi-chalk
0-3 stays demoted. dip-buy n=1, no verdict (eighth week). Multi-angle legs
7-3 (70.0%, n=10) — preliminary, unchanged this week (no new multi-angle legs).

## Claimed edge bands (numeric-aware parser)

below-4%: 53-45 (54.1%, n=100) — still outhits every band except the tiny 12%+ tail.
4.0-5.9%: 25-24 (51.0%, n=50). 6.0-7.9%: 25-21 (54.3%, n=47).
8.0%+: 31-41 (43.1%, n=72) — the worst eligible band; 8.0-11.9% sub-band 19-32
(37.3%, n=51, eligible), this week 5-7 (41.7%); 12%+ is 12-9 (57.1%, n=21,
preliminary). The inversion in the 8-12% range persists — rule 2 (multi-angle
requirement for that band) stands and did its job this week: the two 8%+ legs that
settled (49ers -9.5, edge 9.3; Rams/WAS Under 47.5, edge 8.1) were both paper, both won.

## Brand tax (sides only)

Backing marquee 4-6 (40.0%, n=10); fading marquee 15-9 (62.5%, n=24, eligible) —
the fade lean is supported at the 20-leg bar. Fade/back rules stand.

## Stack-rank dogfood (Sven's 10/7 goal: 80%)

Ranks 1-5: 54-62 (46.6%, n=116) vs ranks 6-10: 29-23 (55.8%, n=54) — ranking is
still inverted on the full sample. Daily average hit rate (ranks 1-5): 43.0% over
31 days (up from 38.9% over 24). Trailing-20 top-5: 12-8 (60.0%) vs the 80% goal —
recovered to exactly the 60% structural-change line, not under it; no structural
change fires this week. Qualified=true: 55-60 (47.8%, n=115) vs qualified=false:
60-54 (52.6%, n=117) — the binary-bar signal is still inverted on the full sample,
though qualified trailing-20 improved to 13-7 (65.0%), exactly at the 65% guardrail
from the 10/12 rule-2 re-audit.

## Best slice

Slice-qualified (NFL away sides + NFL totals): 32-12 (72.7%, n=45), trailing-20
14-6 (70.0%) — well above the 55% shrink trigger in 11/02 rule 1; the staked set
stays at max 5 slice legs, never forced. NFL overall trailing-20 10-10 (50.0%)
remains under the old 55% line, but that concentration rule was already replaced by
the slices. Nominated third slice this week: NHL (see rule 1).

## Tickets

Classic tiers unchanged (no classic tickets since 10/06): steady 2-3 (-1.67u),
balanced 1-13 (-10.35u), lottery 0-11 (-11.00u, suspended), single 1-0 (+0.71u),
single-lean 1-1 (-0.13u); all -22.43u over 33. Uncapped-tier staked legs @1u singles:
21-25 (45.7%, -4.79u); this week 1-1 (50.0%, -0.38u) — Seahawks ML -175 loss
(transition leg, pre-rule-1) and Giants ML -162 win (slice-qualified NFL away side).

## Props discovery (prop-ledger, never merged into v3)

Settled prop legs: 112 (64-48, 57.1%); this week 8 (7-1, 87.5%).
By prop_type, the only types at n≥10 are player prop 25-19 (56.8%, n=44),
parlay set leg (ML) 9-3 (75.0%, n=12), parlay set leg (ATS) 4-8 (33.3%, n=12),
player passing yards 5-5 (50.0%, n=10). By repeatable_pattern:
- GRADUATES (new): "star-RB vs elite run D" 3-0 (100.0%, n=3) — all UNDERS:
  Kenneth Walker III Under 85.5 (10/25 win), Derrick Henry Under 70.5 (11/05 win),
  D'Andre Swift Under 63.5 (11/08 win). Meets the 3+ / 65%+ bar; provisional,
  re-audit at n=6. Future legs on this angle carry the tag.
- Already graduated (11/02), unchanged: "efficient-RB vs soft-front overs" 2-1
  (66.7%, n=3) — no new legs this week; still provisional, re-audit at n=6.
- Already killed, re-flagged by the script on historical legs (NOT a new kill):
  "struggling-QB passing under vs elite pass D" 1-3 (25.0%, n=4).
- No other pattern at 3+ instances. Pattern hygiene still failing: 5 of 8 props
  settled this week carry NO repeatable_pattern (56 of 112 overall) — the 10/19
  consolidation rule is still not producing labelled legs, which caps discovery at
  n=3 graduations like this one.
- Sven's own legs in the v3 ledger: none newly settled this week (the three
  ticket-level entries are unchanged since 10/28); nothing re-scored here.

## Pending (excluded from all stats above)

4 legs pending for 2026-11-09, all paper (staked=False): Hornets +8.5, Hawks ML,
Suns ML, Islanders/Sharks Under 6.5.
