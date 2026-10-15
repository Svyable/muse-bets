# Pick strategy — v3 (2026-09-16)

Multi-sport handicapping experiment, enhanced with the Silver/Beane upgrades. Updated only by the weekly Monday review, on ledger evidence — plus user-directed process changes, marked as such below.

## Process change — user-directed uncap (2026-10-14)

Sven: "Uncap it — log every leg that clears the bar." Supersedes the 2026-10-07 daily-20 cap. This is a *process* change on his direct instruction — no edge bars, staking rules, or Silver evidence thresholds were altered.

- **Daily 20 → uncapped card.** The card is every leg that clears its edge bar — no cap, no filler. Count varies by slate (a dozen on a thin Wednesday, 40+ on a big Saturday).
- **Staked set unchanged** (10/12 rule): qualified legs ranked by edge, max 5, never forced — fewer than 5 qualifiers → stake fewer.
- **Paper tier = all other qualifiers** (`staked:false`): zero bankroll risk, logged to the same ledger purely to grow settled-leg volume toward the Silver thresholds (50+ legs per sport/approach).
- **Below-bar legs are no longer logged.** The 10/12 review showed the binary bar is the signal (qualified 64.3% vs unqualified 51.4%); near-miss/below-bar fills added noise, not discovery.
- If games are scheduled but nothing clears the bar, deliver an empty card and say so plainly — never force picks to fill a quota.

## Process change — user-directed scale-up (2026-10-07)

Sven: "Scale up your betting to self improve faster." This is a *process* change on his direct instruction, not a weekly-review rule change — no edge bars, staking rules, or Silver evidence thresholds were altered.

- **Daily 10 → daily 20.** Ranks 1–5 remain the staked dogfood set (80% hit-rate goal, all edge bars unchanged). Ranks 6–20 are a paper-trade learning tier (`staked:false`): zero bankroll risk, logged to the same ledger purely to grow settled-leg volume, so the Silver thresholds (50+ legs per sport/approach) arrive ~2x faster. Paper-tier inclusion: legs within 2pp of their edge bar first (near-misses are the most informative data), then BELOW-BAR fills.
- **Props discovery goes daily** (was no-NFL/Wednesdays only). Still in prop-ledger.jsonl, never mixed into v3 binary evidence.
- **No-pick days still log the paper tier.** If games are scheduled but nothing qualifies for the staked set, the paper tier is still delivered and logged — the ledger grows every day there are games. (2026-10-06 and 2026-10-07 logged zero legs; that dead time is what this fixes.)
- The weekly review analyzes staked and paper tiers separately: the staked tier drives staking/tier decisions; the paper tier drives approach/sport discovery (which angles earn promotion to the staked set).

## The standing rule
Sven's instruction: the loop's job is to find what works, not to defend a method. Never anchor to a single handicapping approach or a single evaluation metric. Every pick records its **approach** (the method that produced it: power-rating edge, brand-tax fade, dip-buy, situational spot, line movement, user pick, etc.), and the weekly review compares approaches against each other on every metric — CLV, ROI, hit rate, calibration. Approaches that don't earn their keep get cut or down-weighted, no matter how clever they sound.

## Scope: which sport am I actually good at?
- Cover every sport in season (MLB, NFL, CFB, NBA, NHL as the calendar turns). The ledger decides my best sport; the review cuts sports the record says to cut.
- New sport or new season = conservative priors. Confidence starts small until the data earns it (Bayesian shrinkage: one weekend never makes a team "elite").

## Markets: low-vig binary outcomes ONLY
- Allowed: moneyline, spread (incl. run line / puck line), totals (over/under).
- Banned: same-game parlays, player props, touchdown-scorer markets, any exotic without a clean win/lose/push outcome.
- Avoid heavy juice (worse than -200) without a clear, stated edge.

## The fair-odds edge rule (core)
- Maintain simple power ratings per sport (Elo-style, updated from results) and convert them to fair probabilities for every candidate leg.
- A leg only makes the card if: model probability − market implied probability ≥ 4%.
- No edge, no bet. If a parlay tier can't be filled with edged legs, deliver fewer legs or say so honestly — never force picks to fill a quota.
- Shop the line: record the best available odds and the book. -105 vs -110 is the whole business.

