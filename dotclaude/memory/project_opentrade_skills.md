---
name: project-opentrade-skills
description: 8 enhanced TradingView/CDP trading skills built from brandononchain/opentrade repo. Includes ICT methodology and risk management skills that did not exist in the original.
metadata: 
  node_type: memory
  type: project
  originSessionId: 6144a4ca-1f07-4dfe-ab21-8a036dc6c623
---

Source repo: https://github.com/brandononchain/opentrade
Skills location: C:\Users\Zoher\.claude\skills\opentrade-*.md

## Skills Installed

| Skill File | Trigger |
|-----------|---------|
| opentrade-chart-analyst.md | chart analysis, technical analysis, what's the chart saying |
| opentrade-hedge-fund.md | hedge fund analysis, institutional setup, full trade plan |
| opentrade-quant.md | quant analysis, statistical edge, trending or ranging |
| opentrade-ict.md | ICT, order blocks, FVG, liquidity sweep, smart money |
| opentrade-backtest.md | backtest, Pine Script strategy, test this idea |
| opentrade-portfolio-scanner.md | scan watchlist, rank symbols, find best setup |
| opentrade-macro.md | macro analysis, regime, sector rotation, risk on/off |
| opentrade-risk.md | position size, how much to risk, drawdown management |

## What Was Improved vs. Original OpenTrade

- chart-analysis: Added divergence, volume confirmation, ICT level classification, trend-context RSI
- hedge-fund: Fixed win rate estimation (quantified, not guessed), removed $1M AUM assumption, concrete Kelly sizing
- quant: Added formulas, Sharpe/Sortino, minimum data requirements, autocorrelation
- backtest: 100-trade minimum (was 30), walk-forward protocol, overfitting checklist, Pine v6 templates
- macro: Quantified scoring thresholds, practical CDP workflow, regime timing guidance
- portfolio-scanner: Concrete 5-dimension scoring rubric, sector concentration check, missing-data handler
- ict: NEW — no ICT methodology existed in original. Full killzone, MSB, liquidity, OB, FVG, IFVG, OTE
- risk: NEW — standalone risk module. ATR stops, Kelly, portfolio heat, drawdown protocol, daily limits

**Why:** opentrade v1 sentiment/onchain skills referenced external APIs (Fear & Greed, TVL, whale tracking) that TradingView CDP cannot access. Those were not ported as skills — they require separate API integrations outside TradingView.
