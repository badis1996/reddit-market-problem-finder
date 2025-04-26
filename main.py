#!/usr/bin/env python3

"""Main entry point for the Reddit Market Problem Finder."""

import os
import time
import schedule
import logging
import argparse
from dotenv import load_dotenv
from datetime import datetime

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler(f"logs/{datetime.now().strftime('%Y-%m-%d')}.log"),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

# Ensure logs directory exists
os.makedirs('logs', exist_ok=True)
os.makedirs('reports', exist_ok=True)

# Load environment variables
load_dotenv()

def run_agent():
    """Main function to run the Reddit market problem finder agent."""
    start_time = time.time()
    logger.info("Starting Reddit market problem finder agent")
    
    try:
        # Import necessary modules
        from reddit_crawler import RedditCrawler
        from problem_analyzer import ProblemAnalyzer
        from opportunity_assessor import OpportunityAssessor
        from report_generator import ReportGenerator
        from data_store import DataStore
        
        # Initialize components
        data_store = DataStore()
        reddit_crawler = RedditCrawler()
        problem_analyzer = ProblemAnalyzer()
        opportunity_assessor = OpportunityAssessor()
        report_generator = ReportGenerator()
        
        # Step 1: Crawl Reddit for posts
        posts = reddit_crawler.crawl_subreddits()
        logger.info(f"Crawled {len(posts)} posts from Reddit")
        
        # Step 2: Extract problems from posts
        problems = problem_analyzer.extract_problems(posts)
        logger.info(f"Extracted {len(problems)} potential problems")
        
        # Step 3: Cluster similar problems
        clustered_problems = problem_analyzer.cluster_problems(problems)
        logger.info(f"Clustered into {len(clustered_problems)} unique problem categories")
        
        # Step 4: Assess opportunities
        opportunities = opportunity_assessor.assess_opportunities(clustered_problems)
        logger.info(f"Assessed {len(opportunities)} potential opportunities")
        
        # Step 5: Store results
        data_store.save_opportunities(opportunities)
        
        # Step 6: Generate report
        report_path = report_generator.generate_report(opportunities)
        logger.info(f"Generated report at {report_path}")
        
        # Optional: Send notifications if configured
        if os.getenv('EMAIL_RECIPIENT'):
            from notifier import Notifier
            notifier = Notifier()
            notifier.send_email_notification(report_path)
            logger.info("Sent email notification")
            
        execution_time = time.time() - start_time
        logger.info(f"Agent run completed in {execution_time:.2f} seconds")
        return opportunities
    
    except Exception as e:
        logger.error(f"Error running agent: {e}", exc_info=True)
        execution_time = time.time() - start_time
        logger.info(f"Agent run failed after {execution_time:.2f} seconds")
        return []

def schedule_agent():
    """Schedule the agent to run periodically."""
    interval_hours = int(os.getenv('SCHEDULE_INTERVAL_HOURS', 24))
    logger.info(f"Scheduling agent to run every {interval_hours} hours")
    schedule.every(interval_hours).hours.do(run_agent)
    
    while True:
        schedule.run_pending()
        time.sleep(60)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Reddit Market Problem Finder")
    parser.add_argument("--schedule", action="store_true", help="Run the agent on a schedule")
    args = parser.parse_args()
    
    # Run immediately once
    run_agent()
    
    # If scheduling is enabled, start the scheduler
    if args.schedule or os.getenv('SCHEDULE_INTERVAL_HOURS'):
        schedule_agent()
