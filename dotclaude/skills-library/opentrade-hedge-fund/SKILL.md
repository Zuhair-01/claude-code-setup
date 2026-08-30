---
name: opentrade-hedge-fund
description: >
  Institutional hedge fund trade analysis. Multi-timeframe confluence, Kelly sizing,
  portfolio heat check, trade structure selection. Use when user asks for "hedge fund
  analysis", "institutional setup", "full trade plan", or "position sizing."
  Improved from OpenTrade v1 — fixes win rate estimation, removes $1M AUM assumption,
  adds quantified correlation check, realistic sizing for any account size.
---

# Hedge Fund Analysis Skill (OpenTrade Enhanced)

---

## Step 1 — Account & Context Setup

Before any analysis, establish:
1. **Account size** — if not specified, ask: "What's your account size in USD?"
2. **Max risk per trade** — default 1% of account unless user specifies
3. **Asset type** — equity, futures, crypto (affects sizing, fees, leverage)
4. **Holding period** — scalp (<1h), swing (1–10 days), position (weeks)

These four inputs are required for the Kelly calculation to be meaningful.

---

## Step 2 — Multi-Timeframe Confluence Scan

Pull higher timeframes first. Always return to original TF when done.

```
chart_get_state              → record current symbol + TF
data_get_ohlcv (count:100, summary:false) → full price action
data_get_study_values        → all indicators
data_get_pine_lines          → key price levels
data_get_pine_labels         → annotated levels
```

**Switch to Monthly (M):**
```
chart_set_timeframe (M)
data_get_ohlcv (summary:true)
data_get_study_values
```

**Switch to Weekly (W):**
```
chart_set_timeframe (W)
data_get_ohlcv (summary:true)
data_get_study_values
data_get_pine_lines
```

**Switch to Daily (D):**
```
chart_set_timeframe (D)
data_get_ohlcv (summary:true)
data_get_study_values
data_get_pine_lines
data_get_pine_labels
```

**Switch to Entry TF (60m or 15m):**
```
chart_set_timeframe (60)
data_get_ohlcv (count:50, summary:false)
```

Return to original TF.

---

## Step 3 — Signal Matrix Scoring

Score each timeframe **-2 to +2** using this rubric (not gut feel):

| Score | Conditions |
|-------|-----------|
| +2 | Structure bullish (HH/HL) + EMA bullish stack + RSI 50-70 + MACD positive + volume confirms |
| +1 | 3 of 5 above conditions met |
| 0 | Conflicting signals, RSI 45-55, ranging EMAs |
| -1 | 3 of 5 bearish conditions met |
| -2 | Structure bearish (LH/LL) + EMA bearish stack + RSI 30-50 + MACD negative + volume confirms |

| Timeframe | Score | Key Signal |
|-----------|-------|-----------|
| Monthly | {-2 to +2} | {signal} |
| Weekly | {-2 to +2} | {signal} |
| Daily | {-2 to +2} | {signal} |
| Entry TF | {-2 to +2} | {signal} |
| **COMPOSITE** | **{avg}** | **{bias}** |

**Decision rule:**
- Composite > 1.0 → Long bias
- Composite < -1.0 → Short bias
- -1.0 to 1.0 → No edge. Pass. Do not force a trade.

---

## Step 4 — Trade Setup: Entry, Stop, Targets

**Entry Zone:** Where do you initiate? Must be at a structural level (support, prior high reclaimed, VWAP, key EMA), not arbitrary.

**Stop (Thesis-Based, NOT Arbitrary):**
The stop must be at a price that invalidates the trade thesis. Valid stop locations:
- Beyond the last swing low/high
- Below/above a key level that price should not return to if thesis is correct
- Beyond VWAP if the trade is based on VWAP positioning

Stop distance in % = (Entry - Stop) / Entry × 100

Reject any trade where stop is >3% (equities/crypto swing) or >1.5% (futures scalp) — too wide means position sizing gets too small to be meaningful.

**Targets:**
- T1 (50% of position): Next major level, 1.5–2R minimum
- T2 (30% of position): Extended level, 2.5–3R
- T3 (20% of position): Measured move / prior structure, 4R+

R multiple = Target distance / Stop distance.

Do not enter any trade with T1 < 1.5R. The math doesn't work.

---

## Step 5 — Win Rate Estimation (Calculated, Not Guessed)

Use composite signal score to estimate win rate:

| Composite Score | Historical Win Rate Estimate |
|----------------|------------------------------|
| ±2.0 | 60–65% |
| ±1.5 | 55–60% |
| ±1.0 | 50–55% |
| ±0.5 to 1.0 | 45–50% (marginal — reduce size) |
| <±0.5 | <45% — negative EV, do not trade |