## Beane rules: hunt mispricing, not winners
- **Fade the brand tax.** Marquee teams (Yankees, Dodgers, Cowboys, Lakers, Chiefs, etc.) are systematically overpriced by public money. Require a *larger* edge (≥6%) to back them; default lean is the other side when the line looks shaded.
- **Buy the dip on cluster luck.** Teams on losing streaks built from one-run/one-score losses, bad sequencing, or BABIP-style bad fortune are value candidates, not automatic fades. Distinguish "bad" from "unlucky" in the reasoning.
- **Process over results, ruthlessly.** CLV (did we beat the closing line?) is the primary scoreboard. A winning week with negative CLV changes nothing; a losing week with positive CLV changes nothing. Cut a lucky winner, keep an unlucky process.

## Silver rules: respect the sample
- 10 settled legs = preliminary observations only, flagged as such. **50+ settled legs** (per sport for sport-level calls, 20+ per confidence bucket for calibration calls) = eligible for actual rule changes.
- No narrative inputs as edge tags until the ledger proves they predict: momentum, revenge games, "due for a win," gut feel. Banned until evidence.
- Prefer ensembles: two or three simple angles agreeing beats one clever story.

## Logging discipline
- Every pick logged to `pick-ledger.jsonl` BEFORE the event starts. Nothing retroactive. Sven's and Muse's picks all count.
- Full schema per leg: sport, league, matchup, picked team, home/away/neutral, market, line, odds (+ book), closing line/odds, confidence, **approach** (which method produced this pick), edge tag, one-line reason.
- Confidence = estimated probability, and it should roughly match the model's fair probability. Calibration is graded weekly.

## Parlay construction & staking
- **Steady**: 3–4 legs, every leg ≥60% confidence. Largest share of stake.
- **Balanced**: 4–5 legs, 55–70% mix. Medium share.
- **Lottery**: 6+ legs, longshots allowed. Smallest share — it must never be able to nuke the other two.
- A losing day never changes the process. Tilt is not a strategy.

## What changes and how
- Only the weekly review changes these rules, and only at the evidence thresholds above.
- The review examines: record by tier/sport/market/home-away, calibration per bucket, CLV win rate, edge-tag hit rates, brand-tax performance, dip-buy performance — and **approach vs approach**: which methods are actually producing winners, judged on all metrics, not one.

---

## Weekly review 2026-09-21 (66 settled legs; full numbers in hidden_files/weekly-review-2026-09-21.md)

Headline: tickets 1-12 on Muse cards (-10.09u @1u); Muse legs 19/49 (38.8%) vs ~57% average stated confidence. CLV is negative (5 beat / 6 lost / 1 push on the 12 evaluable unique legs) — the process is NOT beating the close; the inputs are miscalibrated and the prices are bad too. (Correction 9/21: the review first wrote 6b/4l/1p with inverted spread/total CLV semantics; independently recomputed to 5b/6l/1p.) Calibration gap is ~19 points in BOTH buckets (50-59%: n=33, stated 55.2% vs actual 36.4% — eligible for a rule change; 60-69%: n=16, stated 63.2% vs actual 43.8% — preliminary). By sport: NFL 19-11, MLB 11-16, CFB 2-7 (all preliminary, <50/sport — no cuts). By approach: model-edge 7-11 (-5.5u), situational 5-7, fpi-value 4-6, fpi-chalk 0-3, line-movement 2-2 (all preliminary, <20/approach — no cuts). Brand-tax: backing marquee 1-3, fading 3-1 (preliminary). Dip-buy n=1 (too small). Sven's own legs: 12-3, +$12,273 real.

### Rule changes (effective immediately)
1. **15-point confidence haircut.** Logged confidence = model probability − 15 until a weekly review shows the calibration gap ≤5 points in the 50-59% bucket. The steady-ticket bar stays at *logged* ≥60% (i.e. raw model ≥75%). The 60-69% bucket (n=16, gap +19.4pp) corroborates; it graduates to its own rule when it hits n=20.
2. **fpi-chalk demoted.** Raw FPI gaps may never be the lead approach and may never anchor a steady ticket — the 9/17 steady card's own contemporaneous note admitted "No backtested model edge; FPI is ESPN's," then went 0-3 (-3.0u). FPI is a confirming angle only, and only alongside an independent edge.
3. **model-edge (esp. MLB SP mismatch) bar raised to ≥6%.** The flagship approach is 7-11 (-5.5u) and its CLV is also negative — failing on process as well as results — so it is down-weighted, spared from an outright cut only because n=18 < 20: SP-mismatch/projection-gap legs need a 6%+ edge until the trailing-20 hit rate recovers above 45%. Re-audit next week; if CLV and hit rate are both still negative, weigh cutting the approach entirely.
4. **Dedupe rule for the review itself.** A leg logged across multiple tiers (Colts +6.5 ×3, Cubs ML ×3) counts once per unique (date, matchup, pick) in all leg-level review stats. Ticket stats unchanged. (This review applied it: unique-leg CLV 5b/6l/1p on the 12 evaluable legs.)

