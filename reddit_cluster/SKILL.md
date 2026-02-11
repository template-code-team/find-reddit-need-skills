---
name: reddit_cluster
description: Cluster extracted Reddit needs and output actionable content/product ideas.
---

# Reddit Clustering & Actionable Output Skill

This skill takes the extracted structured data and clusters it into 10–30 actionable "Need Cards".

## Instructions

Group the insights by theme and generate "Executable Topic Cards" (可执行选题).

**IMPORTANT: All output (Title, Analysis, Suggestions, Page Structure) MUST be in Chinese (Simplified).** 
- **Only** keep original Reddit quotes and specific English SEO keywords in English.
- Use **Chinese** for "Target User", "Suggested Page Structure", and "Monetization Suggestion".

Each card must include (Use these exact Chinese labels):

1. **需求标题**: Catchy and descriptive title for the need (in Chinese).
2. **目标用户**: Who is experiencing this need (in Chinese).
3. **Reddit 证据**: 2-3 supporting quotes/evidence with links (Key quotes in English, context in Chinese).
4. **页面大纲建议**: H2/H3 outline for a landing page or blog post (All headings in Chinese).
5. **SEO 关键词**: Main keyword + long-tail keywords (English).
6. **变现建议**: Subscription, one-time, ads, or affiliate/leads (in Chinese).

**FINAL STEP: Save Results**
You MUST save the generated topic cards to a file in the `find-need-skills/reddit_result/` directory.

File Naming Convention: `result-YY-MM-DD.md` (e.g., `result-26-02-11.md`).
If a file for the current date already exists, you **must** append a number like `result-26-02-11-2.md`. **Never** overwrite existing result files.

## Output Format

Present the results as a series of structured cards or a comprehensive JSON object suitable for report generation.

## Examples
See `examples/output_example.md` or previous results in `find-need-skills/reddit_result/`.