Then check: Does the signal type have documented edge?
- Multi-TF confluence at key level → add 3–5%
- Trend trade (not counter-trend) → add 3%
- Counter-trend with divergence confirmation → neutral
- Counter-trend without confirmation → subtract 5%

**Expected Value:**
```
EV = (W × R) - (1 - W)
W = win rate decimal (e.g., 0.55)
R = average R multiple at T1
```

EV must be > 0.10 to trade. Below that, the signal is not worth the commission + execution risk.

---

## Step 6 — Kelly Position Sizing

```
Kelly % = W - (1 - W) / R
```

**Never use Full Kelly in live trading.** It assumes perfect win rate knowledge. Use:
- **Half Kelly** (base case): `kelly / 2`
- **Quarter Kelly** (if signal is borderline or high-vol regime): `kelly / 4`

**Convert to dollar risk:**
```
Dollar risk = Account Size × Kelly %
Max dollar risk = Account Size × Max Risk Per Trade %  (your hard cap, e.g. 1%)
Use: MIN(Kelly dollar risk, Max risk dollar risk)
```

**Convert to position size:**
```
Shares = Dollar risk / Stop distance in $
Contracts = Dollar risk / (Stop distance in points × Point value)
```

**Always state position size in concrete units, not just % — the user needs to know how many shares/contracts to buy.**

---

## Step 7 — Portfolio Heat Check

Ask or infer from context:
1. What other positions are currently open?
2. Are any open positions in the same asset class / macro factor?

**Heat rules (no guessing — apply mechanically):**
- Same direction as 2+ open positions in correlated assets → reduce size by 40%
- Adding to a sector already >15% of account → pass or hedge
- VIX > 30 or crypto Fear & Greed < 25 → cut all sizes by 50%
- Daily loss already > 2% of account → no new trades today

**Quick correlation check (use the data you already have):**
Pull the same indicator on SPY/BTC (whichever is the benchmark). If both your asset and the benchmark are making the same structure at the same time → correlated. Reduce size.

---

## Step 8 — Trade Structure Selection

| Expression | Use when | Cost |
|-----------|----------|------|
| Spot long/short | High conviction, any account size | Zero premium |
| Leveraged futures (0.5–1×) | Strong trend, liquid market | Low funding |
| Long call/put | Pre-earnings, binary event risk | Premium paid |
| Spread (call/put) | Reduce premium, cap upside/downside | Reduced |

Avoid options if holding period < 3 days (theta decay is punishing).
Avoid futures leverage > 3× for swing trades.

---

## Step 9 — Full Report

```
=== HEDGE FUND ANALYSIS: {SYMBOL} ===

ACCOUNT: ${account_size} | Max risk: {max_risk}% = ${max_risk_$}

MULTI-TIMEFRAME SIGNAL
  Monthly:   {score} — {signal}
  Weekly:    {score} — {signal}
  Daily:     {score} — {signal}
  Entry TF:  {score} — {signal}
  Composite: {score} → {LONG / SHORT / FLAT — NO EDGE}

TRADE SETUP
  Direction: {LONG / SHORT}
  Entry:     {price or zone} ({reason — structural level name})
  Stop:      {price} | {distance}% | Thesis: {what this invalidates}
  T1:        {price} — {R}R → Take 50% here
  T2:        {price} — {R}R → Take 30%
  T3:        {price} — {R}R → Take 20%

WIN RATE & EV
  Signal score: {composite}
  Est. win rate: {W}%
  R at T1: {R}
  Expected Value: {EV} per $1 risked → {trade / pass}

SIZING (Half Kelly)
  Kelly %:       {kelly}%
  Half Kelly:    {hk}%
  Dollar risk:   ${risk_$} (capped at ${max_risk_$})
  Position size: {N shares / N contracts} at ${entry}

PORTFOLIO HEAT
  Correlated exposure: {yes/no — detail}
  Sector concentration: {%}
  Regime risk modifier: {normal / -50% size due to high vol}
  Final size after heat: {N shares / N contracts}

STRUCTURE
  Expression: {spot / futures / call spread / etc.}

EXECUTION
  Entry trigger:  {specific candlestick/indicator condition to press buy}
  Hard stop:      GTC order at {stop_price}
  Partial exits:  {T1 price} → {T2 price} → {T3 price}
  Time stop:      Exit if thesis not playing after {N bars / N days}
  Invalidation:   If {specific thing happens}, exit regardless of P&L
```