### Explicitly NOT changed (preliminary or too small — re-audit 9/28)
- No sport cut (NFL 19-11 best / CFB 2-7 worst, but no sport ≥50 legs).
- No approach cut (none ≥20 legs); situational, fpi-value, line-movement stay.
- Brand-tax fade/back rules stand (backing 1-3, fading 3-1 — preliminary).
- Dip-buy: n=1, no verdict.
- Home/away split (home 7-15 vs away 22-17) is noted and watched, not acted on.

---

## Weekly review 2026-09-28 (54 unique settled legs; full numbers in hidden_files/weekly-review-2026-09-28.md)

Headline: tickets 3-21 (-15.30u @1u) — steady 2-3 (-1.67u), balanced 1-8 (-5.35u), lottery 0-9 (-9.00u), single 1-0 (+0.71u). Legs 26-28 (48.1%). The week itself (settled since 9/21): legs 11-11 (50.0%) on 22 unique legs — results stabilized, but tickets went 2-8 (-6.86u) because the wins came on short-priced steady/single cards and the losses on long balanced/lottery cards. CLV is still negative: 8 beat / 9 lost / 4 push on 21 evaluable unique legs (47.1% excl. pushes); this week 2b/4l/2p (33%). Process is NOT beating the close. Calibration: the 50-59 logged bucket improved a lot (n=25, stated 55.1% vs actual 48.0%, gap +7.1pp vs +18.8 last week) but is still above the 5pp lift bar. The <50 logged bucket (n=20, stated 43.0% vs actual 50.0%, gap -7.0pp) shows the 15-pt haircut is now misfiring on longshots — dogs are calibrated-or-better. By sport: NFL 12-10, MLB 12-14, CFB 2-4 (all <50 — no cuts). By market: moneyline 12-8 (60.0%) best, spread 11-13, totals 3-7 (30%, preliminary). Home/away: away 17-9 (65.4%) vs home 6-13 (31.6%) — home is n=19, one leg short of eligibility; watched, not acted on. By approach: situational n=20 (eligible): 9-11 (45.0%), CLV 3b/4l (42.9%) — failing on both metrics, gets down-weighted. model-edge n=10: 6-4 (60.0%), CLV 4b/2l (66.7%) — the 9/21 re-audit condition is satisfied on the positive side; approach stays, 6% bar stays. line-movement 3-2, brand-tax fade 2-2, fpi-value 3-3, fpi-chalk 0-3 (stays demoted), model-value 1-1, mild-value 1-1, structural 1-0 (all preliminary). Brand-tax (sides only): backing marquee 2-2, fading 6-2 (preliminary, supports the lean). Dip-buy n=1, no verdict. Sven's own (off-schema, ticket-level only): 8-leg 0-1, prop 7-leg 1-0 (+$12,278.17 real), 2-pick 0-1.

### Rule changes (effective immediately)
1. **Haircut split by raw model probability.** The 15-point haircut now applies ONLY to legs with raw model probability ≥60% — the 50-59 logged bucket (n=25, gap +7.1pp) still needs it. Legs with raw model <60% (dogs/longshots) are logged at raw model probability with no haircut: the <50 logged bucket (n=20, eligible) is calibrated-or-better (stated 43.0% vs actual 50.0%), so the haircut was pure distortion there. Re-audit both buckets next week.
2. **Situational down-weighted to a 6% edge bar.** situational is now n=20 (eligible): 9-11 hit rate and 42.9% CLV win rate — the same two-metric failure that got model-edge its 6% bar last week. Situational legs need model − implied ≥6% until the trailing-20 hit rate recovers above 50% AND CLV turns positive. Re-audit next week; if both are still negative, weigh cutting the approach.
3. **Closing-line capture is now a logging rule.** CLV is the primary scoreboard and it is going dark: the entire 9/25 and 9/27 cards (9 legs) plus several earlier legs have no closing data. The morning settle pass must backfill closing line/odds for every leg and flag any leg that stays CLV-inevaluable. A leg with no close is a process miss, same as a leg with no odds.
4. **model-edge re-audit: PASSED, 6% bar retained.** 6-4 (60%) with 4b/2l CLV (66.7%) — the 9/21 condition (cut if both negative) resolved positive. The flagship approach lives, and the 6% bar that likely drove the recovery stays.

