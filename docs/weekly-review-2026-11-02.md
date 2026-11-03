# Weekly review 2026-11-02 — full numbers

Scope: 107 settled v3-schema entries; 283 unique settled legs (137-142, 49.1%, pushes excluded).
3 entries skipped silently (off-schema). Dedupe: one count per unique (date, matchup, pick).
Ticket stats NOT deduped. Flat 1u. Script: hidden_files/weekly_review_2026_11_02.py
(adapted from the 10/26 script; week window = settled ≥ 2026-10-27).
CORRECTION vs prior scripts: the old `claimed_edge` parser required a "pp"/"%" suffix and
silently dropped numeric edge values (112 legs in the ledger carry a bare float edge).
All edge-band figures below use the numeric-aware parser; the old 8%+ band (4-4) was an
artifact of that drop. Corrected 8%+ band: 22-31 (41.5%, n=53).

## Headline

A flat week on legs, a bad week for the staked set's premise. 39 legs settled since 10/27,
20-19 (51.3%), all model-value, ROI -2.77u at flat 1u singles. The week's only post-rule
staked leg to settle — Vikings ML (+165) at Detroit, the sole Nov 1 staked leg — lost,
though it beat the close (+153). The two other staked legs settled this week (Oct 27 NHL
1-1) belong to the Oct 26 card, logged before the 10/26 NFL-only rule took effect, so
they are transition legs, not a rule violation. All staked legs now 20-24 (45.5%, -4.41u);
NFL staked legs 7-9 (43.8%, -2.84u) — still under 50%, firing the 10/26 caveat that the
staked set itself gets re-examined at this review. Two pre-committed triggers fire:
NFL overall trailing-20 at 50.0% is UNDER the 55% concentration re-open line, and the
dogfood trailing-20 top-5 at 45.0% is under the 60% structural-change line (second week
running). Non-NFL trailing-20 hit rate recovered to 65.0% (13-7), but its CLV is
0-for-20 evaluable (all 20 missing closes), so the 10/26 re-open condition (hit ≥50%
AND CLV ≥50%) is NOT met — non-NFL stays paper-only. CLV overall is 56.3% excl pushes,
but capture collapsed this week: 33 of 39 legs (84.6%) missing closes, sixth straight
flag, and the paper-tier capture is now the binding constraint on every CLV claim.

## Legs by sport

NFL 36-24 (60.0%, n=62) — still best sport by full sample, but trailing-20 10-10 (50.0%)
is under the 55% re-open trigger. NFL away 15-7 (68.2%, n=23), trailing-20 13-6 (68.4%).
NFL home 5-12 (29.4%, n=18) is the drag. NFL totals 15-5 (75.0%, n=20) — the strongest
pocket in the ledger at the 20-leg bar, and it does not overlap NFL away (totals carry
no home/away). | NHL 41-37 (52.6%, n=79), trailing-20 9-11 (45.0%). |
CFB 25-25 (50.0%, n=51) + NCAAF 2-6 (25.0%, n=8) = combined 27-31 (46.6%, n=59, eligible,
below breakeven) — the label split is STILL not normalized, third flag. CFB trailing-20
11-8 (57.9%). | MLB 20-30 (40.0%, n=50) — stays paper-only; MLB totals 3-13 (18.8%,
n=16) remains the worst corner. | NBA 7-12 (36.8%, n=19) — one leg short of the n=20
entry bar; stays a watched newcomer, never a forced staked leg. | WNBA 6-8 (42.9%, n=14).

Non-NFL combined: 101-118 (46.1%, n=221, eligible) — below breakeven on the full sample;
trailing-20 13-7 (65.0%) on results, CLV unevaluable (20/20 missing).

## Legs by market / home-away

Moneyline 72-67 (51.8%, n=139) best; spread 35-38 (47.9%, n=76); totals 30-37 (44.8%,
n=68) — totals are a tale of two sports (NFL totals 15-5 vs MLB totals 3-13).
Home/away (sides only): away 61-53 (53.5%, n=115) vs home 45-52 (46.4%, n=99) — split
narrowed from 43.6/55.3 but persists; home 6% bar stays.

## Calibration (logged confidence; haircut reinstated 10/26 for raw ≥60)

| bucket | n | stated | actual | gap |
|---|---|---|---|---|
| <50 | 57 | 43.6% | 53.6% | -9.9pp (dogs conservative-or-better — fine) |
| 50-59 | 181 | 54.9% | 48.9% | +6.0pp |
| 60-69 | 38 | 63.7% | 34.2% | +29.5pp — worse than 10/26 (+24.1pp); haircut stays |
| 70+ | 7 | 72.0% | 100.0% | -28.0pp (tiny n) |

This week's subset (settled ≥10/27): 50-59 bucket 10-9 (52.6%, stated 55.5% — roughly
calibrated); 60-69 bucket 0-5 (stated 64.8%, n=5, preliminary but corroborating);
70+ bucket 6-0. The 10/26 haircut re-audit is due 11/09, not today — no lift.

## CLV (corrected spread semantics)

Overall: beat 40 / lost 31 / push 63 / missing 149 (52.7% missing) — 56.3% excl pushes,
up from 53.7%, on a shrinking evaluable base. This week: beat 4 / lost 0 / push 2 /
missing 33 (84.6% missing). By sport this week: CFB 11/11 missing, NBA 11/12 missing,
NHL 11/15 missing, NFL 1/1 beat (Vikings). Staked legs are the exception: 3/3 settled
this week carry closes, and only 7 of 44 all-time staked legs lack one — the gate held
where it was applied. The failure is the paper tier. Sixth straight flag.

