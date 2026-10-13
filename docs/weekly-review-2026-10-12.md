# Weekly review 2026-10-12 — full numbers

Scope: 86 settled v3-schema entries (top-level tier + source; legs carry pick, market, odds, confidence, approach, result). 3 entries skipped silently (Sven's 9/16 8-leg, 9/17 prop 7-leg, 9/19 2-pick — user-source, legs lack odds/confidence). Dedupe: legs counted once per unique (date, matchup, pick). Ticket stats are NOT deduped. All odds @1u flat. Script: hidden_files/weekly_review_2026_10_12.py (kept in the repo for reruns).

**CLV semantics correction vs the 10/05 review.** The 10/05 doc's spread example ('Raiders +4.5 beat vs close 5.5') is economically inverted: a dog closing at a BIGGER number is a worse price for the booked bettor (money came in on the favorite — you're on the wrong side of the steam), i.e. CLV lost, not beat. Corrected semantics: dog pick beats iff booked line > closing line (favorite pick: booked numerically greater, e.g. -4.5 > -5.5); totals unchanged (over: booked < close; under: booked > close). Legs flipping verdict: Houston +7.5 (9/18), Raiders +4.5 (10/03) — both beat→lost; this-week flips: Buccaneers +8.5 (10/08), Florida State +3.5 (10/10), Dolphins +7, Titans +7, 49ers +3 (10/11 card) — all beat→lost. Pre-10/06 CLV under corrected semantics: 14b/10l/14p = 58.3% excl pushes (was reported 60.0%). The 'CLV turned positive' story survives, slightly weaker.

## Tickets @1u (classic tiers)

| tier | W-L | net | ROI |
|---|---|---|---|
| steady | 2-3 | -1.67u | -33.3% |
| balanced | 1-13 | -10.35u | -73.9% |
| lottery | 0-11 | -11.00u | -100.0% (SUSPENDED 10/05) |
| single | 1-0 | +0.71u | +71.4% |
| single-lean | 1-1 | -0.13u | -6.5% |
| **all** | | **-22.43u** | over 33 tickets |

No classic-tier tickets since 10/06 — the format is now the daily ranked card (daily-10 → daily-20). The 10/06 single-lean loss (-1u) is the only ticket change.

## Legs: 164 unique settled, 82-79 (50.9%)

This week alone (settled >=10/06): 91 unique legs, 47-42 (52.8%). The paper tier (ranks 6-20, staked:false) is doing its job: the ledger more than doubled in a week (73 → 164), which is what let NFL cross the 50-leg bar.

By sport: **NFL 30-18 (62.5%, n=50) best — now ELIGIBLE** | MLB 16-22 (42.1%, n=38) worst | CFB 17-18 (48.6%, n=36) | NHL 13-13 (50.0%, n=26, newcomer) | WNBA 6-8 (42.9%, n=14, newcomer now losing). NFL crossed 50 legs; nothing else is there yet.

By market: spread 33-26 (55.9%, n=62) best | moneyline 29-28 (50.9%, n=57) | totals 20-25 (44.4%, n=45) — totals are the soft spot, approaching eligibility; on watch, not acted on.

By home/away (sides only): away 41-27 (60.3%, n=69) | home 21-27 (43.8%, n=50). Both eligible now. The home/away split persists — the 10/05 home-side 6% bar stays.

## Calibration (logged confidence)

| bucket | n | stated avg | actual | gap |
|---|---|---|---|---|
| <50 | 37 | 43.6% | 50.0% | -6.4pp |
| 50-59 | 116 | 54.8% | 50.9% | +4.0pp |
| 60-69 | 11 | 62.8% | 54.5% | +8.3pp |
| 70+ | 0 | — | — | — |

The 50-59 bucket (eligible, n=116) gap fell to +4.0pp — **the 9/21 lift trigger (gap ≤5pp) is met**. Forensic on the haircut (implied odds + claimed edge reconstructs the raw model): 44 legs logged with the 15pt haircut; the 35 with inferred raw ≥60 averaged raw 66.9% and hit 62.9% — the raw model is calibrated within 4pp in that range, while the haircut understates those legs by ~11pp. The haircut has flipped from fix to distortion. The <50 bucket (dogs, logged raw since 9/28) is conservative-or-better (-6.4pp) — fine. 60-69 (raw 75-84 pre-lift) is preliminary at n=11 with an +8.3pp gap — the top end stays watched.

## CLV: 27 beat / 22 lost / 40 push / 75 missing — 55.1% excl pushes

Down from the (corrected) 58.3% pre-10/06. This week: 13b/12l/26p. Process is roughly neutral-to-positive, not the edge it looked like last week. The 9/28 logging rule is still being violated: **75 of 164 legs (46%) have no closing data**, including 40 this week. Flagged for the third straight review — the rule exists, it needs enforcing, not rewriting.

## Approach vs approach (flat 1u singles)

| approach | n | W-L | hit | CLV excl-push | roi |
|---|---|---|---|---|---|
| model-value | 87 | 46-39 | 54.1% | 59% (13b/9l) | +2.60u |
| situational | 29 | 13-15 | 46.4% | 60% (6b/4l) | -4.46u |
| model-edge | 14 | 7-7 | 50.0% | 67% (4b/2l) | -1.38u |
| line-movement | 12 | 5-7 | 41.7% | 0% (0b/5l) | -2.32u |
| brand-tax fade | 8 | 5-3 | 62.5% | 60% (3b/2l) | +4.78u |
| fpi-value | 6 | 3-3 | 50.0% | n/a | -0.27u |
| fpi-chalk | 3 | 0-3 | 0.0% | n/a | -3.00u (stays demoted) |
| mild-value | 2 | 1-1 | 50.0% | n/a | -0.09u |
| dip-buy | 1 | 0-1 | 0.0% | n/a | -1.00u (fourth week, still n=1) |

