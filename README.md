# DeFi Protocol Quality & Sustainability Analysis

This repository analyzes DeFi protocols through the lens of **TVL quality and sustainability**, rather than raw Total Value Locked rankings.

The objective is to distinguish:
- Sustainable, usage-driven TVL
- Incentive-driven or reflexive liquidity
- Protocols with durable capital retention across market cycles

The analysis emphasizes **time-series behavior of TVL**, focusing on growth, volatility, drawdowns, and post-peak capital retention.

---

## Repository Structure

```text
defi_protocol_quality/
│
├─ README.md
│
├─ notebooks/
│  ├─ 01_ingest.ipynb
│  └─ 02_tvl_quality.ipynb
│
├─ data/
│  ├─ raw/
│  └─ processed/
│
├─ case_studies/
│  ├─ curve.md
│  ├─ gmx.md
│  ├─ lido.md
│  ├─ olympusdao.md
│  └─ sushiswap_liquidity_mining.md
│
├─ data_sources.md
└─ methodology.md

```
---

## Notebook Overview

### Notebook 01 — Data Ingestion
**notebooks/01_ingest.ipynb**

- Fetches protocol-level TVL data from public DeFi APIs
- Stores raw JSON snapshots and cleaned datasets
- Establishes a reproducible ingestion pipeline

---

### Notebook 02 — TVL Quality & Sustainability Metrics
**notebooks/02_tvl_quality.ipynb**

This notebook evaluates protocols using **TVL quality metrics**, including:
- Average daily TVL growth
- TVL volatility (stability of capital)
- Maximum drawdown (peak-to-trough losses)
- Capital retention vs historical peak
- TVL half-life (time to decay from peak to 50%)

Rather than ranking protocols by size, this analysis focuses on **capital behavior over time** and resilience across market cycles.

---

## Case Studies

The case_studies directory contains focused qualitative analyses that complement the quantitative TVL metrics.

Each case study highlights a distinct TVL behavior pattern observed in practice.

```text
case_studies/
├─ curve.md
├─ gmx.md
├─ lido.md
├─ olympusdao.md
└─ sushiswap_liquidity_mining.md

```
Covered themes:
- Incentive-driven liquidity expansion and decay
- Sustainable usage-driven TVL
- Capital retention after peak cycles
- Structural drawdowns and regime shifts
- Scenarios where TVL ceases to be a meaningful health metric

---

## Key Takeaways

- Raw TVL rankings obscure protocol risk and sustainability
- Large drawdowns often indicate incentive-heavy liquidity
- Lower volatility and higher retention suggest durable protocol usage
- TVL quality metrics provide a clearer picture of protocol health

---

## Disclaimer

This repository is for research and analytical purposes only and does not constitute financial advice.
