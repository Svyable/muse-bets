# Weekly review 2026-11-23 — full numbers

Scope: 128 settled v3-schema entries; 420 unique settled legs (201-215, 48.3%, pushes excluded).
3 entries skipped silently (off-schema — all three are Sven's own ticket-level entries, unchanged since 10/28).
Dedupe: one count per unique (date, matchup, pick).
Ticket stats NOT deduped. Flat 1u. Script: hidden_files/weekly_review_2026_11_23.py
(adapted from the 11/16 script; week window = settled ≥ 2026-11-17).
Script patch this week: CLV now coerces string closing_odds (a new leg stored them as strings);
props sort/format now tolerates prop_type=None.

## Headline

A bad week where the staked set itself is the problem: 47 legs settled since 11/17, 21-26 (44.7%),
and staked legs went 5-8 (-3.49u) on 13 settled legs — NFL staked 2-5, NHL staked 3-3.
All staked legs now 29-37 (43.9%, -10.11u). Three pre-committed triggers fire:
the slice-qualified trailing-20 fell to 9-11 (45.0%, under the 55% shrink line), the NHL
re-open close trigger fires on the CLV base (14/39 evaluable, 36% < 50%), and the CFB
label split still persists (CFB 89 / NCAAF 8) — CFB logging pauses per the 11/16 gate.
The fourth rule is new evidence, not a trigger: the claimed-edge 12%+ band is 18-25
(41.9%, n=43, eligible) and is the worst band in the ledger, and it was never covered by
the multi-angle requirement. The haircut re-audit due today says the haircut STAYS
(60-69 bucket n=50, gap +21.5pp).

## Legs by sport

NFL 46-35 (56.8%, n=83) — still best sport, ROI +9.41u; but this week 2-6 (25.0%)
on 8 legs, -4.19u — the best sport had its worst week. NFL away 19-10 (65.5%, n=30),
trailing-20 12-8 (60.0%). NFL totals 20-11 (64.5%, n=31), trailing-20 11-9 (55.0%)
— exactly at the line. NFL home 6-14 (30.0%, n=21) — unchanged, the drag. |
NHL 54-46 (54.0%, n=101), ROI +0.63u — the only non-NFL sport above breakeven at scale;
this week 3-4 (42.9%). NHL staked legs 13-12 (52.0%, -0.03u) — breakeven. |
CFB 42-46 (47.7%, n=89) + NCAAF 2-6 (25.0%, n=8) = combined 44-52 (45.8%, n=97),
ROI -12.13u combined; this week CFB 12-15 (44.4%) on 27 legs, -4.81u. |
NBA 31-44 (41.3%, n=75), ROI -10.21u — suspended; its 5 pending 11/16 legs settled
4-1 (+5.35u) under the old rule, which changes nothing at n=75. |
MLB 20-30 (40.0%, n=50), ROI -11.56u — worst sport at scale, unchanged (no MLB in season). |
WNBA 6-8 (42.9%, n=14).

ROI by sport (flat 1u singles): NFL +9.41u, NHL +0.63u, WNBA -1.56u, CFB -7.99u,
NCAAF -4.14u, NBA -10.21u, MLB -11.56u (worst).

Non-NFL combined trailing-20: 7-13 (35.0%) with CLV 1b/1l/3p and 15 missing —
the blanket re-open condition fails on both legs, so no blanket re-open.

## Legs by market / home-away

Moneyline 97-93 (51.1%, n=190) best; spread 54-63 (46.2%, n=120);
totals 50-59 (45.9%, n=110) worst. This week: moneyline 5-2, spread 4-6,
totals 12-18 (40.0%) on 30 legs — a totals-heavy week that dragged the week down.
Home/away (sides only): away 86-80 (51.8%, n=167) vs home 64-76 (45.7%, n=142)
— split persists; home 6% bar stays.

## Calibration (logged confidence; haircut in force since 10/26 for raw ≥60)

| bucket | n | stated | actual | gap |
|---|---|---|---|---|
| <50 | 73 | 42.2% | 48.6% | -6.4pp (dogs conservative-or-better — fine) |
| 50-59 | 288 | 55.2% | 47.7% | +7.5pp (widened from +6.2pp — still above the 5pp bar) |
| 60-69 | 50 | 63.5% | 42.0% | +21.5pp — haircut STAYS (re-audit due today, 11/23) |
| 70+ | 9 | 73.1% | 100.0% | -26.9pp (tiny n) |

This week's subset (settled ≥11/17): 60-69 bucket 2-1 (66.7%, n=3) — third
positive subset since reinstatement, still n=3, preliminary; it does not move
the full-sample verdict. Next re-audit 11/30.

## CLV (corrected spread semantics)

Overall: beat 69 / lost 49 / push 117 / missing 185 (44.0% missing) — 58.5%
excl pushes, down from 59.3%. This week: beat 5 / lost 5 / push 11 / missing 26
(55% missing — capture BROKE again, one week after the first clean week ever).
The regression is concentrated in the paper tier and in CFB: non-NFL legs this week
are 25-of-39 missing closes. Ninth flag on the capture rule; the 11/02 rule-4 gate
re-arms (no new card for a sport until that sport's prior closes are backfilled
or each missing close is flagged with its source documented as unavailable).
Process note: the 11/16 clean week was not a durable fix — the sweep needs a
checklist step, not a one-off effort.

## Approach vs approach (flat 1u singles)

model-value n=333, 161-169 (48.8%), CLV 60%, ROI -17.77u — the workhorse is now
below breakeven at scale; it was again the ONLY approach logged this week (47/47).
situational n=36, 16-19 (45.7%), CLV 60% — no new legs this week; dual trigger
still not met (trailing-20 hit 47.4% ≤50% met, CLV 75% not <50%). line-movement
n=13, 5-8 (38.5%), CLV 0% — failing both metrics but still n=13 <20, no new legs.
model-edge n=15, 7-8 (46.7%), CLV 71% — mixed, preliminary. brand-tax fade
(approach field) n=9, 6-3 (66.7%), ROI +6.40u — preliminary, best ROI.
fpi-chalk 0-3 stays demoted. dip-buy n=1, no verdict (tenth week). Multi-angle
legs 9-7 (56.2%, n=16) — preliminary; this week 2-4 (33.3%), which does not
rescue the 8.0-11.9% band (see below).

## Claimed edge bands (numeric-aware parser)

below-4%: 53-45 (54.1%, n=100) — still the best eligible band. 4.0-5.9%: 27-26
(50.9%, n=54). 6.0-7.9%: 45-41 (52.3%, n=87). 8.0%+: 60-82 (42.3%, n=142) —
the worst eligible band; 8.0-11.9% sub-band 42-57 (42.4%, n=99, eligible),
this week 13-13 (50.0%); 12%+ is 18-25 (41.9%, n=43, eligible) — the worst
band in the ledger, and the only band with no multi-angle requirement on it.
The inversion persists at every level: the more edge the model claims, the
worse the leg hits.

Inside the slice, the inversion is now a third consecutive observation:
slice-qualified legs by claimed edge — below-4% 12-3 (80.0%, n=15), 4-5.9%
12-5 (70.6%, n=17), 6-7.9% 4-5 (44.4%, n=10), 8-11.9% 3-4 (42.9%, n=7),
12%+ 1-1 (50.0%, n=2). Bands are still under n=20 each, so the pre-committed
check (n≥20 per band → stop ranking slice legs by claimed edge) has NOT fired
yet — below-4% is at 15, 4-5.9% at 17. It is one good week from firing.

## Brand tax (sides only)

Backing marquee 5-6 (45.5%, n=11); fading marquee 20-16 (55.6%, n=36,
eligible) — the fade lean is supported at the 20-leg bar but weakening (was
57.1% at n=35, 62.5% at n=24). Fade/back rules stand.

## Stack-rank dogfood (Sven's 10/7 goal: 80%)

Slice-first dogfood (11/16 rule 2 — the dogfood set is the top-5 of the
slice-first ordering, i.e. the staked set on staking days): staked legs 29-37
(43.9%, n=66), trailing-20 8-12 (40.0%) vs the 80% goal — UNDER the 60%
structural line for the second straight review, and the daily average is 40.9%
over 24 days. The old global-rank series stays frozen at 72-78 (11/16).
Qualified=true: 106-123 (46.3%, n=229) vs qualified=false: 60-54 (52.6%,
n=117) — the binary-bar signal is still inverted on the full sample, and the
qualified trailing-20 is now 6-14 (30.0%), far under the 65% guardrail from the
10/12 rule-2 re-audit. The staked subset keeps underperforming the slice's
paper record (65.0%): NFL staked legs are 11-16 (40.7%, -6.84u) while the
slice itself is 39-21. The staked set is chosen by ranking slice legs by
claimed edge — the signal the ledger keeps showing is inverted — which is the
mechanism. The slice-edge-band check at n≥20 per band (due any week now) is
the adjudicator; until it fires, the shrink in rule 1 is the brake.

## Best slice

Slice-qualified (NFL away sides + NFL totals): 39-21 (65.0%, n=61),
trailing-20 9-11 (45.0%) — UNDER the 55% shrink trigger in 11/02 rule 1;
the staked set shrinks to max 3 (see rule 1). NFL overall trailing-20 10-10
(50.0%) remains under the old 55% line, but that concentration rule was
already replaced by the slices. Staked slice legs (NFL slices + NHL): the
staked subset still trails the slice's paper record (see dogfood above).

## Tickets

Classic tiers unchanged (no classic tickets since 10/06): steady 2-3 (-1.67u),
balanced 1-13 (-10.35u), lottery 0-11 (-11.00u, suspended), single 1-0 (+0.71u),
single-lean 1-1 (-0.13u); all -22.43u over 33. Uncapped-tier staked legs @1u
singles: 29-37 (43.9%, -10.11u); this week 5-8 (38.5%, -3.49u) — NFL 2-5,
NHL 3-3. Per-day NHL staked caps respected (Nov 18: 1, Nov 20: 2, Nov 22: 2,
Nov 23: 1).

## Props discovery (prop-ledger, never merged into v3)

Settled prop legs: 120 (71-49, 59.2%); this week 7 settled, 6-1 (85.7%).
No graduations, no kills. The two patterns at 2-0 ("TE yardage under vs elite
pass rush", "workhorse-RB rushing over vs light box") got no new legs — still
one instance short. Already graduated, unchanged: "star-RB vs elite run D"
3-0 (n=3, no new legs) and "efficient-RB vs soft-front overs" 2-1 (n=3, no
new legs). Already killed, re-flagged by the script on historical legs (NOT a
new kill): "struggling-QB passing under vs elite pass D" 1-3 (25.0%, n=4).
Pattern hygiene still failing: 64 of 120 props carry NO repeatable_pattern
(includes 12 "parlay set leg (ATS)" at 4-8 and 12 "(ML)" at 9-3 — the
user-requested parlay sets, which are logged but not pattern-tagged).
Sven's own legs in the v3 ledger: none newly settled this week (the three
ticket-level entries are unchanged since 10/28); nothing re-scored here.

## Pending (excluded from all stats above)

1 leg pending: 2026-11-23 NFL CIN @ WAS Under 54.5, staked=True (MNF tonight).
