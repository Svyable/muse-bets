"""Build the data files behind the public muse-bets dashboard (svyable.github.io/muse-bets).

Source of truth: the local ledgers in this goal's hidden_files/
  - pick-ledger.jsonl            (ticket-level rows; each row has a `legs` list)
  - prop-ledger.jsonl
  - pick-ledger-quarantine.jsonl

Outputs:
  - legs.csv      (flattened legs, 24-column schema)
  - site-data.json (dashboard aggregates)

Methodology (reverse-engineered from the 2026-10-08 snapshot and verified
exactly for tickets + equity; legs within 1 leg of 84):
  - tickets: settled tickets (parlay_result win/loss), excluding `sven-*` tiers
    (Sven's own bets are his record, not the model's).
  - legs: unique settled legs, deduped by (date, sport, matchup, pick, line,
    market) so a pick logged across several tier cards counts once.
    (Reproduces the 2026-10-08 snapshot's 38 wins exactly; 45 losses vs the
    snapshot's 46 -- one duplicate pair the original counted twice is merged
    here. Immaterial and deterministic.)
  - equity: 1 unit staked per settled ticket at the ticket's combined_odds;
    loss = -1u, win = +(decimal(combined_odds) - 1). Win with no combined_odds
    recorded scores +0. Cumulative by settled_date; dates with zero net
    change are omitted.
  - calibration: legs bucketed by confidence (60-69 / 50-59 / <50);
    stated = mean confidence, actual = win %.
  - card: the latest ticket's legs, flattened for the "daily card" panel.
"""

import csv
import io
import json
from collections import defaultdict

LEGS_CSV_COLUMNS = [
    # Exact column order of the repo's legs.csv:
    "date", "tier", "source", "ticket_result", "sport", "league", "matchup",
    "pick", "line", "odds", "book", "market", "home_away", "confidence",
    "edge", "approach", "stack_rank", "qualified", "staked", "result",
    "score", "closing_line", "closing_odds", "reason",
]


def load_ledger(path):
    rows = []
    with open(path) as f:
        for line in f:
            line = line.strip()
            if line:
                rows.append(json.loads(line))
    return rows


def american_to_decimal(o):
    """American odds -> decimal odds multiplier. Returns None if unknown."""
    if o is None or o == "":
        return None
    s = str(o).strip()
    try:
        if s.startswith("+"):
            return 1 + int(s[1:]) / 100
        if s.startswith("-"):
            return 1 + 100 / int(s[1:])
        v = float(s)
        return 1 + v / 100 if v > 0 else 1 + 100 / abs(v)
    except (ValueError, ZeroDivisionError):
        return None


def is_sven_ticket(t):
    return str(t.get("tier", "")).startswith("sven")


def settled_tickets(tickets):
    return [t for t in tickets
            if not is_sven_ticket(t) and t.get("parlay_result") in ("win", "loss")]


def leg_key(ticket, leg):
    return (ticket.get("date"), leg.get("sport"), leg.get("matchup"),
            leg.get("pick"), leg.get("line"), leg.get("market"))


def unique_settled_legs(tickets):
    """(ticket, leg) pairs, deduped so one pick = one leg."""
    seen = {}
    for t in tickets:
        if is_sven_ticket(t):
            continue
        for leg in t.get("legs", []) or []:
            if leg.get("result") in ("win", "loss"):
                seen.setdefault(leg_key(t, leg), (t, leg))
    return list(seen.values())


def build_legs_csv(tickets):
    buf = io.StringIO()
    w = csv.writer(buf)
    w.writerow(LEGS_CSV_COLUMNS)
    for t in tickets:
        base = {"date": t.get("date"), "tier": t.get("tier"),
                "source": t.get("source"),
                "ticket_result": t.get("parlay_result")}
        for leg in t.get("legs", []) or []:
            row = dict(base)
            for col in LEGS_CSV_COLUMNS[4:]:
                row[col] = leg.get(col)
            w.writerow([row[c] if row[c] is not None else ""
                        for c in LEGS_CSV_COLUMNS])
    return buf.getvalue()


