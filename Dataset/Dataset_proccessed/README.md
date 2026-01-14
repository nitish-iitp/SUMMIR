# Dataset Processing Pipeline

This directory contains the complete data processing pipeline from raw scraped articles to final ranked insights.

## Pipeline Stages

```mermaid
flowchart TB
    S1["1_Scrapped/"] --> S2["2_First Level Validation/"]
    S2 --> S3["3_Valid Data 200/"]
    S3 --> S4["4_Second Level Validated Data and Insights/"]
    S4 --> S5["5_Hallucination Detection/"]
    S5 --> S6["6_Ranking Insights/"]
    
    style S1 fill:#fee2e2,stroke:#dc2626
    style S6 fill:#bbf7d0,stroke:#16a34a
```

## Stage Descriptions

| Stage | Directory | Description |
|-------|-----------|-------------|
| 1 | `1_Scrapped/` | Raw sports articles scraped from online sources |
| 2 | `2_First Level Validation/` | Initial filtering for language and relevance |
| 3 | `3_Valid Data 200/` | Validated articles meeting quality threshold |
| 4 | `4_Second Level Validated Data and Insights/` | LLM-generated insights from validated articles |
| 5 | `5_Hallucination Detection/` | Fact-checked insights (GPT-4o / SummaCConv) |
| 6 | `6_Ranking Insights/` | Final insights with importance rankings |

## Output

The final output from Stage 6 is converted to JSONL format and stored in [`../Dataset_jsonl/`](../Dataset_jsonl/) for model training.

## Related Scripts

Processing is performed by scripts in [`../../data_generation/`](../../data_generation/):
- `article_validation_save.py` → Stages 2-3
- `insight_generation.py` → Stage 4
- `factScore.py` / `summacConv.py` → Stage 5
