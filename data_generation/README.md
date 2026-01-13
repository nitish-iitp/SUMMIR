# Data Generation Pipeline

This module contains the automated pipeline for generating high-quality, fact-verified sports insights from raw articles.

## Pipeline Overview

```mermaid
flowchart LR
    A[Raw Articles] --> B[article_validation_save.py]
    B --> C[Validated Articles]
    C --> D[insight_generation.py]
    D --> E[Generated Insights]
    E --> F{Fact Verification}
    F --> G[factScore.py]
    F --> H[summacConv.py]
    G --> I[Scored Insights]
    H --> I
    
    style A fill:#e2e8f0,stroke:#4a5568
    style I fill:#48bb78,stroke:#276749,color:#fff
```

## Scripts

### 1. Article Validation

**File:** `article_validation_save.py`

| Attribute | Value |
|-----------|-------|
| **Purpose** | Validates article relevance to specific matches |
| **Model** | Qwen2.5-32B-Instruct |
| **Output** | Binary classification (relevant/irrelevant) |

**Key Functions:**
- `createUserPrompt()`: Generates system prompt for validation
- `get_llm_output()`: Invokes LLM for classification
- `process_files_in_order()`: Batch processing of article directories

---

### 2. Insight Generation

**File:** `insight_generation.py`

| Attribute | Value |
|-----------|-------|
| **Purpose** | Extracts key insights from validated articles |
| **Model** | DeepSeek-R1-Distill-Llama-70B |
| **Output** | Structured list of insight sentences |

**Process:**
1. Loads validated article content
2. Applies sport-specific prompts from [`prompt_for_each_sport/`](prompt_for_each_sport/)
3. Generates ranked insight sentences

---

### 3. Factual Scoring (GPT-4o)

**File:** `factScore.py`

| Attribute | Value |
|-----------|-------|
| **Purpose** | Scores factual consistency of insights |
| **Model** | GPT-4o (OpenAI API) |
| **Output** | Factual accuracy scores per insight |

> [!NOTE]
> Requires OpenAI API key configured as environment variable.

---

### 4. Factual Verification (SummaCConv)

**File:** `summacConv.py`

| Attribute | Value |
|-----------|-------|
| **Purpose** | Alternative factual consistency verification |
| **Model** | SummaCConv (local) |
| **Output** | Consistency scores |

**Advantages:**
- No API dependency
- Faster inference for large batches

## Usage

```bash
# Step 1: Validate articles
python article_validation_save.py

# Step 2: Generate insights
python insight_generation.py

# Step 3: Score insights (choose one)
python factScore.py      # GPT-4o based
python summacConv.py     # Local model
```

## Directory Contents

| File | Purpose |
|------|---------|
| `article_validation_save.py` | Article relevance classification |
| `insight_generation.py` | LLM-based insight extraction |
| `factScore.py` | GPT-4o factual scoring |
| `summacConv.py` | SummaCConv verification |
| [`prompt_for_each_sport/`](prompt_for_each_sport/) | Sport-specific prompt templates |
