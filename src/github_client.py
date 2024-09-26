import os
from github import Github
from dotenv import load_dotenv

def init_github_client():
    # Load environment variables from .env file if it exists
    if os.path.exists('.env'):
        load_dotenv()

    # Get the GitHub token from environment variables
    token = os.getenv("GIT_FULL_ACCESS_TOKEN")
    
    if not token:
        raise ValueError("GitHub token not found in environment variables.")
    
    # Initialize GitHub API client
    g = Github(token)
    print(f"GitHub client initialized with token.")
    
    return g
