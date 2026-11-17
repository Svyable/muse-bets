# Weekly review 2026-11-16 — full numbers

Scope: 121 settled v3-schema entries; 373 unique settled legs (180-189, 48.8%, pushes excluded).
3 entries skipped silently (off-schema — all three are Sven's own ticket-level entries, unchanged since 10/28).
Dedupe: one count per unique (date, matchup, pick).
Ticket stats NOT deduped. Flat 1u. Script: hidden_files/weekly_review_2026_11_16.py
(adapted from the 11/09 script; week window = settled ≥ 2026-11-10).

## Headline

A losing week driven by one sport: 67 legs settled since 11/10, 30-37 (44.8%),
and 40 of those 67 legs were NBA at 15-25 (37.5%). Staked legs went 3-4 (-1.83u)
on 7 settled legs: 5 NHL (2-3) and 2 NFL (1-1 — Chiefs ML win, Texans -4.5 loss,
the first slate under the 11/13 user-directed scale-up; the totals slice again had
zero staked legs). All staked legs now 24-29 (45.3%, -6.62u). The week's real news
is process, not results: CLV capture is finally clean — 17b/10l/40p this week with
ZERO missing closes, the first clean week in the ledger's history (eighth flag
resolved, see below). Two pre-committed triggers fire: the dogfood structural-change
trigger (trailing-20 top-5 at 50.0%, under the 60% line) and the NBA cut bar
(27-43, 38.6% at n=70 — eligible). Both NHL re-open close triggers PASS, so the
scoped NHL re-open stays open.

## Legs by sport

NFL 44-29 (60.3%, n=75) — still best sport; trailing-20 9-11 (45.0%), under the
old 55% line, but that concentration rule was already replaced by the slices.
NFL away 19-8 (70.4%, n=28), trailing-20 13-6 (68.4%). NFL home 6-14 (30.0%,
n=21) — unchanged, the drag. NFL totals 18-7 (72.0%, n=25), trailing-20 14-6
(70.0%) — still the strongest pocket. | NHL 51-42 (54.8%, n=94), trailing-20
12-8 (60.0%) — the only non-NFL sport above breakeven at scale; ROI +1.93u.
NHL moneyline 39-32 (54.9%, n=71), totals 9-9 (50.0%, n=19), spread 3-1.
NHL this week 5-3. | NBA 27-43 (38.6%, n=70) — worst sport at scale, and it got
worse: trailing-20 7-13 (35.0%), this week 15-25 on 40 legs. NBA moneyline
17-31 (35.4%, n=48), spread 10-12 (45.5%, n=22), no totals logged. Every NBA
edge band fails: 6-7.9% 6-11 (35.3%), 8-11.9% 8-17 (32.0%), 12%+ 13-15 (46.4%).
| CFB 30-31 (49.2%, n=62) + NCAAF 2-6 (25.0%, n=8) = combined 32-37 (46.4%,
n=70), trailing-20 11-9 (55.0%) — the label split is STILL not normalized,
fifth flag. | MLB 20-30 (40.0%, n=50), unchanged (no MLB in season). |
WNBA 6-8 (42.9%, n=14).

ROI by sport (flat 1u singles): NFL +13.60u, NHL +1.93u, WNBA -1.56u,
CFB -3.19u, NCAAF -4.14u, MLB -11.56u, NBA -15.56u (worst).

Non-NFL combined trailing-20: 8-12 (40.0%) with CLV 5b/4l/11p — the old blanket
re-open condition fails, so no blanket re-open; only the scoped NHL slice stays.

## Legs by market / home-away

Moneyline 92-91 (50.3%, n=183) best; spread 50-57 (46.7%, n=110);
totals 38-41 (48.1%, n=80). Home/away (sides only): away 81-75 (51.9%, n=157)
vs home 60-73 (45.1%, n=135) — split persists but narrowed; home 6% bar stays.

## Calibration (logged confidence; haircut in force since 10/26 for raw ≥60)

| bucket | n | stated | actual | gap |
|---|---|---|---|---|
| <50 | 72 | 42.4% | 47.9% | -5.5pp (dogs conservative-or-better — fine) |
| 50-59 | 246 | 55.1% | 49.0% | +6.2pp (still above the 5pp bar) |
| 60-69 | 47 | 63.8% | 40.4% | +23.3pp — haircut stays (re-audit due 11/23, not today) |
| 70+ | 8 | 72.4% | 100.0% | -27.6pp (tiny n) |

This week's subset (settled ≥11/10): 60-69 bucket 4-2 (66.7%, n=6) — first
positive subset since the haircut was reinstated, but n=6, preliminary; it does
not move the full-sample verdict. Next re-audit 11/23.

## CLV (corrected spread semantics)

Overall: beat 64 / lost 44 / push 106 / missing 159 (42.6% missing) — 59.3%
excl pushes, up from 58.0%. This week: beat 17 / lost 10 / push 40 / missing 0
(0% missing — first clean week ever). The 9/28 capture rule is finally satisfied
and the 11/02 rule-4 gate is met for every sport this week. Eighth flag resolved:
no new rule, the old one is now being enforced — the morning/evening sweep gets
the credit, and the review stops flagging it until it breaks again.

## Approach vs approach (flat 1u singles)

model-value n=286, 140-143 (49.5%), CLV 61%, ROI -12.82u — the workhorse is a
coin flip at scale; trailing-20 11-9 (55.0%). This week it was again the ONLY
approach logged (67/67 legs, 30-37). situational n=36, 16-19 (45.7%), CLV 60% —
no new legs this week; dual trigger still not met (trailing-20 hit 47.4% ≤50%
met, CLV 75% not <50%). line-movement n=13, 5-8 (38.5%), CLV 0% — failing both
metrics but still n=13 <20, no new legs. model-edge n=15, 7-8 (46.7%), CLV 71% —
mixed, preliminary. brand-tax fade (approach field) n=9, 6-3 (66.7%), ROI
+6.40u — preliminary, best ROI. fpi-chalk 0-3 stays demoted. dip-buy n=1,
no verdict (ninth week). Multi-angle legs 7-3 (70.0%, n=10) — preliminary,
unchanged this week (no new multi-angle legs).

