#!/usr/bin/python3
"""
    Retrieve the number of subscribers for a given subreddit.
"""
import requests


def number_of_subscribers(subreddit):
    """
        URL for the Reddit API endpoint to get subreddit information
    """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"

    # Adding a custom User-Agent header to prevent Too Many Requests error
    headers = {'User-Agent': 'Custom User Agent'}

    # Making a GET request to the API
    response = requests.get(url, headers=headers, allow_redirects=False)

    # Checking if the response is successful (status code 200)
    # and if the subreddit exists
    if response.status_code == 200:
        data = response.json()
        # Checking if the 'subscribers' key exists in the JSON response
        if 'subscribers' in data['data']:
            return data['data']['subscribers']
        else:
            # If the 'subscribers' key doesn't exist,
            # it means the subreddit is invalid
            return 0
    else:
        # If the status code is not 200, it means the subreddit is invalid
        return 0
