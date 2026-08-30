---
name: opentrade-ict
description: >
  ICT (Inner Circle Trader) methodology analysis via TradingView CDP.
  Covers market structure, liquidity sweeps, order blocks, fair value gaps,
  IFVG inversions, optimal trade entries, killzone timing, and PD arrays.
  Use when user mentions ICT, order blocks, FVG, OTE, liquidity sweep, killzone,
  smart money concepts, or "what would ICT do here."
  This is a NEW skill — OpenTrade v1 had no ICT methodology at all.
---

# ICT Methodology Skill (OpenTrade — New)

ICT is the most widely used retail-to-institutional framework. This skill applies it
rigorously using only TradingView data available through CDP tools.

---

## Step 1 — Session & Killzone Context

ICT trades are time-weighted. Check the session first:

```
chart_get_state
quote_get
```

**Valid killzones (high-probability ICT setups form here):**
| Killzone | Time (EST) | Focus |
|----------|-----------|-------|
| London Open | 02:00–05:00 | Sweep prior day lows/highs |
| NY AM Session | 09:30–11:30 | Primary entry window |
| NY Lunch | 12:00–13:00 | Avoid (stop hunts, low conviction) |
| NY PM Session | 13:30–16:00 | Secondary continuation |
| Asia Range | 20:00–00:00 | Sets the range for London to sweep |

**If outside a killzone:** State this explicitly. ICT setups outside killzones have materially lower probability. Reduce conviction accordingly.

---

## Step 2 — Market Structure (MSB / CHoCH)

```
data_get_ohlcv (count: 100, summary: false)
```

Identify:
- **Swing highs (SH)** and **swing lows (SL)**: A swing is a bar whose high/low is higher/lower than 2 bars on each side.
- **Higher highs (HH)** and **higher lows (HL)** → Bullish market structure
- **Lower highs (LH)** and **lower lows (LL)** → Bearish market structure
- **Market Structure Break (MSB)**: Price closes beyond the last significant swing point. This is a structural shift.
- **Change of Character (CHoCH)**: First MSB in the opposite direction after a trend. This signals a possible reversal.

Record the last 3 structure points and whether structure is intact or broken.

---

## Step 3 — Liquidity Identification

**Where are the stops?**

Retail traders place stops:
- Below swing lows (buyside stop below = **sellside liquidity**)
- Above swing highs (sellside stop above = **buyside liquidity**)
- Below/above round numbers (00, 50, 25 levels)
- At prior day high/low, prior week high/low
- At equal highs or equal lows (double tops/bottoms = obvious liquidity pools)

```
data_get_pine_labels  → look for PDH, PDL, PWH, PWL labels
data_get_pine_lines   → prior day/week levels
```

**ICT core concept:** Price does NOT respect support/resistance — it RUNS to liquidity pools, sweeps them (triggers stops), then reverses.

Identify:
- **Nearest buyside liquidity pool** (equal highs / prior session highs): {price}
- **Nearest sellside liquidity pool** (equal lows / prior session lows): {price}
- **Next HTF draw on liquidity**: Where is price most likely headed to sweep?

---

## Step 4 — Premium/Discount Array

**Current price relative to the dealing range:**

```
Dealing range = last major swing high to last major swing low
Midpoint (equilibrium) = (swing_high + swing_low) / 2
Current price % = (current - swing_low) / (swing_high - swing_low) × 100
```

| Position | Zone | ICT Action |
|----------|------|-----------|
| >75% of range | Premium | Look for shorts / sell limit orders |
| 50–75% | Upper neutral | Evaluate context |
| 25–75% | Equilibrium | Fair value — not ideal ICT entry |
| 25–50% | Lower neutral | Evaluate context |
| <25% of range | Discount | Look for longs / buy limit orders |

**OTE (Optimal Trade Entry):**
- Long OTE: 62–79% retracement of the last bullish impulse (Fibonacci 0.62–0.79)
- Short OTE: 62–79% retracement of the last bearish impulse

---

## Step 5 — Order Blocks (OB)

An order block is the last up-candle before a bearish displacement, or the last down-candle before a bullish displacement.

**Bullish OB (potential support):**
- Last bearish (red) candle before a strong bullish move
- Must have displacement after it (3+ consecutive bullish closes)
- Price returning to this OB = high probability long entry

**Bearish OB (potential resistance):**
- Last bullish (green) candle before a strong bearish move
- Must have displacement after it
- Price returning to this OB = high probability short entry

**OB validity rules:**
- Must be unmitigated (price has NOT traded back through it)
- Stronger if coincides with a FVG (see Step 6)
- Stronger if at a premium/discount extreme
- Weaker if it's the 3rd+ touch (liquidity often consumed by then)

