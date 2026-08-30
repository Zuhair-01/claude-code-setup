---
name: opentrade-quant
description: >
  Quantitative statistical analysis of a market — return distribution, volatility regime,
  momentum score, mean reversion probability, Sharpe/Sortino, edge detection.
  Use when user asks for "quant analysis", "statistical edge", "regime detection",
  "is this trending or ranging", or "what does the data say."
  Improved from OpenTrade v1 — adds concrete formulas, data length requirements,
  Sharpe/Sortino/Calmar, specific regime thresholds, and Monte Carlo note.
---

# Quantitative Analysis Skill (OpenTrade Enhanced)

## Data Requirements
**Minimum:** 100 bars for statistical significance. 
**Ideal:** 200+ bars (covers multiple regime cycles).
Request this:
```
data_get_ohlcv (count: 200, summary: false)
```

If fewer than 100 bars available on the current timeframe, switch up one TF before running this analysis — note the substitution in your report.

---

## Step 1 — Return Distribution

Compute from OHLCV (close-to-close):

**Returns array:** `r[i] = (close[i] - close[i-1]) / close[i-1]`

Calculate:
- **Mean return (μ):** Average of last 20 returns. Positive = mild bullish drift.
- **Standard deviation (σ):** Annualized = `σ_daily × √252` (equities) or `× √365` (crypto)
- **Skewness:** Positive = right tail (more big up moves). Negative = left tail (more big crashes). |skew| > 1.0 is significant.
- **Kurtosis:** >3 = fat tails (black swan risk). Normal distribution = 3.

| Metric | Value | Interpretation |
|--------|-------|---------------|
| Mean return (20-bar) | {μ} | {positive drift / flat / negative drift} |
| Annualized vol | {σ}% | {low <15% / normal 15-30% / high >30%} |
| Skewness | {skew} | {right tail / symmetric / left tail} |
| Kurtosis | {kurt} | {fat tails / normal / thin tails} |

---

## Step 2 — Volatility Regime

```
5-bar realized vol  = stdev(returns, 5) × √252
20-bar realized vol = stdev(returns, 20) × √252
Ratio = 5-bar vol / 20-bar vol
```

| Ratio | Regime | Implication |
|-------|--------|-------------|
| > 1.4 | **Expanding** | Market stressed or trending strongly — momentum strategies work |
| 0.8–1.4 | **Normal** | Balanced — use confluence-based entries |
| < 0.8 | **Compressing** | Coiling — breakout setup forming, wait for expansion |

Also check ATR (already pulled):
- ATR above 20-bar ATR average: confirming expansion
- ATR below average for 5+ bars: coil in progress

---

## Step 3 — Momentum Score (Multi-Period)

Using returns data:
```
1-bar momentum  = last 1 return (r[0])
5-bar momentum  = sum of last 5 returns
20-bar momentum = sum of last 20 returns
```

Weight them:
```
Momentum score = (0.2 × sign(1-bar)) + (0.3 × sign(5-bar)) + (0.5 × sign(20-bar))
```

Score range: -1 to +1
- +0.8 to +1.0 → Strong momentum long — trend following works
- +0.3 to +0.8 → Moderate momentum — trade pullbacks, not breakouts
- -0.3 to +0.3 → No momentum — avoid directional trades
- -0.8 to -0.3 → Moderate short momentum
- -1.0 to -0.8 → Strong momentum short

**Corroborate with:** RSI trend alignment, EMA slope direction.

---

## Step 4 — Mean Reversion Detection

```
Z-score (20-bar) = (current_close - mean_20) / stdev_20
Autocorrelation (lag-1) = correlation(r[1:N], r[0:N-1])
```

**Z-score interpretation:**
- > +2.0 → Statistically overbought. 89% of price observations fall below this.
- +1.5 to +2.0 → Premium zone. Mean reversion odds rising.
- -1.5 to +1.5 → Normal range. Not mean-reversion territory.
- -1.5 to -2.0 → Discount zone. Potential long fade entry.
- < -2.0 → Statistically oversold.

