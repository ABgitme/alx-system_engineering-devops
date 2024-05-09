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
    response = requests.get(
        f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10",
        headers={"User-Agent": "My-User-Agent"},
        allow_redirects=False)

    if response.status_code >= 300:
        print('None')
    else:
        [print(
            child['data']['title'])
            for child in response.json().get('data', {}).get('children', [])]
