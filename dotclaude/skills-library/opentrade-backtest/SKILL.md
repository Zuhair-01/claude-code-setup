---
name: opentrade-backtest
description: >
  Write, compile, and validate Pine Script v6 strategies in TradingView via CDP.
  Covers strategy coding, lookahead prevention, realistic costs, walk-forward validation,
  overfitting detection, and performance interpretation.
  Use when user asks to "backtest", "write a strategy", "test this idea",
  "Pine Script strategy", or "does this work historically."
  Improved from OpenTrade v1 — adds walk-forward protocol, overfitting checklist,
  100-trade minimum, Monte Carlo guidance, and Pine v6 code templates.
---

# Strategy Backtest Skill (OpenTrade Enhanced)

---

## Step 1 — Strategy Specification

Before writing a single line of code, confirm:
1. **Signal logic**: What triggers a long entry? A short entry?
2. **Exit logic**: Fixed TP/SL? Trailing stop? Signal reversal? Time-based?
3. **Timeframe**: What TF does this strategy run on?
4. **Asset class**: Equity, futures, or crypto? (Affects realistic commission/slippage)
5. **Position type**: Long only, short only, or both?

If the user hasn't specified all five, ask before coding.

---

## Step 2 — Write the Pine Script

```
chart_get_state  → confirm current symbol and TF
```

Open the Pine editor and write the strategy. Use this template as base:

```pinescript
//@version=6
strategy(
    title       = "{Strategy Name}",
    overlay     = true,
    initial_capital = 10000,
    default_qty_type = strategy.percent_of_equity,
    default_qty_value = 10,          // 10% per trade — adjust to user's preference
    commission_type  = strategy.commission.percent,
    commission_value = {0.05},       // equities: 0.05 | crypto: 0.15 | futures: 0.01
    slippage         = {2},          // ticks: 1-2 equities, 3-5 crypto, 2 futures
    calc_on_order_fills = false,     // prevents lookahead
    calc_on_every_tick  = false      // prevents lookahead
)

// ─── INDICATORS ───
// Always use barstate.isconfirmed or [1] indexing for signal confirmation
// WRONG:  if ta.crossover(fast, slow)         ← lookahead if recalculates mid-bar
// CORRECT: if ta.crossover(fast[1], slow[1])  ← uses confirmed prior bar values

{indicator_code}

// ─── SIGNALS ───
longCondition  = {your_long_condition}[1]   // [1] = confirmed bar
shortCondition = {your_short_condition}[1]

// ─── ENTRIES ───
if longCondition and strategy.position_size == 0
    strategy.entry("Long", strategy.long)

if shortCondition and strategy.position_size == 0
    strategy.entry("Short", strategy.short)

// ─── EXITS ───
// Option A: Fixed R:R
strategy.exit("Long Exit",  "Long",  profit = {TP_ticks}, loss = {SL_ticks})
strategy.exit("Short Exit", "Short", profit = {TP_ticks}, loss = {SL_ticks})

// Option B: ATR-based dynamic stops
atr = ta.atr(14)
if strategy.position_size > 0
    strategy.exit("Long ATR", "Long",
        stop   = strategy.position_avg_price - atr * {SL_mult},
        limit  = strategy.position_avg_price + atr * {TP_mult})
```

---

## Step 3 — Compile and Fix

```
ui_open_panel (panel: "pine_editor")    // MUST open panel first
pine_set_source (code: {script})
pine_smart_compile
```

If compilation errors: read the error, fix the specific line, recompile.
**Never guess at fixes** — Pine v6 errors are specific. Read them.

Common errors:
- `Cannot use 'strategy.entry' in 'study' context` → Change `study()` to `strategy()`
- `Undeclared identifier` → Variable used before declared, or typo
- `Series not allowed here` → You're using a series where Pine expects a simple value

---

## Step 4 — Initial Sanity Check

Before running the full backtest, check these first:

```
pine_save (title: "{Strategy Name} v1")
```

Open Strategy Tester. Look at:
- **Number of trades**: Is it ≥ 100? If < 30, the data is meaningless.
- **Date range**: Does it cover at least 2 full market cycles (bull + bear)?
- **First trade date**: Is it way in the past? Data quality issues before 2015 are common.

