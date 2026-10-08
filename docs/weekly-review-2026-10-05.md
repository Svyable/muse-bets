# Weekly review 2026-10-05 — full numbers

Scope: 32 settled v3-schema entries (top-level tier + source; legs carry pick, market, odds, confidence, approach, result). 3 entries skipped silently (Sven's 9/16 8-leg, 9/17 prop 7-leg, 9/19 2-pick — user-source, legs lack odds/confidence). Dedupe: legs counted once per unique (date, matchup, pick) — e.g. 9/30 Padres -1.5 logged in 2 tiers counts once; the 9/28 review applied the same rule. Ticket stats are NOT deduped. All odds @1u flat. Script: /tmp/weekly_review_2026_10_05.py (scratch; rerun against the ledger to reproduce).

CLV semantics (unchanged from the 9/21 correction): ML — beat when booked odds numerically exceed closing odds (favorite: less juice; dog: bigger payout; push when equal). Spread — beat when booked line numerically exceeds the closing line on the picked side (closing read from closing_line, or closing_odds when |x|<=40; e.g. Jaguars +2.5 push vs close 2.5, Raiders +4.5 beat vs close 5.5). Total — over: beat when booked line < close; under: beat when booked line > close (closing read from closing_line, or closing_odds when it looks like a line, e.g. Under 67.5 vs close 70).

## Tickets @1u

| tier | W-L | net | ROI |
|---|---|---|---|
| steady | 2-3 | -1.67u | -33.4% |
| balanced | 1-13 | -10.36u | -74.0% |
| lottery | 0-11 | -11.00u | -100.0% |
| single | 1-0 | +0.71u | +71.4% |
| single-lean | 1-0 | +0.87u | +87.0% |
| **all** | **5-27** | **-21.44u** | **-67.0%** |

Sven's own (off-schema, ticket-level only — not re-scored): sven-8-leg 0-1 (legs 5-3), sven-prop-7-leg 1-0 (legs 7-0, +$12,278.17 real), sven-2-pick 0-1 (legs 1-1).

This week alone (entries dated ≥9/29, plus the now-settled 9/28 single-lean): tickets 1-7 (-6.13u); unique legs 9-9 (50.0%, n=19 incl. 1 push); CLV 7b/1l/10p. Legs stabilized at a coin flip while tickets kept bleeding — the wins came on singles, the losses on full parlays.

## Legs: 73 unique, 35-37 (47.9%)

By sport: NFL 16-10 (61.5%, n=27) best | MLB 13-17 (43.3%, n=30) worst | CFB 3-5 (37.5%, n=8) | WNBA 1-5 (16.7%, n=6) | NHL 2-0 (n=2). No sport at the 50-leg bar — no cuts. WNBA is a watched newcomer (all six legs came this week).

By market: moneyline 15-12 (55.6%, n=27) best | spread 15-14 (51.7%, n=30) | totals 5-11 (31.2%, n=16) worst (preliminary).

By home/away (sides only, totals excluded): away 20-13 (60.6%, n=34) | home 10-13 (43.5%, n=23). Home is now at the 20-leg eligibility bar — see rule change 2.

## Calibration (logged confidence)

| bucket | n | stated avg | actual | gap |
|---|---|---|---|---|
| <50 | 26 | 43.5% | 48.0% | -4.5pp |
| 50-59 | 37 | 55.5% | 48.6% | +6.8pp |
| 60-69 | 10 | 63.0% | 50.0% | +13.0pp |
| 70+ | 0 | — | — | — |

<50 and 50-59 are eligible (n≥20). The 50-59 bucket gap moved barely (+7.1pp → +6.8pp) — still above the 5pp lift bar, so the 15-pt haircut stays for raw ≥60. The <50 bucket is calibrated-or-better (dogs logged raw stay raw). 60-69 is preliminary; it graduates to its own rule at n=20.

## CLV: 39 evaluable unique legs — 15 beat / 10 lost / 14 push (60.0% excl. pushes)

Up from 47.1% (9/28). This week: 7b/1l/10p. The process IS beating the close on moneylines now (7 of the 8 beats this week are ML juice wins: Phillies ML, Aces ML, Valkyries ML, Liberty ML, Rangers ML, Lightning ML, Dodgers ML). Caveat: 10 pushes this week are mostly booked-line == closing-line entries (logged at event time, not true closes), and 34 of 73 legs still have no closing data at all — the 9/28 logging rule (capture a close for every leg or flag it) is not being followed. A leg with no close is still a process miss.

## Approach vs approach (primary approach = normalized first component)

| approach | n | W-L | hit | CLV | flat-1u |
|---|---|---|---|---|---|
| situational | 25 | 12-12 | 50.0% | 5b/5l | -2.33u |
| model-value | 12 | 5-7 | 41.7% | 3b/1l | -2.46u |
| model-edge | 11 | 6-5 | 54.5% | 3b/2l | -0.12u |
| fpi-value | 6 | 3-3 | 50.0% | n/a | -0.27u |
| brand-tax fade | 6 | 3-3 | 50.0% | 2b/1l | +0.23u |
| line-movement | 5 | 3-2 | 60.0% | 1b/1l | +0.73u |
| fpi-chalk | 3 | 0-3 | 0.0% | n/a | -3.00u |
| mild-value | 2 | 1-1 | 50.0% | n/a | -0.09u |
| dip-buy | 1 | 0-1 | 0.0% | n/a | -1.00u |
| structural | 1 | 1-0 | 100% | n/a | +0.91u |
| projection gap | 1 | 1-0 | 100% | 1b/0l | +0.91u |

Only situational is at the 20-leg approach bar. Trailing-20 situational: 10-9 (52.6%) hit, CLV 3b/3l (50%) excl pushes — the 9/28 re-audit condition (hit >50% AND CLV positive) is half-met: hit rate ✓, CLV not positive ✗. The 6% bar stays; an explicit cut trigger is now set (see rule change 4). Nothing else earns a promotion or a cut: everything else is preliminary, and no approach is both failing-on-two-metrics and eligible.

## Edge tags: does the claimed edge predict?

Legs with an explicit claimed edge in the edge field (e.g. "model-value (+4.6%)"): 4.0-5.9% → 10-7 (58.8%, n=17); 6.0-7.9% → 7-6 (53.8%, n=14); 8.0%+ → 1-3 (25.0%, n=4). Combined 18-16 (52.9%). All preliminary (n<20 per band). Warning sign, not a rule: the bigger the claimed edge, the worse the hit rate — the edge estimates themselves look inflated. Watch this band next week; if the 6%+ band is still under 50% at n=20, the edge-threshold rules get rewritten.

## Brand-tax (sides only)

Backing marquee (NYY, LAD, CHC, BOS, KC, DAL, PHI, NYG, LAL, GSW): 2-4 (33.3%, n=6): Chiefs -6.5 L, Cowboys -3.5 W, Cubs ML W, Phillies ML L ×2, Dodgers ML L.
Fading marquee: 6-2 (75.0%, n=8): Titans +7 W, Colts +6.5 W, Rays ML L, Guardians ML W ×2, Dolphins +10.5 L, Padres -1.5 W, Raiders +4.5 W.
Preliminary (n<20 both), but directionally supportive of the fade lean — unchanged rule.

## Dip-buy: n=1 (Syracuse +10.5, L). No verdict — third week running.

## Method notes
- Push legs in parlay ROI are reduced (decimal 1.0); a ticket with any losing leg is a loss.
- Sven's legs are off-schema by design (no odds/confidence) and are never re-scored — ticket-level only.
- The 73 unique settled legs include the 9/28 review's 54 plus 19 net-new (26 raw new legs minus cross-tier dupes within a date, plus the settled 9/28 single-lean).
