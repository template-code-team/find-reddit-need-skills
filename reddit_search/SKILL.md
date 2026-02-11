---
name: reddit_search
description: Search Reddit for posts based on keywords, subreddits, and time range.
---

# Reddit Search Skill

This skill allows searching Reddit for specific keywords within targeted subreddits.

## Usage

**Method 1: Web Search Simulation (Recommended)**

Since the Reddit API often blocks automated requests (429/403 errors), the most reliable method is to use the `search_web` tool.

> **Note**: This method queries the search engine's index (Google/Bing) rather than Reddit's servers directly. Therefore, you do **not** need to add artificial delays or worry about IP bans/rate limits (HTTP 429) from Reddit.

1.  **Construct Query**: Create a search query in the format: `site:reddit.com (r/subreddit1 OR r/subreddit2) "keyword" after:YYYY-MM-DD`.
2.  **Execute Search**: Use the `search_web` tool with this query.
3.  **Parse Results**: Extract post titles, URLs, and summaries from the search results.



## Output Format
The output should be a list of posts containing:
- `title`: Post title
- `url`: Full URL to the post
- `summary`: Brief description of the post content
- `subreddit`: Subreddit name (if available)
