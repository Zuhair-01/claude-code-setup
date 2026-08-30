---
name: opentrade-macro
description: >
  Top-down macro regime analysis using cross-asset TradingView data.
  Classifies growth + inflation quadrant, identifies sector rotation,
  maps factor exposure, and derives asset allocation tilts.
  Use when user asks for "macro analysis", "regime", "what's the macro doing",
  "sector rotation", "risk on / risk off", or "where to allocate."
  Improved from OpenTrade v1 — quantified scoring thresholds, practical CDP workflow,
  regime timing guidance, and realistic cross-asset switching process.
---

# Macro Regime Analysis Skill (OpenTrade Enhanced)

## Important: CDP Limitation Note
TradingView CDP can only view **one chart at a time**. Cross-asset analysis requires
switching symbols sequentially. This takes ~2–3 minutes. The payoff is a complete
macro picture that most retail traders never build.

---

## Step 1 — Cross-Asset Snapshot

Pull each asset in sequence. Record only the essential metrics — don't linger.

For each symbol: `chart_set_symbol ({sym})` → `quote_get` → `data_get_ohlcv (count:20, summary:true)` → record 20-bar return and trend direction.

**Equity Risk:**
- SPY (S&P 500): {20-bar return}, {above/below 200d MA}
- QQQ (Nasdaq): {20-bar return}
- IWM (Russell 2000 — risk appetite proxy): {return}
- VIX (volatility): {current level}

**Bonds / Rates:**
- TLT (20Y Treasury): {return} — falling TLT = rates rising
- HYG (High Yield): {return} — rising HYG = credit risk appetite on

**Commodities:**
- GLD (Gold): {return} — rising = inflation hedge demand or risk-off
- USO (Oil): {return} — rising = demand-driven growth or supply shock

**Dollar:**
- UUP (Dollar index): {return} — rising dollar = risk-off, commodity headwind

**Crypto (if relevant):**
- BTC: {return} — leading risk indicator for crypto correlation

---

## Step 2 — Regime Scoring (Quantified)

Score each factor from -2 to +2 using the specific rules below:

### Growth Score (−2 to +2)
| Condition | Score |
|-----------|-------|
| SPY 20-bar return > +5% AND IWM outperforming | +2 |
| SPY 20-bar return > +2%, IWM mixed | +1 |
| SPY flat ±2%, mixed signals | 0 |
| SPY 20-bar return −2 to −5% | −1 |
| SPY 20-bar return < −5% OR IWM > 5% underperform | −2 |

### Inflation Score (−2 to +2)
| Condition | Score |
|-----------|-------|
| GLD > +5% AND USO > +5% AND TLT < −3% | +2 (hot inflation) |
| GLD up, USO up, TLT flat/down | +1 |
| Mixed commodity / rate signals | 0 |
| GLD and USO falling, TLT rising | −1 (deflationary) |
| All three pointing deflationary strongly | −2 |

### Risk Appetite Score (−2 to +2)
| Condition | Score |
|-----------|-------|
| VIX < 15 AND HYG rising AND IWM > SPY | +2 |
| VIX < 20, HYG stable | +1 |
| VIX 20–25 | 0 |
| VIX 25–35 OR HYG falling | −1 |
| VIX > 35 | −2 |

### Dollar Score (−2 to +2)
| Condition | Score |
|-----------|-------|
| UUP 20-bar return > +3% | +2 (strong dollar headwind for EM, commodities) |
| UUP 0–3% | +1 |
| UUP flat ±0.5% | 0 |
| UUP −1 to −3% | −1 (weak dollar tailwind) |
| UUP < −3% | −2 |

---

## Step 3 — Quadrant Classification

Map Growth score vs. Inflation score:

| Growth | Inflation | Regime | Characteristics |
|--------|-----------|--------|----------------|
| Positive | Low | **GOLDILOCKS** | Best for equities, growth beats value |
| Positive | High | **OVERHEATING** | Commodities win, rates rising, rotation to value |
| Negative | High | **STAGFLATION** | Worst for stocks; gold, energy outperform |
| Negative | Low | **DEFLATION/RECESSION** | Bonds win, defensives, gold, cash |

**Current regime: {QUADRANT}**

Note: Regimes typically last **6–18 months** at the macro level. Mid-cycle transitions (growth turning) typically signal 2–4 months before price action confirms it clearly. Watch for inflection, not confirmation lag.

---

## Step 4 — Sector Rotation by Regime

**GOLDILOCKS** (Growth+, Inflation−):
- Overweight: XLK (Tech), XLY (Consumer Discretionary), XLC (Comms)
- Neutral: XLF (Financials), XLI (Industrials)
- Underweight: XLE (Energy), GLD, XLU (Utilities), XLP (Consumer Staples)

**OVERHEATING** (Growth+, Inflation+):
- Overweight: XLE (Energy), XLB (Materials), XLF (Financials — rates benefit)
- Neutral: XLI (Industrials), XLK
- Underweight: XLU, XLP, TLT

**STAGFLATION** (Growth−, Inflation+):
- Overweight: GLD, XLE, XLB, cash
- Neutral: XLP, XLV (Healthcare — defensive)
- Underweight: XLK, XLY, XLC, TLT

**DEFLATION/RECESSION** (Growth−, Inflation−):
- Overweight: TLT (long bonds), XLU, XLP, XLV, GLD
- Neutral: Cash
- Underweight: XLK, XLY, XLE, XLF, all cyclicals

---

## Step 5 — Factor Tilt

Which equity factor dominates in this regime?

| Regime | Factor Tilt |
|--------|------------|
| Goldilocks | Momentum > Growth > Quality |
| Overheating | Value > Energy > Size (small/mid-cap lags) |
| Stagflation | Defensive Quality > Low Volatility > Value |
| Deflation | Low Volatility > Quality > Minimum Variance |

---

## Step 6 — Trade Ideas Derived from Regime

Generate 2–3 specific trade ideas that directly express the regime thesis:

**Idea format:**
- **Asset**: What to buy or short
- **Instrument**: ETF, futures, stock (match user's account type)
- **Thesis**: One sentence why this fits the regime
- **Entry**: Near or approach
- **Hedge**: What to pair against it to isolate the factor

---

## Step 7 — Full Macro Report

```
=== MACRO REGIME ANALYSIS: {DATE} ===

CROSS-ASSET SNAPSHOT
  SPY:   {ret}% (20-bar) | VIX: {level}
  IWM:   {ret}%          | HYG: {ret}%
  TLT:   {ret}%          | GLD: {ret}%
  USO:   {ret}%          | UUP: {ret}%

SCORING
  Growth:       {score} ({rationale})
  Inflation:    {score} ({rationale})
  Risk Appetite:{score} ({rationale})
  Dollar:       {score} ({rationale})

REGIME:  {GOLDILOCKS / OVERHEATING / STAGFLATION / DEFLATION}
Confidence: {HIGH if scores clearly in one quadrant / MODERATE if borderline}
Est. duration: {early / mid / late cycle — detail}

SECTOR CALLS
  Overweight:  {sectors}
  Neutral:     {sectors}
  Underweight: {sectors}

FACTOR TILT:  {Momentum / Value / Quality / Low-Vol}

KEY RISKS
  Bull case: {what would push the regime more positive}
  Bear case: {what would accelerate deterioration}
  Watch:     {specific upcoming catalyst — earnings season / FOMC / CPI print}

TRADE IDEAS
  1. {asset} — {thesis} — Entry: {price/zone} — Hedge: {instrument}
  2. {asset} — {thesis} — Entry: {price/zone} — Hedge: {instrument}
```