```
data_get_ohlcv (count: 50, summary: false)
```

Scan for the last 3 unmitigated OBs in each direction.

---

## Step 6 — Fair Value Gaps (FVG) & IFVG

**Fair Value Gap:** A 3-candle pattern where bar 1's low is above bar 3's high (bullish FVG), or bar 1's high is below bar 3's low (bearish FVG). This gap is "inefficiency" — price tends to return and fill it.

**Bullish FVG:** candle[2].high < candle[0].low → gap between those two price levels
**Bearish FVG:** candle[2].low > candle[0].high → gap between those two price levels

**IFVG (Inversion):** An FVG that price trades through and then uses as support (bullish inversion) or resistance (bearish inversion). IFVGs are higher probability than raw FVGs.

**ICT priority of entries:**
1. IFVG + OB overlap (highest probability)
2. OB alone (high probability)
3. FVG alone (medium probability)
4. FVG partially filled (lower probability)

```
data_get_pine_boxes  → check if FVG indicator is loaded (will show boxes)
data_get_pine_lines  → check for drawn FVG levels
```

If no FVG indicator loaded: manually identify from OHLCV data as above.

---

## Step 7 — PD Array Stack (Power of 3 Concept)

PD Arrays = Price Delivery Arrays. Stack them in priority order for the current trade direction:

**For longs (price in discount):**
1. Bearish OB (now acting as support) → highest priority
2. Bullish FVG / IFVG
3. Equilibrium (50% of dealing range)
4. Prior swing low (liquidity swept and reversed)

**For shorts (price in premium):**
1. Bullish OB (now acting as resistance)
2. Bearish FVG / IFVG
3. Equilibrium
4. Prior swing high (liquidity swept and reversed)

The more PD arrays that stack at a single price, the higher the probability.

---

## Step 8 — Entry Model

**ICT 2022 Model (simplified for CDP execution):**

1. Higher timeframe (4H/Daily) identifies direction and draw on liquidity
2. Current TF confirms market structure break in that direction
3. Price retraces into PD array (OB / FVG in premium/discount zone)
4. Entry on: first candle that closes into the PD array, or first reversal candle inside OB
5. Stop: below the OB low (long) or above the OB high (short) — add 2 ticks buffer
6. Target: the identified liquidity pool / next PD array on the opposite side

**Minimum requirements to take a trade:**
- [ ] In a valid killzone (or strong reasoning to override)
- [ ] HTF structure aligned with trade direction
- [ ] Price in premium/discount (not equilibrium)
- [ ] At least one unmitigated OB or IFVG as entry
- [ ] R:R ≥ 2:1 to liquidity target

---

## Step 9 — Screenshot

```
capture_screenshot (region: "chart")
```

---

## Step 10 — ICT Analysis Report

```
=== ICT ANALYSIS: {SYMBOL} {TIMEFRAME} ===

SESSION
  Current time:  {time EST}
  Killzone:      {ACTIVE: NY AM / ACTIVE: London / OUTSIDE KILLZONE}
  Bias penalty:  {none / -30% conviction (outside killzone)}

MARKET STRUCTURE
  Trend:         {Bullish HH/HL / Bearish LH/LL}
  Last MSB:      {bullish / bearish} at {price} on {date}
  CHoCH:         {yes/no — detail}
  Structure:     {INTACT / BROKEN / SHIFTING}

LIQUIDITY
  Nearest buyside pool:   {price} ({equal highs / PDH / PWH})
  Nearest sellside pool:  {price} ({equal lows / PDL / PWL})
  HTF draw:               Price likely targeting {price} ({reason})

PREMIUM/DISCOUNT
  Dealing range:  {low} — {high}
  Equilibrium:    {mid}
  Current price:  {price} = {N}% of range → {PREMIUM / DISCOUNT / EQUILIBRIUM}

ORDER BLOCKS
  Bullish OBs (unmitigated): {price zones, strength}
  Bearish OBs (unmitigated): {price zones, strength}

FAIR VALUE GAPS
  Bullish FVGs:  {zones}
  Bearish FVGs:  {zones}
  IFVGs active:  {yes/no — price}

TRADE SETUP
  Direction:     {LONG / SHORT / NO SETUP}
  Entry zone:    {price range — PD array}
  Entry type:    {OB + IFVG / OB only / FVG only}
  Stop:          {price} ({pips/points} beyond OB)
  Target:        {price} ({liquidity pool / next PD array})
  R:R:           {ratio} — {TAKE / SKIP if <2:1}
  Killzone OK:   {YES / NO}
  Checklist met: {N/5 conditions}
  VERDICT:       {EXECUTE / WAIT / SKIP}
```