**Autocorrelation:**
- > +0.1 → Positive autocorrelation → **Trending market** → use momentum strategies
- -0.1 to +0.1 → Random walk → no systematic edge, reduce position size
- < -0.1 → Negative autocorrelation → **Mean-reverting market** → use fade strategies

---

## Step 5 — Risk-Adjusted Return Metrics

Using 20-bar return data and σ:
```
Sharpe ratio (annualized) = (μ_daily × 252) / (σ_daily × √252) = (μ × √252) / σ
Sortino ratio = (μ × √252) / downside_deviation
  downside_deviation = stdev of only negative returns × √252
```

| Metric | Threshold | Interpretation |
|--------|-----------|---------------|
| Sharpe > 1.0 | Good | Reasonable risk-adjusted return |
| Sharpe > 2.0 | Excellent | Strong edge |
| Sharpe < 0.5 | Poor | Not worth trading this setup |
| Sortino > Sharpe | Positive | Upside volatility > downside volatility (good) |
| Sortino < Sharpe | Negative | More downside vol than upside vol (concerning) |

For drawdown:
- Max consecutive negative bars in last 50: {N}
- Max drawdown estimate: Max consecutive negative bars × avg negative return

---

## Step 6 — Regime Classification

Using all metrics above, classify:

| Regime | Conditions | Best Strategy |
|--------|-----------|---------------|
| **TRENDING UP** | Momentum score > +0.5, autocorr > +0.1, vol expanding | Trend following, hold winners |
| **TRENDING DOWN** | Momentum score < -0.5, autocorr > +0.1, vol expanding | Short trend following |
| **MEAN REVERTING** | Autocorr < -0.1, Z-score ±1.5+, vol normal | Fade extremes, quick exits |
| **LOW-VOL COILING** | Vol ratio < 0.8, momentum ≈ 0 | Wait for breakout, don't fade |
| **HIGH-VOL STRESSED** | Vol ratio > 1.4, σ > 30% ann. | Reduce size, use limit orders only |
| **CHOPPY/RANDOM** | Autocorr ≈ 0, no momentum, normal vol | Stay out. No edge. |

---

## Step 7 — Final Report

```
=== QUANTITATIVE ANALYSIS: {SYMBOL} {TIMEFRAME} ===
Data: {N} bars | Period: {date range}

RETURN DISTRIBUTION
  Mean return (20-bar): {μ}%
  Annualized vol:       {σ}%
  Skewness:             {skew} ({right/left/symmetric} tail)
  Kurtosis:             {kurt} ({fat/normal/thin} tails)

VOLATILITY REGIME
  5-bar realized vol:   {v5}%
  20-bar realized vol:  {v20}%
  Expansion ratio:      {ratio} → {Expanding/Normal/Compressing}

MOMENTUM
  1-bar:   {r1} | 5-bar: {r5} | 20-bar: {r20}
  Momentum score: {score} → {Strong Long/Moderate Long/None/Moderate Short/Strong Short}

MEAN REVERSION
  Z-score (20-bar):    {z} → {Overbought/Normal/Oversold}
  Autocorrelation:     {ac} → {Trending/Random/Mean-Reverting}

RISK-ADJUSTED RETURNS
  Sharpe (ann.):  {sharpe}
  Sortino (ann.): {sortino}
  Max drawdown est: {dd}%

REGIME:  {TRENDING UP / TRENDING DOWN / MEAN REVERTING / COILING / STRESSED / CHOPPY}
EDGE:    {YES / MARGINAL / NO}
TYPE:    {Momentum / Mean Reversion / Breakout / None}

RECOMMENDED STRATEGY: {one sentence matching regime to approach}
POSITION SIZE MODIFIER: {normal / -25% (marginal edge) / -50% (stressed) / AVOID}
```
