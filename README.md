# muse-bets

A sports-betting experiment run by Muse (Meta's personal AI agent) for Sven. Every pick is logged **before** the event with full schema — sport, matchup, market, line, odds + book, closing line, confidence %, edge tag, approach, reasoning — then graded on hit rate, ROI, CLV (closing-line value), and calibration. The loop's job is to find what works, not defend a method.

## Current scoreboard (updated 2026-10-08)

- **Tickets:** 8-35
- **Unique legs:** 38-45 (45.8%, n=83)
- **By sport:** NFL 16-10 (62%) · MLB 14-20 (41%) · CFB 4-7 (36%) · WNBA 2-7 (22%)
- **CLV:** positive for the first time (60% excl. pushes, Oct 5 review) — the process is beating the close

## How it works

- **Daily picks:** 20 stack-ranked legs every morning (ranks 1-5 = staked dogfood set tracked against an 80% hit-rate goal; ranks 6-20 = paper-trade learning tier, zero bankroll risk).
- **Concentration (the betting lesson):** volume goes to the best slice. NFL is the current best (16-10); on NFL slates the card builds NFL-first, on no-NFL slates it runs discovery mode across all sports.
- **Props discovery lane:** player props / alt lines / exotics are hunted for repeatably mispriced DraftKings action, logged separately, never mixed into the core binary-markets evidence.
- **Edge rule:** a leg only qualifies if model probability beats market implied probability by ≥4% (≥6% for marquee public brands and home sides).
- **Weekly review:** every Monday the ledger is audited on all metrics — approaches that don't earn their keep get cut. Full reviews in `docs/`.

## Repo layout

```
data/
  pick-ledger.jsonl            # every pick, full schema (source of truth)
  prop-ledger.jsonl            # props discovery lane
  pick-ledger-quarantine.jsonl # quarantined entries (never scored as evidence)
  legs.csv                     # flattened legs for easy analysis
  bet-matrix.xlsx              # dashboard: every ticket, leg, odds, result
docs/
  strategy.md                  # the living strategy doc + all rule changes
  weekly-review-2026-09-21.md
  weekly-review-2026-09-28.md
  weekly-review-2026-10-05.md
```

## Honesty notes

- The lottery tier went 0-11 (-100% ROI) and was suspended Oct 5.
- Edge estimates were found to be inflated (bigger claimed edge → worse hit rate); recalibration is in progress.
- About a third of legs are still missing closing-line data — a known process gap being closed.
- Stakes are tracked in units, not dollars. Nothing here is financial advice.
