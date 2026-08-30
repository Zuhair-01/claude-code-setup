---
name: opentrade-chart-analyst
description: >
  Full TradingView chart analysis via CDP. Use when user asks for chart analysis,
  market read, technical analysis, price action, bias, or "what's the chart saying."
  Covers structure, momentum, levels, volume, divergence, and multi-TF confirmation.
  Improved from OpenTrade v1 — adds divergence, session context, volume integration,
  and ICT-aware level classification.
---

# Chart Analysis Skill (OpenTrade Enhanced)

Execute every step in order. Never skip. Record values before interpreting.

---

## Step 1 — Session & Chart State

```
chart_get_state
```

Record: symbol, timeframe, chart type, all indicator names + entity IDs.

Then establish session context:
- What NY session phase are we in? (Pre-market / AM session / Lunch / PM / After-hours)
- Is this a Monday open / Friday close / FOMC day / earnings day?
- Has there been an overnight gap? (Compare chart open to prior close)

---

## Step 2 — Real-Time Quote

```
quote_get
```

Record: last price, open, high, low, volume, change%. Note if volume is above/below average.

---

## Step 3 — OHLCV Structure Read

```
data_get_ohlcv (count: 100, summary: false)
```

From the last 100 bars identify:
- **Swing highs / swing lows** (last 3 pivot points each direction)
- **Higher highs + higher lows** → uptrend structure
- **Lower highs + lower lows** → downtrend structure
- **Equal highs / equal lows** → potential liquidity pools (ICT concept — stops cluster here)
- **Last 5 bars direction** and body-to-wick ratio (strong closes vs. rejection wicks)
- **Average volume** over 20 bars; flag any bar with >1.5× average as "volume event"

---

## Step 4 — Indicator Values

```
data_get_study_values
```

Record every numeric value, then interpret with **trend context** (not in isolation):

**RSI:**
- In uptrend: RSI 40–80 is normal range. Oversold = 40–50 (buy dips). >80 = exhaustion.
- In downtrend: RSI 20–60 is normal. Overbought = 50–60 (sell rallies). <20 = exhaustion.
- In ranging market: standard 30/70 thresholds apply.
- **Divergence check**: If price makes new high but RSI makes lower high → bearish divergence (weakening momentum). If price makes new low but RSI makes higher low → bullish divergence (selling pressure fading). ALWAYS check this.

**MACD:**
- Histogram direction + momentum (growing or shrinking)
- Line crossover above/below signal line
- **Divergence**: MACD histogram making lower peaks while price makes higher highs = bearish hidden weakness

**EMAs / SMAs:**
- Price above all EMAs → bullish structure
- EMAs in order (fast > medium > slow) → trend alignment
- EMA compression (all within 0.5%) → coiling, potential expansion incoming
- **EMA slope**: flat = ranging, rising = trending, diverging = accelerating

**Bollinger Bands (if loaded):**
- Price at upper band + RSI >70 in downtrend = high-probability fade
- Band squeeze (width < 1%) = breakout imminent
- Walk along the band = strong trend, not a fade signal

**ATR:** Record absolute value and compare to 20-bar average. If current ATR > 1.5× average → elevated volatility session.

---

## Step 5 — Key Levels (Pine Lines, Labels, Boxes)

```
data_get_pine_lines (no study_filter)
data_get_pine_labels (no study_filter)
data_get_pine_boxes (if any visible)
data_get_pine_tables (if any table indicators)
```

Classify every level by type and proximity to current price:

| Level Type | ICT Classification | Action |
|------------|-------------------|--------|
| Equal highs / prior day high | Buyside liquidity | Price often sweeps before reversing |
| Equal lows / prior day low | Sellside liquidity | Same — sweep then reverse |
| VAH, PDH, ODH (labeled) | Premium zone | Sell from here in downtrend |
| VAL, PDL, ODL (labeled) | Discount zone | Buy from here in uptrend |
| POC | Fair value | Magnet for price in ranges |

**Immediate zone** (within 0.5%): High probability interaction this session.
**Key zone** (0.5–2%): Major magnet for next 1–3 sessions.
**Extended zone** (>2%): Swing target / stop hunt destination.

---

## Step 6 — Volume Analysis

From the OHLCV data already pulled:
- **Volume trend**: rising, falling, or flat over last 10 bars?
- **Volume at key moves**: did the breakout/breakdown have above-average volume? If price moved big on low volume → suspect move, likely to retrace.
- **Climactic volume**: single bar with >2× average + long wick → exhaustion, potential reversal.
- **Volume dry-up**: 3+ bars of below-average volume before a key level → accumulation/distribution.

---

## Step 7 — Screenshot

```
capture_screenshot (region: "chart")
```

---

## Step 8 — Multi-Timeframe Bias (Quick Check)

Only switch timeframes if needed to resolve conflicting signals. Always return to original TF.

```
chart_set_timeframe ({one_TF_higher})
data_get_study_values
data_get_ohlcv (summary: true)
chart_set_timeframe ({original})
```

Higher TF bias = directional filter. Only take trades aligned with higher TF.

---

## Step 9 — Final Report

```
=== 📊 CHART ANALYSIS: {SYMBOL} {TIMEFRAME} ===

SESSION: {AM/PM/London/Asia} | {Monday/OpEx/FOMC/Regular}

PRICE ACTION
  Last:    {price} | Change: {change%}
  Range:   {low} — {high} | Volume: {volume} ({above/below avg})
  Structure: {BULLISH / BEARISH / RANGING}
  Trend:   {Higher highs + higher lows / Lower highs + lower lows / Coiling}

KEY LEVELS
  🔴 Resistance / Buyside Liquidity:  {level1} ({distance}%), {level2}
  🟢 Support / Sellside Liquidity:    {level3} ({distance}%), {level4}
  ⚪ Fair Value / POC:                {level}

INDICATORS
  RSI({period}):   {value} → {signal in trend context}
  MACD:           {line}/{signal} | Histogram: {growing/shrinking}
  EMA Alignment:  {bullish stack / bearish stack / compressed}
  ATR:            {value} ({vs avg: normal/elevated/compressed})

DIVERGENCE
  RSI Divergence:   {BULLISH / BEARISH / NONE}
  MACD Divergence:  {BULLISH / BEARISH / NONE}

VOLUME
  Volume Trend:  {Rising / Falling / Flat}
  Last Big Move: {above/below} average volume → {confirms/suspects move}

HTF BIAS:  {BULLISH / BEARISH / NEUTRAL} ({timeframe} context)

BIAS:      {BULLISH / BEARISH / NEUTRAL}
RATIONALE: {one sentence combining structure + momentum + levels + divergence}

WATCH FOR:  {specific price/signal that would flip the bias}
```