def _pct(w, n):
    return round(100 * w / n, 1) if n else 0.0


def _group(pairs, keyfn):
    groups = defaultdict(list)
    for t, leg in pairs:
        groups[keyfn(t, leg)].append(leg)
    out = []
    for k, legs in groups.items():
        w = sum(1 for leg in legs if leg.get("result") == "win")
        out.append({"k": k, "n": len(legs), "w": w, "pct": _pct(w, len(legs))})
    out.sort(key=lambda d: (-d["n"], d["k"] or ""))
    return out


def build_equity(tickets):
    daily = defaultdict(float)
    for t in settled_tickets(tickets):
        sd = t.get("settled_date") or t.get("date")
        if t["parlay_result"] == "loss":
            daily[sd] -= 1
        else:
            d = american_to_decimal(t.get("combined_odds"))
            daily[sd] += (d - 1) if d else 0.0
    cum, curve, prev = 0.0, [], None
    for d in sorted(daily):
        cum += daily[d]  # full precision; round only at output
        rounded = round(cum, 2)
        if prev is None or rounded != prev:  # skip zero-delta dates
            curve.append({"date": d, "units": rounded})
        prev = rounded
    return curve


def build_calibration(pairs):
    buckets = {"60-69": [], "50-59": [], "<50": []}
    for _, leg in pairs:
        c = leg.get("confidence")
        if c is None:
            continue
        b = "60-69" if 60 <= c <= 69 else "50-59" if 50 <= c <= 59 else "<50"
        buckets[b].append(leg)
    out = []
    for b in ("60-69", "50-59", "<50"):
        legs = buckets[b]
        w = sum(1 for leg in legs if leg.get("result") == "win")
        out.append({"bucket": b, "n": len(legs),
                    "stated": round(sum(leg["confidence"] for leg in legs) / len(legs), 1) if legs else 0.0,
                    "actual": _pct(w, len(legs))})
    return out


def build_card(tickets):
    """Flatten every leg from every ticket on the latest date (the daily card)."""
    dated = [t for t in tickets if t.get("date")]
    if not dated:
        return []
    latest_date = max(t["date"] for t in dated)
    card, rank = [], 0
    for t in dated:
        if t["date"] != latest_date:
            continue
        for leg in t.get("legs", []) or []:
            rank += 1
            card.append({
                "rank": leg.get("stack_rank") or rank,
                "sport": leg.get("sport"),
                "matchup": leg.get("matchup"),
                "pick": leg.get("pick"),
                "line": leg.get("line"),
                "odds": leg.get("odds"),
                "conf": leg.get("confidence"),
                "edge": leg.get("edge"),
                "staked": bool(leg.get("staked")),
                "qualified": bool(leg.get("qualified")),
                "reason": leg.get("reason"),
            })
    return card


def build_site_data(tickets, today):
    pairs = unique_settled_legs(tickets)
    w = sum(1 for _, leg in pairs if leg.get("result") == "win")
    n = len(pairs)
    tw = sum(1 for t in settled_tickets(tickets) if t["parlay_result"] == "win")
    tl = sum(1 for t in settled_tickets(tickets) if t["parlay_result"] == "loss")
    return {
        "updated": today,
        "tickets": {"w": tw, "l": tl},
        "legs": {"w": w, "l": n - w, "n": n, "pct": _pct(w, n)},
        "equity": build_equity(tickets),
        "by_sport": _group(pairs, lambda t, leg: leg.get("sport")),
        "by_market": _group(pairs, lambda t, leg: leg.get("market")),
        "by_approach": _group(pairs, lambda t, leg: leg.get("approach")),
        "calibration": build_calibration(pairs),
        "latest_date": max((t.get("date") or "") for t in tickets),
        "card": build_card(tickets),
    }