## Approach vs approach (flat 1u singles)

model-value n=196, 97-96 (50.3%), CLV 58%, ROI -7.74u — the workhorse is a coin flip
at scale; this week it was the ONLY approach logged (39/39 legs, 20-19, -2.77u).
situational n=36, 16-19 (45.7%), CLV 60% — no new legs this week; dual trigger still
not met (trailing-20 hit 47.4% ≤50% met, CLV 75% not <50%). line-movement n=13, 5-8
(38.5%), CLV 0% — failing both metrics but still n=13 <20, no new legs. model-edge
n=15, 7-8 (46.7%), CLV 71% — mixed, preliminary. brand-tax fade (approach field)
n=9, 6-3 (66.7%), ROI +6.40u — preliminary, best ROI. fpi-chalk 0-3 stays demoted.
dip-buy n=1, no verdict (seventh week). Multi-angle legs (approach contains a "+"
combination) 7-3 (70.0%, n=10) — preliminary, unchanged this week.

## Claimed edge bands (numeric-aware parser — see correction note)

below-4%: 53-45 (54.1%, n=100) — outhits every band except the tiny 12%+ tail.
4.0-5.9%: 24-24 (50.0%, n=49). 6.0-7.9%: 22-21 (51.2%, n=44).
8.0%+: 22-31 (41.5%, n=53, eligible) — the worst eligible band, driven by the
8.0-11.9% sub-band at 14-25 (35.9%, n=39, eligible); 12%+ is 8-6 (57.1%, n=14,
preliminary). This week: 6.0-7.9% went 8-3 (72.7%) while 8.0-11.9% went 8-12 (40.0%).
Claimed edge does not rank winners — it inverts in the 8-12% range. Edge-ranked
staking on its own is not a defensible staked-set rule.

## Brand tax (sides only)

Backing marquee 3-6 (33.3%, n=9); fading marquee 14-8 (63.6%, n=22, eligible) —
the fade lean is now supported at the 20-leg bar on sides. Fade/back rules stand.

## Stack-rank dogfood (Sven's 10/7 goal: 80%)

Ranks 1-5: 42-53 (44.2%, n=95) vs ranks 6-10: 28-22 (56.0%, n=52) — ranking is still
inverted; the fine rank does not separate winners. Daily average hit rate (ranks 1-5):
38.9% over 24 days. Trailing-20 top-5: 9-11 (45.0%) vs the 80% goal — under the 60%
structural-change line for the second week running. Qualified=true: 42-50 (45.7%,
n=92) vs qualified=false: 60-54 (52.6%, n=117) — the binary-bar signal is still
inverted on the full sample, though qualified trailing-20 improved to 12-8 (60.0%),
still under the 65% guardrail from the 10/12 rule-2 re-audit.

## Best slice

NFL overall trailing-20 10-10 (50.0%) is UNDER the 55% re-open trigger — the
concentration rule re-opens. Nominated replacement concentration: NFL away sides
(15-7, 68.2%, trailing-20 68.4%) plus NFL totals (15-5, 75.0%, n=20) — the two pockets
holding up while NFL home (5-12, 29.4%) drags the overall slice down. See rule 1.

## Tickets

Classic tiers unchanged (no classic tickets since 10/06): steady 2-3 (-1.67u),
balanced 1-13 (-10.35u), lottery 0-11 (-11.00u, suspended), single 1-0 (+0.71u),
single-lean 1-1 (-0.13u); all -22.43u over 33. Uncapped-tier staked legs @1u singles:
20-24 (45.5%, -4.41u); this week 1-2 (33.3%, -0.64u) counting the two Oct 26-card
transition legs — the only post-rule staked leg to settle (Vikings) lost.

## Props discovery (prop-ledger, never merged into v3)

Settled prop legs: 104 (57-47, 54.8%); this week 46 (23-23, 50.0%).
By prop_type, the only types at n≥10 are player prop 18-18 (50.0%, n=36),
parlay set leg (ML) 9-3 (75.0%, n=12), parlay set leg (ATS) 4-8 (33.3%, n=12),
player passing yards 5-5 (50.0%, n=10). By repeatable_pattern:
- GRADUATES (new): "efficient-RB vs soft-front overs" 2-1 (66.7%, n=3) — Bucky Irving
  over 55.5 (win, 10/08), Jaylen Warren over 63.5 (win, 10/25), Josh Jacobs over 77.5
  rush+rec (loss, 10/29). Meets the 3+ / 65%+ bar exactly; provisional, re-audit at n=6.
- Already killed, re-flagged by the script on historical legs (NOT a new kill):
  "struggling-QB passing under vs elite pass D" 1-3 (25.0%, n=4).
- No other pattern at 3+ instances. Pattern hygiene still failing: 45 of 46 props
  settled this week carry NO repeatable_pattern (51 of 104 overall) — the 10/19
  consolidation rule is not producing labelled legs, which caps discovery at n=3
  graduations like this one.
- Sven's own legs in the v3 ledger: none newly settled this week (the 10/26 MNF
  backfill was already counted 10/28); nothing re-scored here.

## Pending (excluded from all stats above)

7 legs pending for 2026-11-02, including the staked MNF leg Seattle Seahawks ML
(CHI @ SEA) — settles tomorrow's review window, not this one.
