import os
from dotenv import load_dotenv

load_dotenv()

# Reddit API credentials
REDDIT_CLIENT_ID = os.getenv("REDDIT_CLIENT_ID")
REDDIT_CLIENT_SECRET = os.getenv("REDDIT_CLIENT_SECRET")
REDDIT_USERNAME = os.getenv("REDDIT_USERNAME")
REDDIT_PASSWORD = os.getenv("REDDIT_PASSWORD")
USER_AGENT = f"Reddit AI Bot by /u/{REDDIT_USERNAME}"

# Groq API credentials
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
GROQ_API_URL = "https://api.groq.ai/generate"

# POST_TIME = "18:15"  # Replace with your desired time (24-hour format)


POST_SCHEDULE_TIME = "18:13"  # Time in HH:MM format for daily post
