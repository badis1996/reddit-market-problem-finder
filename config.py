# Configuration for Reddit Market Problem Finder

# Subreddits to monitor - these are known for discussing problems and pain points
TARGET_SUBREDDITS = [
    # Main problem-focused subreddits
    'firstworldproblems',
    'mildlyinfuriating',
    'rant',
    'TalesFromRetail',
    'TalesFromTechSupport',
    'sysadmin',
    
    # Industry-specific subreddits
    'personalfinance',
    'homeimprovement',
    'parenting',
    'productivity',
    'fitness',
    'cooking',
    'wfh',
    'remotework',
    'freelance',
    'smallbusiness',
    'startup',
    'entrepreneur',
    
    # Technology-focused subreddits
    'technology',
    'programming',
    'webdev',
    'devops',
    'datascience',
    'MachineLearning',
    'artificial',
    'cybersecurity',
    
    # Lifestyle subreddits
    'travel',
    'minimalism',
    'zerowaste',
    'sustainability',
    'lifehacks',
]

# Keywords that indicate problems/pain points in posts
PROBLEM_KEYWORDS = [
    'problem',
    'issue',
    'frustrated',
    'annoying',
    'annoyed',
    'hate',
    'difficult',
    'impossible',
    'struggle',
    'pain point',
    'hurdle',
    'obstacle',
    'challenge',
    'workaround',
    'solution',
    'alternative',
    'wish there was',
    'need help',
    'looking for',
    'anyone know',
    'how do I',
    'any advice',
    'recommendation',
    'suggestions',
]

# Search parameters
SEARCH_PERIOD = 'week'  # 'day', 'week', 'month', 'year', 'all'
POSTS_LIMIT = 100  # Maximum number of posts to fetch per subreddit
MIN_SCORE = 10  # Minimum score (upvotes - downvotes) for posts to consider
MIN_COMMENTS = 5  # Minimum number of comments for posts to consider

# Opportunity assessment parameters
OPPORTUNITY_THRESHOLD = 0.7  # Minimum opportunity score to include in report
MIN_PROBLEM_FREQUENCY = 3  # Minimum occurrences of a similar problem

# GPT analysis parameters
PROBLEM_EXTRACTION_PROMPT = """
Identify specific problems or pain points mentioned in the following Reddit post. 
Focus on recurring issues that could potentially be solved with a product or service.
Format your response as a JSON array of problems, with each problem containing:
- problem_statement: A clear, concise statement of the problem
- severity: Rate from 1-10 how painful this problem seems
- frequency: Rate from 1-10 how frequently this problem occurs based on context
- audience: Who experiences this problem (demographic, profession, etc.)
- willingness_to_pay: Rate from 1-10 how likely people would pay for a solution

Post: {post_text}
"""

OPPORTUNITY_ASSESSMENT_PROMPT = """
Evaluate the following problem as a potential startup opportunity:

Problem: {problem_statement}
Context: {problem_context}

Provide your assessment in JSON format with the following fields:
- market_size: Estimated size of the target market (small/medium/large)
- competition: Level of existing competition (low/medium/high)
- technical_feasibility: How feasible is building a solution (easy/moderate/difficult)
- regulatory_challenges: Potential regulatory hurdles (none/some/significant)
- business_model: Suggested monetization approach
- go_to_market: Suggested customer acquisition strategy
- differentiator: What would make a solution stand out
- risks: Key risks to be aware of
- opportunity_score: A score from 0-10 indicating overall viability as a startup opportunity
"""

# Reporting configuration
REPORT_ITEMS_LIMIT = 10  # Number of top opportunities to include in the report