Eligible (n≥20): model-value and situational. **model-value is the workhorse the paper tier discovered**: 54.1% hit, positive CLV, the only approach with positive ROI at scale (+2.60u). situational (29 legs): failing on results (46.4%) but passing on process (60% CLV) — mixed verdict, the 6% bar stays (see trigger check below). line-movement is failing on BOTH metrics (41.7% hit, 0b/5l CLV) but n=12 <20 — preliminary; if it reaches 20 still failing both, it gets the fpi-chalk treatment. model-edge (6% bar) is 7-7 with 67% CLV — mixed, bar stays. brand-tax fade is the best ROI approach but n=8, preliminary.

**Situational cut-trigger check** (10/05 rule 4: demote to confirming-angle-only if trailing-20 hit ≤50% AND CLV <50%): trailing-20 is 8-11 (42.1%) — condition 1 met; CLV 4b/3l = 57% excl pushes — condition 2 NOT met. Trigger not fired. The 6% bar stays; re-audit next week with the same dual trigger.

## Edge tags: the inflation warning did NOT repeat

Claimed-edge bands: below-4% → 32-28 (53.3%, n=61); 4.0-5.9% → 21-19 (52.5%, n=41); 6.0-7.9% → 9-7 (56.2%, n=17); 8.0%+ → 4-4 (50.0%, n=8). The 10/05 warning (bigger claimed edge → worse hit rate) has flattened out — the 6%+ band is 13-11 (54.2%) combined, above 50%. Edge estimates look honest now. No rule change.

## Brand-tax (sides only)

Backing marquee (NYY, LAD, CHC, BOS, KC, DAL, PHI, NYG, LAL, GSW): 3-4 (42.9%, n=7) — added Giants +3.5 (W) this week.
Fading marquee: 10-4 (71.4%, n=14) — added Buccaneers +8.5 (W), Buccaneers ML (W), Sabres ML (W), Mammoth ML (W) this week.
Still preliminary (n<20 both), but the fade lean keeps paying: +4.78u on the brand-tax fade approach. Fade/back rules stand.

## Dip-buy: n=1 (Syracuse +10.5, L). No verdict — fourth week running.

## Stack-rank dogfood

Settled legs with stack_rank: ranks 1-5 → 14-11 (56.0%, n=25); ranks 6-10 → 13-11 (54.2%, n=25). **The fine rank ordering is not separating winners** (1.8pp gap). But qualified=true → 9-5 (64.3%, n=14) vs qualified=false → 38-36 (51.4%, n=76): **the binary edge bar IS the signal that works** (13pp gap). The dilution: on 10/07-10/08 the staked set included below-bar legs (10/08 ranks 3-5: White Sox ML +3.5pp, Bruins ML +3.0pp — qualified=false but staked=true). The 10/11 card did it right: ranks 1-5 = the five qualifiers, all staked, 3-2.

- Daily-average top-5 hit rate: 56.0% over 5 days. Trailing-20 top-5: 12-8 (60.0%) vs the 80% goal — **exactly at the structural-change trigger line** (under 60% triggers).
- Actually-staked legs: 10-5 (66.7%), +5.24u @1u singles.

## Best-slice (NFL concentration)

NFL overall: 30-18 (62.5%, n=50) — eligible, best sport by a mile. Trailing-20: 12-7 (63.2%) — far above the 55% re-open trigger. **Concentration stays.** NFL away sub-slice: 13-5 (72.2%, n=19) — one leg short of preliminary-eligible; still the sharpest corner of the ledger. This week's all-NFL card (10/11) went 12-7-1 on legs, 3-2 on the staked five.

## Props discovery (prop-ledger.jsonl, never merged into v3)

17 settled legs, 11-6 (64.7%). By prop_type: player passing yards 4-3 (57.1%, n=7) is the only type with n>2; everything else n≤2. By repeatable_pattern: **no pattern has 3+ settled instances yet** — nothing graduates, nothing gets killed. Closest: 'struggling-QB passing under vs elite pass D' is 0-2 (kill line is <40% at 3+ — one more loss kills it). The 10/11 clean-pattern day (backup/returning-QB unders, matchup overs) went 2-1. The lane is working but the sample is young; keep hunting.

## Sven's own (off-schema, ticket-level only — never re-scored)

sven-8-leg 0-1 (legs 5-3), sven-prop-7-leg 1-0 (legs 7-0, +$12,278.17 real — his pick, the north star), sven-2-pick 0-1 (legs 1-1).

## Method notes
- Push legs excluded from W-L records (164 unique = 82W + 79L + 3P).
- Single-leg ticket ROI: win → decimal(odds)−1; loss → −1.
- The 10/12 daily-20 (14 legs) and 4 prop legs are pending — excluded.
- Edge-band and haircut forensics parse the numeric claimed edge from the edge field (e.g. '+14.6pp', 'model-value (+4.6%)'); 16 legs had ambiguous edge text and were excluded from the forensic only.
