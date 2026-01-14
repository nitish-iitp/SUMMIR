# Dataset JSONL

This directory contains the curated JSONL datasets used for training and evaluating the SUMMIR (Sentence Unified Multimetric Model for Importance Ranking) framework.

## Directory Structure

```
Dataset_jsonl/
├── Cricket( Odi, T20 )/    # Cricket match datasets
├── MLB/                    # Major League Baseball datasets
├── NBA/                    # National Basketball Association datasets
├── Soccer/                 # Football/Soccer datasets
├── sampleDataset.jsonl     # Representative sample for quick testing
└── subDataset.jsonl        # Subset for validation experiments
```

## Sport-Specific Datasets

| Sport | Files | Description |
|-------|-------|-------------|
| **Cricket (ODI, T20)** | 3 | `datasetT20.jsonl`, `datasetodi1.jsonl`, `datasetodi2.jsonl` |
| **MLB** | 5 + PDF | `datasetmlb1-5.jsonl` + `Datasets_Details.pdf` |
| **NBA** | 5 | `datasetnba1-5.jsonl` |
| **Soccer** | 7 | `datasetsoccer1-7.jsonl` |

## JSONL Schema

Each entry in the JSONL files follows this structure:

```json
{
  "match_info": "Team A vs Team B - Date",
  "article": "Original sports article text...",
  "insights": ["Insight sentence 1", "Insight sentence 2", ...],
  "gold_ranking": [1, 3, 2, ...]
}
```

| Field | Type | Description |
|-------|------|-------------|
| `match_info` | string | Match identifier with teams and date |
| `article` | string | Source article from which insights are extracted |
| `insights` | array | List of generated insight sentences |
| `gold_ranking` | array | Human-annotated importance ranking (1 = most important) |

## Sample Files

- **`sampleDataset.jsonl`**: Representative subset for rapid prototyping and testing
- **`subDataset.jsonl`**: Validation subset for cross-validation experiments

## Usage

```python
import json

with open('Dataset/Dataset_jsonl/Soccer/datasetsoccer1.jsonl', 'r') as f:
    for line in f:
        entry = json.loads(line)
        print(entry['match_info'])
```

## Related Documentation

- See [`dataset_details.pdf`](../../dataset_details.pdf) for comprehensive data collection methodology
- See [`MLB/Datasets_Details.pdf`](MLB/Datasets_Details.pdf) for MLB-specific documentation
- See [`../Dataset_proccessed/`](../Dataset_proccessed/) for the raw data processing pipeline
