# Sport-Specific Prompts

This directory contains carefully crafted prompt templates for generating domain-specific insights from sports articles.

## Purpose

These prompts are used by [`insight_generation.py`](../insight_generation.py) to guide the LLM in extracting relevant, high-quality insights tailored to each sport's unique terminology and context.

## Prompt Files

| File | Sport | Key Focus Areas |
|------|-------|-----------------|
| `cricket.txt` | Cricket (ODI, T20) | Overs, wickets, run rates, partnerships |
| `MLB.txt` | Baseball | Innings, RBIs, ERA, batting averages |
| `NBA.txt` | Basketball | Quarters, points, rebounds, assists |
| `soccer.txt` | Soccer/Football | Goals, assists, possession, formations |

## Prompt Structure

Each prompt template follows a consistent structure:

1. **Context Setting**: Establishes the sport and match context
2. **Task Definition**: Specifies insight extraction requirements
3. **Output Format**: Defines expected sentence structure
4. **Quality Criteria**: Emphasizes factual accuracy and relevance

## Usage

```python
# In insight_generation.py
with open(f'prompt_for_each_sport/{sport}.txt', 'r') as f:
    prompt_template = f.read()
```

## Customization

To add support for a new sport:

1. Create `{sport_name}.txt` following the existing format
2. Include sport-specific terminology
3. Define relevant statistical metrics
4. Update the main pipeline configuration
