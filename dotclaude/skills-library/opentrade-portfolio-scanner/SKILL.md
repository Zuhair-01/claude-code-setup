---
name: opentrade-portfolio-scanner
description: >
  Systematic multi-symbol scanner that ranks a watchlist by signal strength and
  identifies the highest-probability setups. Use when user asks to "scan my watchlist",
  "rank these symbols", "find the best setup", "screen for trades", or "portfolio scan."
  Improved from OpenTrade v1 — concrete scoring rubric, sector concentration check,
  missing-data handling, benchmark-relative strength, and tiered output.
---

# Portfolio Scanner Skill (OpenTrade Enhanced)

## Scope
Maximum 20 symbols per scan for speed. If user has more, ask which 20 to prioritize,
or split into two runs.

---

## Step 1 — Build Symbol List

```
chart_get_state  → note current symbol and TF
```

Ask user (if not already given): "Give me your watchlist — up to 20 symbols."

Also note: What sector does each symbol belong to? Group them now:
- Tech, Financials, Energy, Healthcare, Consumer, Crypto, Indices, FX, Commodities

This prevents recommending 5 correlated tech names simultaneously.

---

## Step 2 — Batch Data Collection

For each symbol, switch chart and pull:

```
chart_set_symbol ({symbol})
quote_get                          → last price, change%, volume
data_get_ohlcv (count:50, summary:true)   → range, avg volume, 5-bar direction
data_get_study_values              → RSI, MACD, EMAs, ATR
data_get_pine_lines                → key levels
```

**Missing data handler:**
- If `quote_get` returns null or 0 price → skip symbol, log: "No data: {symbol}"
- If `data_get_study_values` returns empty → indicators not loaded; score as N/A on those dimensions, note in report
- Never assume a value — only score from confirmed data

---

## Step 3 — Composite Score (0–100)

Score each symbol on 5 dimensions, max 20 points each:

### Dimension 1: Momentum (0–20)
- 20: 20-bar return > +5%, 5-bar return > +1%, both positive
- 15: 20-bar return > +2%, 5-bar positive
- 10: 20-bar return > 0%, 5-bar mixed
- 5: Mixed signals, slight positive bias
- 0: 20-bar return negative

### Dimension 2: RSI Condition (0–20)
- 20: RSI 45–65 in uptrend (healthy momentum, not overbought)
- 15: RSI 35–45 in uptrend (oversold pullback = buy opportunity)
- 10: RSI 65–75 (overbought but still trending)
- 5: RSI < 35 (oversold but may indicate downtrend)
- 0: RSI > 75 (overbought in non-trending market) or RSI < 30 in downtrend

### Dimension 3: Volatility Profile (0–20)
- 20: ATR 1–2% daily (liquid, tradeable, not wild)
- 15: ATR 0.5–1% (low vol, stable)
- 10: ATR 2–3% (higher vol, needs wider stops)
- 5: ATR 3–5% (high vol, reduce size)
- 0: ATR > 5% (too volatile for normal sizing)

### Dimension 4: Volume Confirmation (0–20)
- 20: Recent volume >1.5× 20-bar average on upward moves
- 15: Volume above average with positive price action
- 10: Volume average, price moving
- 5: Volume declining with price moving (weak conviction)
- 0: Price moving on below-average volume (suspect move)

### Dimension 5: Trend Structure (0–20)
- 20: Price above 20/50/200 EMA, all EMAs in bullish order, recent HH/HL
- 15: Price above 20 and 50 EMA, structure intact
- 10: Price above 20 EMA only, mixed signals
- 5: Price below 20 EMA but above 50 EMA (pullback, possible entry)
- 0: Price below all EMAs or bearish LH/LL structure

**Total = sum of 5 dimensions (0–100)**

---

## Step 4 — Classification

| Score | Label | Action |
|-------|-------|--------|
| 80–100 | STRONG BUY | High conviction — scan for entry trigger now |
| 65–79 | BUY | Good setup — add to active watchlist |
| 50–64 | WATCH | Developing — revisit in 1–2 sessions |
| 35–49 | NEUTRAL | No edge — skip unless specific reason |
| 20–34 | AVOID | Weak setup — don't force a trade |
| 0–19 | SHORT CANDIDATE | Consider if you trade short |

---

## Step 5 — Benchmark Relative Strength

Compare each symbol to SPY (equities) or BTC (crypto) benchmark:

```
chart_set_symbol (SPY or BTC-USD or BTCUSDT)
data_get_ohlcv (count:20, summary:true)
```

Calculate:
```
RS = Symbol 20-bar return / Benchmark 20-bar return
```

- RS > 1.3 → Significantly outperforming → add 5 bonus points to score
- RS 1.0–1.3 → Outperforming → no adjustment
- RS 0.7–1.0 → Underperforming → subtract 5 points
- RS < 0.7 → Significantly underperforming → subtract 10 points

---

## Step 6 — Sector Concentration Check

After ranking, before selecting setups:

- Count symbols per sector in the top 5
- If 3+ of top 5 are the same sector → sector clustering risk
- In that case: keep only the top 1–2 from that sector, replace others with next-best from different sectors

This prevents all your setups being correlated and blowing up together when the sector rotates.

---

## Step 7 — Top 3 Setup Detail

For the top 3 symbols by score:

```
chart_set_symbol ({top_symbol})
data_get_ohlcv (count:50, summary:false)
data_get_pine_lines
data_get_pine_labels
capture_screenshot (region: "chart")
```

For each:
- Entry zone: Where to buy? (At a key level, not chase)
- Stop: Below key support / OB (not arbitrary)
- Target: Next resistance / liquidity level
- R:R (must be ≥ 1.5)
- ATR-based position size (risk 1% of account / stop distance)

---

## Step 8 — Final Report

```
=== PORTFOLIO SCANNER: {N} symbols | {DATE} ===

RANKINGS
  Rank | Symbol | Score | Label       | Sector   | RS vs Bench
  -----|--------|-------|-------------|----------|------------
  1    | {sym}  | {N}   | STRONG BUY  | Tech     | {x.x}
  2    | {sym}  | {N}   | BUY         | Crypto   | {x.x}
  ...

SECTOR CHECK
  Top 5 sector distribution: {Tech:2, Crypto:1, Energy:1, Fin:1}
  Concentration risk: {none / moderate — capped sector at 2}

SKIPPED / NO DATA: {sym1, sym2}

─────────────────────────────
TOP 3 SETUPS
─────────────────────────────

1. {SYMBOL} — Score: {N} | {LABEL}
   Entry zone:  {price range}
   Stop:        {price} | {%} risk
   Target:      {price} | {R}R
   Position:    {N shares} risking 1% of ${account}
   Trigger:     {specific signal to enter — don't chase}

2. {SYMBOL} — Score: {N} | {LABEL}
   [same format]

3. {SYMBOL} — Score: {N} | {LABEL}
   [same format]

─────────────────────────────
AVOID LIST: {symbols scoring <35, briefly why}
SHORT CANDIDATES: {symbols scoring <20 with weak structure}
```