### Explicitly NOT changed (preliminary or too small — re-audit 10/5)
- No sport cut (NFL 12-10 best / CFB 2-4 worst, no sport ≥50).
- No approach cut; line-movement (3-2), brand-tax fade (2-2), fpi-value (3-3) stay.
- fpi-chalk stays demoted (0-3).
- Brand-tax fade/back rules stand (fading 6-2 on sides vs backing 2-2 — preliminary but directionally supportive).
- Dip-buy: n=1, no verdict.
- Home/away: home 6-13 (n=19) is one leg short of the 20-leg bar — watched, not acted on.
- Lottery tier 0-9 (-9u) is a structural bleed but under 10 tickets — noted, not acted on.

---

## Weekly review 2026-10-05 (73 unique settled legs; full numbers in hidden_files/weekly-review-2026-10-05.md)

Headline: tickets 5-27 (-21.44u @1u, ROI -67.0%) — steady 2-3 (-1.67u), balanced 1-13 (-10.36u), lottery 0-11 (-11.00u), single 1-0 (+0.71u), single-lean 1-0 (+0.87u). Legs 35-37 (47.9%). The week itself: tickets 1-7 (-6.13u); legs 9-9 (50.0%) — a coin flip on legs while parlays kept bleeding, because the wins came on singles and the losses on full cards. CLV turned positive: 15 beat / 10 lost / 14 push (60.0% excl pushes, up from 47.1%; this week 7b/1l/10p) — the process IS beating the close on moneylines now. Results are still bad: 47.9% at ~-110 average juice is below the ~52.4% break-even line. By sport: NFL 16-10 (61.5%) best, MLB 13-17 (43.3%) worst (no sport ≥50 — no cuts). By market: moneyline 15-12 (55.6%) best, spread 15-14 (51.7%), totals 5-11 (31.2%, preliminary). Home/away: away 20-13 (60.6%) vs home 10-13 (43.5%) — home is now eligible (n=23). Calibration: <50 bucket (n=26) gap -4.5pp (dogs calibrated-or-better, stay raw); 50-59 bucket (n=37) gap +6.8pp (still above the 5pp bar — haircut stays for raw ≥60); 60-69 (n=10, gap +13.0pp) preliminary. By approach: situational n=25 (eligible): 12-12 (50.0%), CLV 5b/5l — trailing-20 is 10-9 (52.6%) hit with 3b/3l CLV (50%), so the 9/28 re-audit condition (hit >50% AND CLV positive) is only half-met; the 6% bar stays and now carries an explicit cut trigger. model-edge n=11 (preliminary): 6-5, CLV 3b/2l — 6% bar stays. line-movement 3-2, brand-tax fade 3-3, fpi-value 3-3, model-value 5-7 (all preliminary); fpi-chalk 0-3 stays demoted. Brand-tax: backing marquee 2-4 (33.3%), fading 6-2 (75.0%) — preliminary, fade lean stands. Dip-buy n=1, no verdict — third week running. Warning sign (preliminary): legs with claimed edge 8.0%+ are 1-3; the edge estimates look inflated at the top end. Sven's own (off-schema): sven-8-leg 0-1, sven-prop-7-leg 1-0 (+$12,278.17 real), sven-2-pick 0-1.

