---
name: opentrade-risk
description: >
  Standalone risk management and position sizing calculator. Covers ATR-based stops,
  Kelly sizing, daily loss limits, portfolio heat, drawdown management, and risk journal.
  Use when user asks "how much should I risk", "what's my position size",
  "am I risking too much", "risk management", or "how do I size this trade."
  This is a NEW standalone skill — OpenTrade v1 only embedded risk as a sub-section
  of other skills, making it hard to use independently.
---

# Risk Management Skill (OpenTrade — New)

Risk management is not optional. It is the only thing that determines whether you survive
long enough to be profitable. Apply this before every trade.

---

## Step 1 — Account & Session State

Establish this at the start of every trading session:

**Account:**
- Account size: ${account}
- Max risk per trade: {%} (default recommendation: 1%)
- Max daily loss: {%} (default: 3% of account — if hit, stop trading today)
- Trades taken today: {N} / {daily_max}
- P&L today: ${daily_pnl} ({%})

**If daily loss limit already hit:** Output "TRADING SUSPENDED TODAY. Max daily loss of {%} reached. Resume tomorrow." No further analysis needed.

---

## Step 2 — Position Size Calculator

Inputs required:
1. Entry price
2. Stop price (must be thesis-based, not arbitrary)
3. Account size
4. Risk % per trade

```
Stop distance = |Entry - Stop| / Entry × 100  (in %)
Dollar risk = Account × Risk%
Position size (shares) = Dollar risk / (Entry × Stop%)
Position size (contracts) = Dollar risk / (Stop points × Contract point value)
```

**Check against these hard limits before accepting:**
- Dollar risk ≤ Max risk per trade (never override)
- Position size × Entry ≤ 30% of account (avoid overconcentration)
- If this trade + open positions > 60% of account → reduce to fit

**Output:**
```
Entry:     ${entry}
Stop:      ${stop} (−{distance}%)
Dollar at risk: ${risk}
Position size:  {N shares} or {N contracts}
Total exposure: ${exposure} ({%} of account)
```

---

## Step 3 — ATR-Based Stop Calculation

If user hasn't specified a stop price, calculate one using ATR:

```
chart_get_state
data_get_study_values  → get ATR(14)
data_get_ohlcv (count:20, summary:true)  → get recent range
```

**ATR multiplier by style:**
| Style | ATR Multiplier | Description |
|-------|---------------|-------------|
| Scalp (< 1h) | 1.0–1.5× ATR | Tight stop, high precision required |
| Day trade | 1.5–2.0× ATR | Balanced |
| Swing (multi-day) | 2.0–3.0× ATR | Gives position room to breathe |
| Position (weeks) | 3.0–4.0× ATR | Wide stop, smaller size |

**Stop placement:**
- Long trade: Entry − (ATR × multiplier) = stop price
- Short trade: Entry + (ATR × multiplier) = stop price

**Reject any setup where ATR-based stop = risk > 2× your target risk per trade.** The stop is too wide — reduce position size or skip.

---

## Step 4 — Kelly Criterion (Sanity Check on Size)

If you know your strategy's historical win rate and R:R:

```
Kelly % = W − (1−W) / R

Where:
  W = win rate (as decimal, e.g. 0.55)
  R = average win / average loss ratio
```

Use **Half Kelly** maximum. Never bet Full Kelly in live trading.

```
Recommended max risk = MIN(Half Kelly %, Max risk per trade %)
```

If Half Kelly < 0.5% → signal quality is poor. Reduce size to 0.25% or skip.

---

## Step 5 — Portfolio Heat Check

Before entering any new trade:

1. List all open positions
2. Calculate total portfolio exposure: sum of (size × entry) across all positions
3. Calculate total dollars at risk: sum of (size × stop distance) across all positions
4. Check correlation: are 2+ open positions in the same sector or moving together?

**Heat limits:**
| Condition | Action |
|-----------|--------|
| Total $ at risk > 5% of account | Reduce new trade size |
| Single sector > 40% of exposure | Cap new same-sector trades |
| 3+ correlated positions open | No new trade in same direction |
| 2+ losing positions today | Reduce all new sizes by 50% |
| Daily drawdown > 2% | Reduce all new sizes by 50% |
| Daily drawdown > 3% | STOP TRADING TODAY |

---

## Step 6 — Drawdown Management Protocol

Track your running drawdown from peak account value:

```
Peak account = highest account value reached
Current drawdown = (Peak - Current) / Peak × 100
```

**Response by drawdown level:**
| Drawdown | Response |
|----------|----------|
| 0–5% | Normal trading — no change |
| 5–10% | Reduce position sizes by 25% |
| 10–15% | Reduce by 50%. Only A+ setups. |
| 15–20% | Reduce by 75%. 1 trade per day max. |
| >20% | Stop trading. Review strategy. Do not add capital yet. |

Drawdown psychology note: The biggest mistake is increasing size after losses to "make it back." This is the fastest path to blowing the account. Reduce when losing, not increase.

---

## Step 7 — Risk Journal (After Each Trade)

Record these immediately after closing each trade:

```
Date/time:      {datetime}
Symbol:         {sym}
Direction:      {L/S}
Entry:          ${entry}
Exit:           ${exit}
Stop planned:   ${stop}
Stop hit:       {yes/no}
R outcome:      {+2.1R / -1R / etc.}
P&L:            ${pnl}
Thesis:         {one sentence — was the setup valid?}
Execution:      {did I follow the rules?}
Lesson:         {what to improve next time}
```

Review the journal weekly. Patterns will emerge:
- Am I cutting winners too early?
- Am I letting losers run past my stop?
- Do I trade worse at specific times?
- Does a specific setup have poor results?

---

## Step 8 — Risk Summary Output

```
=== RISK MANAGEMENT: {SYMBOL} ===

ACCOUNT STATE
  Size:         ${account}
  Daily P&L:    ${pnl} ({%}) | Status: {ACTIVE / SUSPENDED}
  Trades today: {N}/{max}

POSITION SIZING
  Entry:        ${entry}
  Stop:         ${stop} (−{distance}%)
  ATR-based:    ${atr_stop} (multiplier: {N}×)
  Dollar risk:  ${risk} ({risk%} of account)
  Position:     {N shares / N contracts}
  Exposure:     ${exposure} ({%} of account)

KELLY CHECK
  Strategy W%:  {W}% | R: {R}
  Half Kelly:   {hk}%
  Final risk:   {MIN(hk, max_risk)}%

PORTFOLIO HEAT
  Open positions: {N}
  Total $ at risk: ${total_risk} ({%} of account)
  Correlated:     {yes — reduce / no — OK}
  Heat status:    {NORMAL / ELEVATED / CRITICAL}

DRAWDOWN STATUS
  Peak:         ${peak}
  Current:      ${current}
  Drawdown:     {%} → {NORMAL / -25% SIZE / -50% SIZE / STOP TRADING}

VERDICT:  {PROCEED with {N shares} / REDUCE SIZE to {N} / SKIP — heat too high}
```
