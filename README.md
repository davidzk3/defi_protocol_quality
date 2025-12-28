# DeFi Protocol Quality & Sustainability Analysis

This repository analyzes DeFi protocols through the lens of **TVL quality and sustainability**, rather than raw Total Value Locked (TVL) rankings.

The objective is to distinguish between:
- Sustainable, usage-driven TVL
- Incentive-driven or reflexive liquidity
- Protocols with durable capital retention across market cycles

Rather than asking “Which protocol is biggest?”, this analysis asks:

How does capital behave over time, and what does that reveal about protocol health?

The work emphasizes **time-series behavior of TVL**, focusing on growth, volatility, drawdowns, and post-peak capital retention.

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
notebooks/01_ingest.ipynb

This notebook establishes the data foundation for the analysis.

Key steps:
- Fetches protocol-level TVL data from public DeFi APIs
- Stores raw JSON snapshots for reproducibility
- Produces cleaned, structured datasets for downstream analysis

The goal is a transparent and repeatable ingestion pipeline, not a one-off scrape.

---

### Notebook 02 — TVL Quality & Sustainability Metrics
notebooks/02_tvl_quality.ipynb

This notebook computes and analyzes TVL quality metrics, including:
- Average daily TVL growth (long-term expansion vs stagnation)
- TVL volatility (stability of deposited capital)
- Maximum drawdown (peak-to-trough capital losses)
- Current TVL vs historical peak (capital retention)
- TVL half-life (time to decay from peak to 50%)

Instead of ranking protocols by size, the analysis focuses on capital behavior over time, resilience across market regimes, and structural sustainability.

---

## Case Studies

The case_studies directory contains focused qualitative analyses that complement the quantitative metrics.

Each case study maps observed TVL behavior to real protocol mechanics and incentive structures.

Case studies included:
- Curve
- GMX
- Lido
- OlympusDAO
- SushiSwap (Liquidity Mining Era)

Covered themes:
- Incentive-driven liquidity expansion and decay
- Sustainable, usage-driven TVL
- Capital retention after peak cycles
- Structural drawdowns and regime shifts
- Scenarios where TVL ceases to be a meaningful health metric

The intent is to bridge quantitative metrics with qualitative protocol understanding.

---

## Key Takeaways

- Raw TVL rankings obscure protocol risk and sustainability
- Large drawdowns often signal incentive-heavy liquidity
- Lower volatility and higher retention suggest durable usage
- TVL quality metrics provide a clearer picture of protocol health than absolute size

---

## Disclaimer

This repository is for research and analytical purposes only.
It does not constitute financial advice.
