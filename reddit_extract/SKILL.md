---
name: reddit_extract
description: Extract structured pain points and user intent from Reddit posts and comments.
---

# Reddit Intent/Pain Point Extraction Skill

This skill processes Reddit content to identify user needs, pain points, and purchase intent.

## Instructions

Analyze the provided Reddit post list or specific comment threads. For each relevant item, extract:

1. **Pain Point Quote**: Direct quote from the user highlighting their struggle.
2. **Need Type**: Classify into:
   - Request for Recommendation (求推荐)
   - Seeking Alternatives (求替代)
   - Tutorial/How-to Request (求教程)
   - Bug/Issue Help (报错求助)
   - Price Sensitive (价格敏感)
   - Comparison/Review (对比评测)
3. **Purchase Intent Score**: 0-5 (0: Low, 5: High)
4. **Potential Opportunity**: Suggest if this is a tool, plugin, template, or content opportunity.

## Output Format

Return a JSON array of extracted insights:

```json
[
  {
    "quote": "...",
    "need_type": "...",
    "intent_score": 4,
    "opportunity": "...",
    "source_url": "..."
  }
]
```
