# Reddit AI Bot

A Reddit bot that uses **Groq AI** to generate and post content to a specified subreddit automatically at scheduled times.

## Features

- **Automated Daily Posting**: Posts AI-generated content to Reddit every day at a scheduled time.
- **Groq AI Content Generation**: Uses Groq AI to generate engaging content.
- **Basic Error Handling**: Logs errors in case of issues with posting or content generation.

## Requirements

- Python 3.10
- Groq API Key
- Reddit API credentials (Client ID, Client Secret, Username, Password)

## Setup Instructions

1. **Clone the repository**:

    ```bash
    git clone https://github.com/Rohit-ghorpade/RedditAIBot
    cd RedditAIBot
    ```

2. **Install dependencies**:

    Make sure you have `pip` installed, then run:

    ```bash
    pip install -r requirements.txt
    ```

3. **Create a `.env` file**:

    Create a `.env` file in the root of your project and add your credentials:

    ```env
    REDDIT_CLIENT_ID=your_reddit_client_id
    REDDIT_CLIENT_SECRET=your_reddit_client_secret
    REDDIT_USERNAME=your_reddit_username
    REDDIT_PASSWORD=your_reddit_password
    GROQ_API_KEY=your_groq_api_key
    ```

4. **Run the bot**:

    Execute the bot script by running:

    ```bash
    python app.py
    ```

    The bot will start posting AI-generated content to Reddit at the scheduled time (default: 09:00 AM).
