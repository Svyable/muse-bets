# Weekly review 2026-10-19 — full numbers

Scope: 93 settled v3-schema entries; 217 unique settled legs (109-104, 51.2%, pushes excluded). 3 entries skipped silently (Sven's off-schema tickets). Dedupe: one count per unique (date, matchup, pick). Ticket stats NOT deduped. Flat 1u. Script: hidden_files/weekly_review_2026_10_19.py. First review under the 10/15 uncap (card = every leg clearing its bar; below-bar legs no longer logged, so qualified=false is frozen legacy data).

## Headline

The uncapped card's first week: staked legs 5-6 (45.5%), -1.05u @1u this week — but the full uncapped run is 15-11 (57.7%), +4.19u. The week's damage is concentrated where the ledger already said it would be: non-NFL legs at 4-6% claimed edge are a coin flip (4.0-5.9% band: 21-20, 51.2%), while NFL keeps validating its 4% bar (35-19, 64.8%, trailing-20 68.4%). Two pre-committed triggers fired: the dogfood trailing-20 top-5 (10-10, 50.0%) is under the 60% structural-change line, and the qualified trailing-20 (10-10, 50.0%) is under the 65% guardrail from the 10/12 rule-2 re-audit. Both point to the same fix: a tighter edge bar for the staked set. CLV 54.2% excl pushes (down from 55.1%) — still positive, but 48% of legs have no closing data: fourth straight flag on the capture rule. Props: the struggling-QB passing-under pattern hits the kill line (1-3) and is dead.

## Legs by sport

NFL 35-19 (64.8%, n=56) — best, stronger than 10/12's 30-18. Eligible. | NHL 29-24 (54.7%, n=54) — crossed 50, eligible and positive. | MLB 20-29 (40.8%, n=49) — ONE leg short of the 50-leg cut trigger (was set: reach 50 under 45% → 6% bar). | CFB+NCAAF combined 19-24 (44.2%, n=44) — data-hygiene note: the sport label split between "CFB" and "NCAAF" this week; normalize to CFB going forward. | WNBA 6-8 (42.9%, n=14) — preliminary, now under the universal 6% bar.

## Legs by market / home-away

Moneyline 44-38 (53.7%) best; spread 35-31 (53.0%); totals 30-35 (46.2%, n=66) — the 10/12 watch condition was "50+ legs under 45% → 6% bar": NOT met (46.2% > 45%), but rule 1 below gives non-NFL totals the 6% bar anyway. Home/away (sides only): away 51-35 (59.3%, n=87) vs home 28-34 (45.2%, n=64) — the split persists; home 6% bar stays.

## Calibration (logged confidence = raw model since the 10/12 haircut lift)

| bucket | n | stated | actual | gap |
|---|---|---|---|---|
| <50 | 46 | 44.0% | 55.6% | -11.5pp (dogs conservative-or-better — fine) |
| 50-59 | 151 | 54.7% | 50.7% | +4.0pp — calibrated, haircut stays lifted |
| 60-69 | 19 | 62.9% | 42.1% | +20.8pp — ugly, but n=19 is ONE leg short of the n=20 guardrail bar |
| 70+ | 1 | — | — | — |

The top-end collapse is real data: raw 60-69% legs hit 42%. Legs with 7-11% claimed edges lost this week (Rangers ML +11.4pp edge, ECU -4.5, Memphis -7). The edge estimates are inflated at the top, not just the middle.

## CLV: 32 beat / 27 lost / 54 push / 104 missing — 54.2% excl pushes

Down from 55.1%. This week: 5b/5l/14p, 29 missing of 53. **104 of 217 legs (48%) have no closing data** — the 9/28 capture rule is violated for the fourth straight review. Flagged, not rewritten: the morning settle pass must backfill every close or flag the leg. Process is neutral-to-positive on the evaluable half, dark on the rest.

## Approach vs approach (flat 1u singles)

| approach | n | W-L | CLV excl-push | roi |
|---|---|---|---|---|
| model-value | 131 | 69-59 (53.9%) | 55% | +4.66u — the workhorse, eligible |
| situational | 36 | 16-19 (45.7%) | 60% | -5.82u — eligible, failing results, passing process |
| model-edge | 15 | 7-8 (46.7%) | 71% | -2.38u — preliminary, mixed |
| line-movement | 12 | 5-7 (41.7%) | 0% | -2.32u — failing BOTH, still preliminary |
| brand-tax fade | 9 | 6-3 (66.7%) | 60% | +6.40u — preliminary, best ROI |
| fpi-value | 6 | 3-3 | n/a | -0.27u |
| fpi-chalk | 3 | 0-3 | n/a | -3.00u (stays demoted) |
| dip-buy | 1 | 0-1 | n/a | fifth week, no verdict — effectively dormant |

Claimed-edge bands: below-4% (legacy fills) 39-33 (54.2%); 4.0-5.9% 21-20 (51.2%); 6.0-7.9% 9-7 (56.2%); 8.0%+ 4-4. The 4% bar admits coin flips; 6%+ is where the hit rate clears breakeven.

**Situational dual-trigger re-audit** (10/12: demote if trailing-20 hit ≤50% AND CLV <50%): trailing-20 is 9-10 (47.4%) — condition 1 met; CLV 3b/1l = 75% excl pushes — condition 2 NOT met. No demotion; same trigger re-armed next week.

**Line-movement**: failing both metrics (41.7% hit, 0b/5l CLV) but n=12 <20 — preliminary; reaching 20 still failing both → demoted (fpi-chalk treatment).

## Brand-tax (sides only)

Backing marquee 3-4 (42.9%, n=7); fading marquee 13-4 (76.5%, n=17) — preliminary (<20) but directionally strong for the fourth week. Fade/back rules stand. Brand-tax fade as an approach: 6-3, +6.40u, best ROI in the ledger (n=9).

## Stack-rank dogfood

Ranks 1-5: 26-23 (53.1%, n=49) vs ranks 6-10: 22-16 (57.9%, n=40) — **the fine rank ordering still doesn't separate winners; the 6-10 bucket outhits 1-5.** Daily-average top-5: 52.1% over 11 days. **Trailing-20 top-5: 10-10 (50.0%) vs the 80% goal — under the 60% structural-change trigger → structural change required.** Qualified=true 14-12 (53.8%, n=26) vs qualified=false 60-54 (52.6%, n=117) — the 10/12 binary-bar signal (64.3% vs 51.4%) collapsed. **Qualified trailing-20: 10-10 (50.0%) — under the 65% guardrail from the 10/12 rule-2 re-audit → the staked bar rises to 6%.** The chosen structural change is the tighter edge bar (rule 1); "fewer forced ranks" is moot (never forced since 10/12); rank-by-edge stays the ordering, the bar does the work.

## Best-slice (NFL concentration)

NFL overall 35-19 (64.8%, n=56); trailing-20 13-6 (68.4%) — far above the 55% re-open trigger. **Concentration stays.** NFL away: 15-5 (75.0%, n=21), trailing-20 15-4 (78.9%) — the sharpest corner of the ledger, still preliminary but widening. No new best slice is nominated: nothing else clears 55% at n≥20.

## Props discovery (prop-ledger, never merged into v3)

43 settled legs, 25-18 (58.1%); this week 26, 14-12 (53.8%). **KILL: 'struggling-QB passing under vs elite pass D' — 1-3 (25.0%, n=4), under the 40% kill line at 3+ instances.** No graduations: no other pattern has 3+ instances (the pattern list has diffused to 30+ one-off labels — see rule 3). Sven's own (off-schema): sven-8-leg 0-1, sven-prop-7-leg 1-0 (his pick, the north star), sven-2-pick 0-1.