### Rule changes (effective immediately)
1. **Lottery tier SUSPENDED.** 0-11 (-11.00u, -100% ROI) — past the 10-ticket bar the 9/28 review named. Our ~48% legs cannot clear a 6+ legger's break-even line without edges far larger than the ledger shows. The morning job stops building lottery tickets; stake redistributes to steady. Revisit only when the trailing-50 unique legs hit ≥52% AND CLV ≥55%.
2. **Home-side 6% edge bar.** Away 20-13 (60.6%) vs home 10-13 (43.5%) on 57 sides; home is now eligible (n=23). Same bar pattern as the approach rules: a home side needs model − implied ≥6% to make the card; away sides keep the 4% bar. Re-audit when home legs reach n=40. (This is a directional split, not a ban — if the split is noise, the bar costs nothing; if it's real, it stops the bleed.)
3. **Calibration re-audit: split haircut CONFIRMED.** 50-59 logged bucket (n=37, eligible): stated 55.5% vs actual 48.6%, gap +6.8pp — barely moved from +7.1pp and still above the 5pp lift bar, so the 15-pt haircut stays for legs with raw model ≥60%. <50 bucket (n=26, eligible): stated 43.5% vs actual 48.0%, gap -4.5pp — dogs stay logged at raw model probability, no haircut. 60-69 bucket (n=10): gap +13.0pp, preliminary; graduates to its own rule at n=20.
4. **Situational: 6% bar stays, cut trigger set.** Trailing-20: 10-9 (52.6%) hit — above 50% ✓; CLV 3b/3l (50%) — not positive ✗. The 9/28 condition needs both, so the bar stays. New: if the next weekly review shows trailing-20 hit rate ≤50% AND CLV <50% (both negative), situational is demoted to confirming-angle-only (fpi-chalk treatment) — no lead legs, no ticket anchors.

### Explicitly NOT changed (preliminary or too small — re-audit 10/12)
- No sport cut (NFL 16-10 best / MLB 13-17 worst, no sport ≥50). WNBA is a watched newcomer (1-5, n=6).
- No approach cut (only situational ≥20); line-movement (3-2), brand-tax fade (3-3), fpi-value (3-3), model-value (5-7) stay.
- model-edge 6% bar stays (6-5, CLV 3b/2l — preliminary, directionally positive).
- fpi-chalk stays demoted (0-3).
- Brand-tax fade/back rules stand (fading 6-2 vs backing 2-4 — preliminary but directionally supportive).
- Dip-buy: n=1, no verdict.
- The 9/28 logging rule (capture a closing line/odds for every leg or flag it) is still being violated: 34 of 73 legs have no closing data, including one this-week card. Flagged again — no new rule, the old one needs enforcing.

---

## Weekly review 2026-10-12 (164 unique settled legs; full numbers in hidden_files/weekly-review-2026-10-12.md)

Headline: classic-tier tickets -22.43u over 33 (no classic tickets since 10/06 — the format is the daily ranked card now). Legs 82-79 (50.9%); this week 47-42 (52.8%) on 91 new settled legs — the paper tier (ranks 6-20) more than doubled the ledger in a week, which is what pushed NFL over the 50-leg bar. CLV 27b/22l/40p (55.1% excl pushes) under CORRECTED spread semantics — the 10/05 review's 'Raiders +4.5 beat vs close 5.5' example was economically inverted (a dog closing at a bigger number is CLV lost, not beat); pre-10/06 CLV restates to 14b/10l/14p = 58.3% (was 60.0%). The positive-CLV story survives, slightly weaker. By sport: NFL 30-18 (62.5%, n=50, ELIGIBLE — best by a mile), MLB 16-22 (42.1%, n=38) worst, CFB 17-18, NHL 13-13 (newcomer), WNBA 6-8 (newcomer, now losing). By market: spread 33-26 (55.9%) best, moneyline 29-28, totals 20-25 (44.4% — soft spot, on watch). Home/away: away 41-27 (60.3%) vs home 21-27 (43.8%), both eligible — split persists. Calibration: 50-59 bucket gap +4.0pp (n=116, eligible) — the 9/21 lift trigger (≤5pp) is met; forensic (implied + claimed edge) shows inferred-raw≥60 legs hitting 62.9% vs avg raw 66.9% — raw is calibrated, the haircut understates by ~11pp. Edge-tag inflation warning did NOT repeat (6%+ band 13-11, 54.2%). By approach (eligible): model-value n=87, 46-39 (54.1%), +2.60u — the workhorse the paper tier discovered, only approach with positive ROI at scale; situational n=29, 13-15 (46.4%), CLV 60% — failing results, passing process. line-movement 5-7 with 0b/5l CLV is failing both metrics but n=12, preliminary. brand-tax fade 5-3 (+4.78u), preliminary, best ROI. Dogfood: ranks 1-5 14-11 (56.0%) vs ranks 6-10 13-11 (54.2%) — the fine ranking doesn't separate; qualified=true 9-5 (64.3%) vs qualified=false 38-36 (51.4%) — the binary edge bar is the signal. Trailing-20 top-5: 12-8 (60.0%) vs the 80% goal — exactly at the structural-change trigger line. Staked legs: 10-5 (66.7%), +5.24u. Best slice: NFL trailing-20 12-7 (63.2%), far above the 55% re-open trigger — concentration stays; NFL away 13-5 (72.2%, n=19) still the sharpest corner. Props: 17 settled legs, 11-6 (64.7%); no pattern at 3+ instances yet — nothing graduates, nothing killed ('struggling-QB passing under vs elite pass D' 0-2 is one loss from the kill line). Dip-buy n=1, fourth week, no verdict. CLV capture still violated: 75 of 164 legs missing closes (40 this week) — flagged third straight week.

### Rule changes (effective immediately)
1. **15-point haircut LIFTED.** The 9/21 rule named its own exit (50-59 logged-bucket gap ≤5pp) and it's met: +4.0pp at n=116. The forensic confirms the raw model is calibrated within 4pp for raw≥60 legs (62.9% actual vs 66.9% avg raw) — the haircut now understates those legs by ~11pp, distorting logged confidence and the steady bar. Log raw model probability as confidence for all legs. Guardrail: re-audit in 2 weeks; if the 60-69 logged bucket (now raw) shows gap >5pp at n≥20, reinstate a 10pt haircut for raw≥70. (The 60-69 bucket is currently +8.3pp at n=11, preliminary — the top end stays watched.)
2. **Staked set = qualified legs only, ranked by edge, max 5 — below-bar legs are paper-only, never staked.** Ranks 1-5 (56.0%) don't outhit ranks 6-10 (54.2%), but qualified=true (64.3%) crushes qualified=false (51.4%); the dilution came from staking below-bar legs on 10/07-10/08. The 10/11 card (ranks 1-5 = the five qualifiers, all staked, 3-2) is now the hard rule, not just the pattern. 'Qualified slots never forced' stands: fewer than 5 qualifiers → stake fewer. Re-audit in 2 weeks: if the qualified set's trailing-20 is under 65%, raise the staked bar to edge ≥6%.
3. **MLB cut trigger set.** MLB is 16-22 (42.1%, n=38), the worst sport and approaching the 50-leg bar, while NFL just validated the concentration rule at 30-18 (62.5%). If MLB reaches 50 settled legs with a hit rate under 45%, MLB legs require a 6% edge to make any card (same bar as home sides). No change today — the trigger is pre-committed.
4. **Situational: 6% bar stays, dual trigger re-armed.** Full sample n=29 (eligible): 13-15 (46.4%) hit, 60% CLV excl pushes — failing on results, passing on process. Trailing-20: 8-11 (42.1%) hit meets the first demotion condition, but CLV 4b/3l (57%) is not <50% — the 10/05 dual trigger (BOTH negative) is not met, so no demotion. Same trigger next week: trailing-20 hit ≤50% AND CLV <50% → situational becomes confirming-angle-only (fpi-chalk treatment).

### Explicitly NOT changed (preliminary or too small — re-audit 10/19)
- NFL concentration confirmed (trailing-20 63.2% vs 55% re-open trigger); NFL away 13-5 (n=19) stays a preliminary sub-slice.
- No approach cut: line-movement (5-7, 0b/5l CLV) is failing both metrics but n=12 — if it reaches 20 still failing both, it gets demoted; model-edge 6% bar stays (7-7, 67% CLV — mixed); fpi-chalk stays demoted (0-3); brand-tax fade stays (5-3, +4.78u, preliminary).
- Home-side 6% bar stays (home 21-27/43.8% vs away 41-27/60.3% — split persists, the bar is doing its job).
- Brand-tax fade/back rules stand (fading 10-4 vs backing 3-4 — preliminary, directionally strong).
- Totals (20-25, 44.4%, n=45) on watch: if it reaches 50 legs under 45%, totals get the 6% bar too.
- WNBA (6-8) and NHL (13-13) stay as watched newcomers; dip-buy n=1, no verdict.
- Props: no graduations, no kills — no pattern at 3+ instances. Keep hunting; 'struggling-QB passing under vs elite pass D' (0-2) is one loss from the kill line.
- The 9/28 close-capture rule is violated for the third straight review (75/164 missing). Not rewritten — it needs enforcing: the morning settle pass must backfill every close or flag the leg.
