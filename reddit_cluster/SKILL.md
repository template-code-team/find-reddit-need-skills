---
name: reddit_cluster
description: Cluster extracted Reddit needs and output actionable content/product ideas.
---

# Reddit Clustering & Actionable Output Skill

This skill takes the extracted structured data and clusters it into 10–30 actionable "Need Cards".

## Instructions

Group the insights by theme and generate "Executable Topic Cards" (可执行选题).

**IMPORTANT: All output (Title, Analysis, Suggestions, Page Structure) MUST be in Chinese (Simplified). Only keep original Reddit quotes and specific English SEO keywords in English.**

Each card must include:

1. **Title**: Catchy and descriptive title for the need (in Chinese).
2. **Target User**: Who is experiencing this need.
3. **Reddit Evidence**: 2-3 supporting quotes/evidence with links.
4. **Suggested Page Structure**: H2/H3 outline for a landing page or blog post.
5. **Keyword Suggestions**: Main keyword + long-tail keywords.
6. **Monetization Suggestion**: Subscription, one-time, ads, or affiliate/leads.

**FINAL STEP: Save Results**
You MUST save the generated topic cards to a file in the `find-need-skills/reddit_result/` directory.

File Naming Convention: `result-YY-MM-DD.md` (e.g., `result-26-02-11.md`).
If a file for the current date already exists, append a number like `result-26-02-11-2.md` or simply overwrite it based on context (default to overwrite if not specified).

## Output Format

Present the results as a series of structured cards or a comprehensive JSON object suitable for report generation.

## Examples
See `examples/output_example.md` or previous results in `find-need-skills/reddit_result/`.