## Claimed edge bands (numeric-aware parser)

below-4%: 53-45 (54.1%, n=100) — still outhits every band except the tiny 12%+
tail. 4.0-5.9%: 26-25 (51.0%, n=52). 6.0-7.9%: 38-33 (53.5%, n=72).
8.0%+: 47-65 (42.0%, n=112) — the worst eligible band; 8.0-11.9% sub-band
29-44 (39.7%, n=73, eligible), this week 10-12 (45.5%); 12%+ is 18-21 (46.2%,
n=39, preliminary). The inversion in the 8-12% range persists and deepened —
rule 2 (multi-angle requirement for that band) stands.

Non-NFL by edge band: below-4% 41-41 (50.0%, n=84), 4-5.9% 14-19 (42.4%),
6-7.9% 33-28 (54.1%, n=61), 8-11.9% 25-39 (39.1%, n=64), 12%+ 17-20 (45.9%).
Even inside the best slice the edge estimates are inverted: slice-qualified legs
by claimed edge — below-4% 12-3 (80.0%, n=15), 4-5.9% 11-4 (73.3%, n=15),
6-7.9% 4-3 (57.1%, n=8), 8-11.9% 2-2 (50.0%, n=4), 12%+ 1-0. Hit rate falls
monotonically as claimed edge rises. Bands are under n=20 each, so this is a
preliminary observation, not a rule — but it is the second independent place the
edge estimates invert (the first was the global 8-12% band). Pre-committed check:
if the slice's below-4% vs 8%+ gap persists at n≥20 per band, the staked set
stops ranking slice legs by claimed edge.

## Brand tax (sides only)

Backing marquee 5-6 (45.5%, n=11); fading marquee 20-15 (57.1%, n=35,
eligible) — the fade lean is supported at the 20-leg bar but weakening (was
62.5% at n=24). Fade/back rules stand.

## Stack-rank dogfood (Sven's 10/7 goal: 80%)

Ranks 1-5: 72-78 (48.0%, n=150) vs ranks 6-10: 40-38 (51.3%, n=80) — ranking
is still inverted on the full sample. Daily average hit rate (ranks 1-5): 44.4%
over 37 days (up from 43.0% over 31). Trailing-20 top-5: 10-10 (50.0%) vs the
80% goal — UNDER the 60% structural-change line; the trigger fires (see rule 2).
Qualified=true: 85-97 (46.7%, n=182) vs qualified=false: 60-54 (52.6%, n=117)
— the binary-bar signal is still inverted on the full sample, though qualified
trailing-20 is 11-9 (55.0%), still under the 65% guardrail from the 10/12
rule-2 re-audit. The bar separates winners only inside the NFL slices, not
globally — which is exactly why staking went slice-first.

## Best slice

Slice-qualified (NFL away sides + NFL totals): 37-15 (71.2%, n=53),
trailing-20 13-7 (65.0%) — well above the 55% shrink trigger in 11/02 rule 1;
the staked set stays at max 5 slice legs per slice under the 11/13 scale-up,
never forced. NFL overall trailing-20 9-11 (45.0%) remains under the old 55%
line, but that concentration rule was already replaced by the slices.
Staked slice legs (NFL slices + NHL): 18-16 (52.9%, n=34) — the staked subset
still trails the slice's paper record (71.2%), because the staked subset is
dominated by the newer, weaker NHL slice legs (NHL staked 10-9, +0.27u).

## Tickets

Classic tiers unchanged (no classic tickets since 10/06): steady 2-3 (-1.67u),
balanced 1-13 (-10.35u), lottery 0-11 (-11.00u, suspended), single 1-0 (+0.71u),
single-lean 1-1 (-0.13u); all -22.43u over 33. Uncapped-tier staked legs @1u
singles: 24-29 (45.3%, -6.62u); this week 3-4 (42.9%, -1.83u) — NHL 2-3,
NFL 1-1. Per-day NHL staked caps respected (Nov 11: 2, Nov 13: 2, Nov 15: 1
alongside 2 NFL).

## Props discovery (prop-ledger, never merged into v3)

Settled prop legs: 113 (65-48, 57.5%); this week only 1 settled (1-0, 100.0%).
No graduations, no kills. Two patterns sit at 2-0, one instance short of the
graduation bar: "TE yardage under vs elite pass rush" and "workhorse-RB rushing
over vs light box". Already graduated, unchanged: "star-RB vs elite run D" 3-0
(n=3, no new legs) and "efficient-RB vs soft-front overs" 2-1 (n=3, no new
legs). Already killed, re-flagged by the script on historical legs (NOT a new
kill): "struggling-QB passing under vs elite pass D" 1-3 (25.0%, n=4).
Pattern hygiene still failing: 57 of 113 props carry NO repeatable_pattern, and
the lane went nearly silent this week (1 settled leg) — discovery is starved of
volume, not just labels.
Sven's own legs in the v3 ledger: none newly settled this week (the three
ticket-level entries are unchanged since 10/28); nothing re-scored here.

## Pending (excluded from all stats above)

5 legs pending for 2026-11-16, all paper (staked=False), all NBA: Suns +10.5,
PHI/BKN Under 225.5, Heat ML, Suns ML, CHI/CLE Under 242.5. These were logged
before today's NBA suspension and settle under the old rule.
