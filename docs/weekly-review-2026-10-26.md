# Weekly review 2026-10-26 — full numbers

Scope: 100 settled v3-schema entries; 244 unique settled legs (117-123, 48.8%, pushes excluded). 3 entries skipped silently (Sven's off-schema tickets). Dedupe: one count per unique (date, matchup, pick). Ticket stats NOT deduped. Flat 1u. Script: hidden_files/weekly_review_2026_10_26.py (adapted from the 10/19 script; week window = settled ≥ 2026-10-20). First review under the 10/19 rules (6% non-NFL staked bar, NBA entry rule, props pattern consolidation).

## Headline

A brutal week: 27 legs settled since 10/20, 8-19 (29.6%). Staked legs went 4-11 (26.7%), -7.96u @1u this week — wiping out the uncapped run's +4.19u and leaving all staked legs at 19-22 (46.3%), -3.77u. The 6% non-NFL bar was enforced (zero sub-6% non-NFL legs logged post-10/19) and still went 7-15 for non-NFL — the bar didn't fail on enforcement, it failed on the underlying edge estimates: the 60-69 confidence bucket now hits 39.4% (n=33) and the claimed-edge bands don't separate winners at any level (8%+ is 4-4). Two pre-committed triggers fire: the 60-69 calibration guardrail (n=33, gap +24.1pp → haircut reinstated) and the dogfood structural-change trigger (trailing-20 top-5 at 30.0%). CLV stays positive (53.7% excl pushes) but 47.6% of legs have no closing data — fifth straight flag. Props stay the best lane: 34-24 (58.6%), this week 9-6 (60.0%).

## Legs by sport

NFL 36-23 (61.0%, n=61) — best, still the only sport above breakeven at scale; trailing-20 11-9 (55.0%) — exactly AT the 55% re-open line, not under. Concentration stays, on the edge. | NHL 33-30 (52.4%, n=64) — positive, stays in the card (paper-only under rule 2). | MLB 20-30 (40.0%, n=50) — crossed 50 legs under 45%: the retired 10/19 cut trigger's condition is met, subsumed by rule 2 (paper-only). MLB totals 3-13 (18.8%, n=16) is the worst corner in the ledger. | CFB+NCAAF combined 19-28 (40.4%, n=48) — label split STILL not normalized (CFB n=40, NCAAF n=8); the 10/19 hygiene addendum was not applied. | NBA 3-4 (42.9%, n=7) — newcomer, 6% bar, no graduation (needs n≥20). | WNBA 6-8 (42.9%, n=14).

Non-NFL combined: 81-100 (44.8%, n=183) — eligible, below breakeven; trailing-20 7-13 (35.0%), CLV 4b/3l (57% excl pushes) — results failing, process passing.

## Legs by market / home-away

Moneyline 52-48 (52.0%, n=100) best; spread 35-38 (47.9%, n=76); totals 30-37 (44.8%, n=68) — the 10/12 watch condition (50+ legs under 45% → 6% bar) is now met, already covered by rule 1 for non-NFL; the totals problem is MLB-driven (NFL totals are 15-5, 75.0%, n=20). Home/away (sides only): away 52-42 (55.3%, n=95) vs home 34-44 (43.6%, n=80) — split persists; home 6% bar stays.

## Calibration (logged confidence = raw model since the 10/12 haircut lift)

| bucket | n | stated | actual | gap |
|---|---|---|---|---|
| <50 | 48 | 44.0% | 55.3% | -11.3pp (dogs conservative-or-better — fine) |
| 50-59 | 162 | 54.8% | 48.4% | +6.4pp — muddy (mixes haircut-era and raw-era legs) |
| 60-69 | 33 | 63.5% | 39.4% | +24.1pp — the guardrail fires (n>20, gap>5pp) |
| 70+ | 1 | — | — | — |

The 60-69 bucket's post-10/20 subset is 5-9 (35.7%, n=14) — still bad under raw logging. The 10/12 forensic (raw≥60 legs hitting 62.9%) has not survived contact with October: raw top-end confidence is overconfident by ~24 points.

## CLV: 36 beat / 31 lost / 61 push / 116 missing — 53.7% excl pushes

Down from 54.2%. This week: 4b/4l/7p, 12 missing of 27. **116 of 244 legs (47.6%) have no closing data** — the 9/28 capture rule is violated for the fifth straight review. Process is positive on the evaluable half, dark on the rest. Post-10/19 legs have closes on 15 of 26 — no improvement.

## Approach vs approach (flat 1u singles)

| approach | n | W-L | CLV excl-push | roi |
|---|---|---|---|---|
| model-value | 157 | 77-77 (50.0%) | 54% | -4.97u — the workhorse went to a coin flip (was 69-59, +4.66u); this week 8-17 |
| situational | 36 | 16-19 (45.7%) | 60% | -5.82u — unchanged this week (no new legs); eligible, failing results, passing process |
| model-edge | 15 | 7-8 (46.7%) | 71% | -2.38u — preliminary, mixed |
| line-movement | 13 | 5-8 (38.5%) | 0% | -3.32u — failing BOTH, still preliminary (n<20) |
| brand-tax fade | 9 | 6-3 (66.7%) | 60% | +6.40u — preliminary, best ROI; no new legs this week |
| fpi-value | 6 | 3-3 | n/a | -0.27u |
| fpi-chalk | 3 | 0-3 | n/a | -3.00u (stays demoted) |
| mild-value | 2 | 1-1 | n/a | -0.09u |
| dip-buy | 1 | 0-1 | n/a | dormant — sixth week, no verdict |
| structural | 1 | 1-0 | n/a | +0.91u |
| projection gap | 1 | 1-0 | 100% | +0.91u |

Claimed-edge bands (no separation at any level): below-4% (legacy fills) 39-33 (54.2%); 4.0-5.9% 21-20 (51.2%); 6.0-7.9% 9-7 (56.2%); 8.0%+ 4-4 (50.0%). The claimed edge is not predictive right now — the highest-edge legs hit no better than the lowest. Post-10/19 legs (all under the new bars): 8-18 (30.8%), model-value 8-17 (32.0%).

**Situational dual-trigger re-audit** (demote if trailing-20 hit ≤50% AND CLV <50%): trailing-20 is 9-10 (47.4%) — condition 1 met; CLV 3b/1l = 75% excl pushes — condition 2 NOT met. No demotion; same trigger re-armed next week.

**Line-movement**: failing both metrics (38.5% hit, 0b/5l CLV) but n=13 <20 — preliminary; reaching 20 still failing both → demoted (fpi-chalk treatment).

**Multi-angle legs** (approach contains '+'): 7-3 (70.0%, n=10) vs single-angle 110-120 (47.8%) — preliminary, directionally supports the ensemble rule; watched, not a rule (needs n≥20).

## Brand-tax (sides only)

Backing marquee 3-5 (37.5%, n=8); fading marquee 14-5 (73.7%, n=19) — one short of the 20-leg bar; fade lean stands. Brand-tax fade as an approach: 6-3, +6.40u, best ROI in the ledger (n=9).

## Stack-rank dogfood

Ranks 1-5: 32-39 (45.1%, n=71) vs ranks 6-10: 24-19 (55.8%, n=45) — **the fine rank ordering is inverted; 6-10 outhits 1-5 by 10.7pp.** Daily-average top-5: 41.1% over 17 days. **Trailing-20 top-5: 6-14 (30.0%) vs the 80% goal — far under the 60% structural-change trigger → structural change required (rule 2).** Qualified=true 22-31 (41.5%, n=53) vs qualified=false 60-54 (52.6%, n=117) — the 10/12 binary-bar signal (64.3% vs 51.4%) has inverted. **Qualified trailing-20: 7-13 (35.0%) — under the 65% guardrail.** Staked legs by sport (all time): NFL 7-8 (46.7%), NHL 7-5 (58.3%), CFB 2-3, MLB 1-3, NCAAF 0-3, WNBA 2-0. This week's staked legs by sport: NFL 1-4, NHL 3-4, CFB 0-2, MLB 0-1.

## Best-slice (NFL concentration)

NFL overall 36-23 (61.0%, n=61); trailing-20 11-9 (55.0%) — exactly AT the 55% re-open trigger, not under. **Concentration stays — but it is one loss from re-opening.** NFL away: 15-6 (71.4%, n=22), trailing-20 14-5 (73.7%) — the sharpest corner, still preliminary. No new best slice is nominated: nothing else clears 55% at n≥20 (NHL 52.4% is closest).

## Props discovery (prop-ledger, never merged into v3)

58 settled legs, 34-24 (58.6%); this week 15, 9-6 (60.0%). **No graduations, no new kills.** No pattern has 3+ settled instances except the already-killed 'struggling-QB passing under vs elite pass D' (1-3, 25%, n=4). 'volume-shooter-vs-weak-goalie' is 1-1 settled (n=2; 3 total instances incl. a no-action); 'WNBA next-woman-up usage' 1-0 settled (n=1; 3 total instances). NOTE: the script flags the `None` pattern (4-2, n=6) as "GRADUATE" — that is a script artifact; None means no pattern label, not a pattern. It does not graduate. By prop_type: 'player receiving yards' 4-0 (n=4), 'player passing yards' 5-5 (n=10), 'player prop' (generic) 10-8 (n=18). Sven's own (off-schema): sven-8-leg 0-1, sven-prop-7-leg 1-0 (his pick, the north star), sven-2-pick 0-1 — unchanged.
