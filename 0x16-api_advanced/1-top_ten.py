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
    # URL for the Reddit API endpoint to get hot posts in a subreddit
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    # Adding a custom User-Agent header to prevent Too Many Requests error
    headers = {'User-Agent': 'Custom User Agent'}
    # Making a GET request to the API
    response = requests.get(url, headers=headers, allow_redirects=False)
    # Checking if the response is successful (status code 200)
    # and if the subreddit exists
    if response.status_code == 200:
        data = response.json()
        if 'data' in data and 'children' in data['data']:
            # Extracting titles from the response JSON and printing them
            for i, post in enumerate(data['data']['children'], 1):
                print(f"{post['data']['title']}")
        else:
            # If the subreddit exists but no posts are found, print None
            print("None")
    else:
        # If the status code is not 200, it means the subreddit is invalid
        print("None")
