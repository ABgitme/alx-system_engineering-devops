#!/usr/bin/python3
"""
    Titles of the first 10 hot posts listed for a given subreddit
"""
import requests


def top_ten(subreddit):
    """
    Print the titles of the first 10 hot posts listed for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit.

    Returns:
        None

    Raises:
        None

    Note:
        This function queries the Reddit API and prints
        the titles of the first 10 hot posts
        listed for the specified subreddit.
        If the subreddit does not exist or is invalid, it
        prints None.

    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = {"User-Agent": "your_user_agent"}

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        data = response.json()
        for post in data['data']['children']:
            print(post['data']['title'])
    except requests.exceptions.HTTPError:
        print("None")