If fewer than 100 trades: extend the date range, or switch to a shorter timeframe.

---

## Step 5 — Full Performance Read

Open Strategy Tester → Performance Summary. Record:

**Core metrics:**
| Metric | Value | Threshold |
|--------|-------|-----------|
| Net profit | {$} | Must be positive |
| Profit factor | {PF} | >1.5 good, >2.0 excellent, >4.0 suspect overfitting |
| Max drawdown | {%} | <20% acceptable, <10% excellent |
| Win rate | {%} | Context-dependent (see below) |
| Total trades | {N} | Must be ≥ 100 |
| Avg win / avg loss | {ratio} | Must yield positive EV |
| Sharpe ratio | {S} | >1.0 good, >2.0 excellent |

**Win rate context:**
- High win rate (>60%) requires low RR (trades quick) — verify avg win > avg loss
- Low win rate (<40%) requires high RR (≥2.5R minimum) — verify EV positive
- Win rate >80% with high profit factor on <100 trades → **red flag: overfitting**

---

## Step 6 — Overfitting Checklist

Run through this before declaring the strategy valid:

| Check | Question | Red flag |
|-------|----------|----------|
| Sample size | Are there ≥ 100 trades? | < 50 trades = meaningless |
| Parameter count | How many parameters were optimized? | > 3 parameters optimized = likely overfit |
| In-sample PF | Is profit factor > 4.0? | Extremely high on limited data = overfit |
| Out-of-sample | Does it work on a different date range? | Fails OOS = overfit |
| Different asset | Does it work on a correlated asset? | Fails all others = overfit |
| Logic simplicity | Can you explain the logic in 2 sentences? | If not, probably overfit |

---

## Step 7 — Walk-Forward Validation

This is the only reliable way to test for overfitting.

Split the data:
- **In-sample (IS)**: First 70% of available data → optimize here
- **Out-of-sample (OOS)**: Last 30% → test here, no changes allowed

Procedure:
1. Run backtest on IS period only. Record PF, max DD, win rate.
2. Do NOT touch the parameters.
3. Run the same strategy on OOS period.
4. Compare results.

**Acceptance criteria:**
- OOS profit factor ≥ 70% of IS profit factor
- OOS max drawdown ≤ 150% of IS max drawdown
- OOS win rate within ±10% of IS win rate

If OOS degrades severely → strategy doesn't generalize. Start over.

---

## Step 8 — Results Interpretation

```
=== BACKTEST RESULTS: {Strategy Name} on {SYMBOL} {TF} ===

SAMPLE
  Total trades:  {N} | Date range: {start} — {end}
  Timeframe:     {TF} | Commission: {%} | Slippage: {ticks}

PERFORMANCE
  Net profit:      {$} ({%} return)
  Profit factor:   {PF}
  Max drawdown:    {%}
  Win rate:        {%}
  Avg win / loss:  {ratio}
  Sharpe ratio:    {S}

WALK-FORWARD
  In-sample PF:    {PF_is} | OOS PF: {PF_oos} | Ratio: {oos/is}
  In-sample DD:    {dd_is} | OOS DD: {dd_oos}
  Verdict:         {GENERALIZES / DEGRADED / FAILED}

OVERFITTING CHECK
  Parameters used: {N}
  Sample size:     {adequate / borderline / insufficient}
  PF suspicion:    {none / moderate / high}
  Verdict:         {LOW RISK / MODERATE RISK / HIGH RISK OF OVERFIT}

VERDICT
  Strategy status: {DEPLOY-READY / NEEDS REFINEMENT / DISCARD}
  Next step:       {paper trade 30 days / reduce parameters / start over}
```

---

## Step 9 — If Strategy Passes

```
pine_save (title: "{Strategy Name} — Validated v{N}")
capture_screenshot (region: "chart")
```

Document in the report:
- Exact parameters (do not change them after validation)
- Which assets and timeframes it was tested on
- Walk-forward results
- Max expected drawdown (use OOS figure, not IS)
- Recommended position size (stay at 10% of equity per trade max until live-validated)
