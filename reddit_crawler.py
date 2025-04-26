import praw
import os
import logging
from tqdm import tqdm
from dotenv import load_dotenv
from config import TARGET_SUBREDDITS, SEARCH_PERIOD, POSTS_LIMIT, MIN_SCORE, MIN_COMMENTS, PROBLEM_KEYWORDS

logger = logging.getLogger(__name__)

class RedditCrawler:
    def __init__(self):
        """Initialize the Reddit crawler with API credentials."""
        load_dotenv()  # Load environment variables if not already loaded
        
        # Check if required environment variables are set
        required_vars = ['REDDIT_CLIENT_ID', 'REDDIT_CLIENT_SECRET', 'REDDIT_USER_AGENT']
        missing_vars = [var for var in required_vars if not os.getenv(var)]
        
        if missing_vars:
            logger.error(f"Missing required environment variables: {', '.join(missing_vars)}")
            logger.error("Please set these variables in your .env file or environment")
            raise ValueError(f"Missing required environment variables: {', '.join(missing_vars)}")
        
        # Initialize the Reddit API client
        try:
            self.reddit = praw.Reddit(
                client_id=os.getenv('REDDIT_CLIENT_ID'),
                client_secret=os.getenv('REDDIT_CLIENT_SECRET'),
                user_agent=os.getenv('REDDIT_USER_AGENT'),
                username=os.getenv('REDDIT_USERNAME'),
                password=os.getenv('REDDIT_PASSWORD')
            )
            logger.info("Reddit API client initialized")
        except Exception as e:
            logger.error(f"Failed to initialize Reddit API client: {e}")
            raise
    
    def crawl_subreddits(self):
        """Crawl target subreddits for posts that indicate problems."""
        all_posts = []
        
        for subreddit_name in tqdm(TARGET_SUBREDDITS, desc="Crawling subreddits"):
            try:
                subreddit = self.reddit.subreddit(subreddit_name)
                logger.info(f"Crawling r/{subreddit_name}")
                
                # Get top posts from the current time period
                top_posts = subreddit.top(time_filter=SEARCH_PERIOD, limit=POSTS_LIMIT)
                
                for post in top_posts:
                    # Skip posts that don't meet minimum criteria
                    if post.score < MIN_SCORE or post.num_comments < MIN_COMMENTS:
                        continue
                    
                    # Check if the post title or body contains any problem keywords
                    post_text = f"{post.title} {post.selftext}".lower()
                    if any(keyword.lower() in post_text for keyword in PROBLEM_KEYWORDS):
                        # Get top comments
                        post.comments.replace_more(limit=0)  # Load only top-level comments
                        comments = []
                        for comment in post.comments[:20]:  # Get top 20 comments
                            comments.append({
                                'id': comment.id,
                                'body': comment.body,
                                'score': comment.score,
                                'created_utc': comment.created_utc
                            })
                        
                        # Add post to our collection
                        all_posts.append({
                            'id': post.id,
                            'subreddit': subreddit_name,
                            'title': post.title,
                            'selftext': post.selftext,
                            'url': post.url,
                            'permalink': f"https://reddit.com{post.permalink}",
                            'score': post.score,
                            'num_comments': post.num_comments,
                            'created_utc': post.created_utc,
                            'comments': comments
                        })
                        logger.debug(f"Found relevant post: {post.title}")
                        
            except Exception as e:
                logger.error(f"Error crawling r/{subreddit_name}: {e}")
        
        logger.info(f"Crawled {len(all_posts)} relevant posts from {len(TARGET_SUBREDDITS)} subreddits")
        return all_posts
    
    def search_specific_problem(self, problem_query, subreddits=None, limit=100):
        """Search for a specific problem across all or specified subreddits."""
        if subreddits is None:
            subreddits = TARGET_SUBREDDITS
        
        subreddit_list = '+'.join(subreddits)  # Join subreddits with '+' for multi-search
        subreddit = self.reddit.subreddit(subreddit_list)
        
        search_results = []
        for post in subreddit.search(problem_query, limit=limit):
            if post.score >= MIN_SCORE:
                search_results.append({
                    'id': post.id,
                    'subreddit': post.subreddit.display_name,
                    'title': post.title,
                    'selftext': post.selftext,
                    'url': post.url,
                    'permalink': f"https://reddit.com{post.permalink}",
                    'score': post.score,
                    'num_comments': post.num_comments,
                    'created_utc': post.created_utc,
                })
        
        return search_results

# Example usage
if __name__ == "__main__":
    # Set up logging
    logging.basicConfig(level=logging.INFO)
    
    # Create crawler
    crawler = RedditCrawler()
    
    # Crawl subreddits
    posts = crawler.crawl_subreddits()
    print(f"Found {len(posts)} relevant posts")
    
    # Example search
    results = crawler.search_specific_problem("can't find coworking space")
    print(f"Found {len(results)} posts about coworking spaces")
