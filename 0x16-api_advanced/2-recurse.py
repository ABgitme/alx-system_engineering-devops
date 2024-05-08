#!/usr/bin/python3

import requests


def recurse(subreddit, hot_list=None, after=None):
    """
    Recursively query the Reddit API to retrieve
    all hot articles for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit.
        hot_list (list): List to store the titles
        of hot articles. Default is None.
        after (str): The "after" parameter for pagination.
        Default is None.

    Returns:
        list: A list containing the titles of all hot
        articles for the given subreddit,
        or None if no results are found.

    Raises:
        None

    Note:
        This function recursively queries the Reddit API
        to retrieve all hot articles for the specified subreddit.
        If the subreddit does not exist or is invalid,
        it returns None.
    """
    if hot_list is None:
        hot_list = []

    # URL for the Reddit API endpoint to get hot posts in a subreddit
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=100"
    # Adding a custom User-Agent header to prevent Too Many Requests error
    headers = {'User-Agent': 'Custom User Agent'}
    # Parameters for pagination
    params = {'after': after} if after else {}
    # Making a GET request to the API
    response = requests.get(url, headers=headers,
                            params=params, allow_redirects=False)
    # Checking if the response is successful (status code 200)
    # and if the subreddit exists
    if response.status_code == 200:
        data = response.json()
        if 'data' in data and 'children' in data['data']:
            # Extracting titles from the response
            # JSON and appending them to hot_list
            for post in data['data']['children']:
                hot_list.append(post['data']['title'])
            # Recursively call the function with the
            # 'after' parameter for pagination
            if data['data']['after']:
                return recurse(subreddit, hot_list, data['data']['after'])
            else:
                return hot_list
        else:
            # If the subreddit exists but no posts are found, return None
            return None
    else:
        # If the status code is not 200, it means the subreddit is invalid
        return None
