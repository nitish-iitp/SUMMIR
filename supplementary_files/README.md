# Supplementary Files

This directory contains supporting data files used by the SUMMIR training framework for feature computation.

## Contents

| File | Purpose | Format |
|------|---------|--------|
| `processed_persons.csv` | Named entity importance scores | CSV |
| `processed_persons_cleaning.py` | Data cleaning utility | Python |
| `sports_keywords.csv` | Domain-specific keyword scores | CSV |
| `sports_sentiment.csv` | Sentiment lexicon for sports | CSV |
| `sports_keyword.ipynb` | Keyword analysis notebook | Jupyter |

## Data Schemas

### processed_persons.csv

Contains Historical Popularity Index (HPI) scores for athletes and sports personalities.

| Column | Type | Description |
|--------|------|-------------|
| `name` | string | Person's full name (lowercase) |
| `hpi` | float | Historical Popularity Index (0-1000) |

**Usage in training:** Person Score feature computation

---

### sports_keywords.csv

Domain-specific keywords with relevance scores.

| Column | Type | Description |
|--------|------|-------------|
| `Word` | string | Sports-related keyword |
| `AverageScore` | float | Importance score (0-1) |

**Usage in training:** Buzzword Score feature computation

---

### sports_sentiment.csv

Sentiment lexicon tailored for sports domain.

| Column | Type | Description |
|--------|------|-------------|
| `word` | string | Term |
| `sentiment` | float | Sentiment polarity (-1 to 1) |

**Usage in training:** Sentiment Score refinement

## Usage

These files are automatically loaded by the training scripts:

```python
# In 6_metrics_Training_code.py
sports_keywords_df = pd.read_csv("sports_keywords.csv")
famous_people_df = pd.read_csv("processed_persons.csv")
```

## Utilities

- **`processed_persons_cleaning.py`**: Preprocesses raw person data
- **`sports_keyword.ipynb`**: Exploratory analysis of keyword distributions
