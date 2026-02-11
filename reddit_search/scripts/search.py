import requests
import json
import sys
import time
import random
from datetime import datetime

# Common User-Agents to rotate to avoid IP blocking
USER_AGENTS = [
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36',
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.2 Safari/605.1.15',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:122.0) Gecko/20100101 Firefox/122.0'
]

def get_random_headers():
    return {
        'User-Agent': random.choice(USER_AGENTS),
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.9',
    }

def search_reddit(keyword, subreddits=None, time_range='month', limit=100):
    results = []
    
    # If no subreddits provided, search all of reddit
    target_subs = subreddits if subreddits else ['all']
    
    for sub in target_subs:
        url = f"https://www.reddit.com/r/{sub}/search.json"
        params = {
            'q': keyword,
            'restrict_sr': 1 if sub != 'all' else 0,
            't': time_range,
            'limit': limit,
            'sort': 'relevance'
        }
        
        try:
            # Use random headers for each request
            headers = get_random_headers()
            
            response = requests.get(url, params=params, headers=headers)
            
            # Handle rate limiting
            if response.status_code == 429:
                print(f"Rate limited on r/{sub}, waiting 10s...", file=sys.stderr)
                time.sleep(10)
                continue
                
            response.raise_for_status()
            data = response.json()
            
            posts = data.get('data', {}).get('children', [])
            for post in posts:
                p = post.get('data', {})
                results.append({
                    'title': p.get('title'),
                    'url': f"https://www.reddit.com{p.get('permalink')}",
                    'upvotes': p.get('ups'),
                    'comments': p.get('num_comments'),
                    'created': datetime.fromtimestamp(p.get('created_utc')).isoformat() if p.get('created_utc') else None,
                    'subreddit': p.get('subreddit')
                })
            
            # Random delay between requests (2.5 to 5.5 seconds) to be safe
            sleep_time = random.uniform(2.5, 5.5)
            time.sleep(sleep_time)
            
        except Exception as e:
            print(f"Error searching r/{sub}: {e}", file=sys.stderr)
            # Sleep even on error to avoid hammering
            time.sleep(random.uniform(2.0, 4.0))
            
    return results

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python search.py <keyword> [subreddits_comma_separated] [time_range]")
        sys.exit(1)
        
    kw = sys.argv[1]
    subs = sys.argv[2].split(',') if len(sys.argv) > 2 and sys.argv[2] else None
    tr = sys.argv[3] if len(sys.argv) > 3 else 'month'
    
    results = search_reddit(kw, subs, tr)
    print(json.dumps(results, indent=2, ensure_ascii=False))
