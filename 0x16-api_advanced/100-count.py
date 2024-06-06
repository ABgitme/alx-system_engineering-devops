#!/usr/bin/python3
"""
recursive function that queries the Reddit API,
parses the title of all hot articles,
and prints a sorted count of given keywords.
"""
import requests


def count_words(subreddit, word_list, after=None, counts=None):
    """
    Recursively query the Reddit API to count occurrences
    of given keywords in hot articles.

    Args:
        subreddit (str): The name of the subreddit.
        word_list (list): List of keywords to count occurrences for.
        after (str): The "after" parameter for pagination. Default is None.
        counts (dict): Dictionary to store counts of keywords. Default is None.

    Returns:
        None

    Raises:
        None

    Note:
        This function recursively queries the Reddit API
        to count occurrences of given keywords
        in hot articles for the specified subreddit.
        The results are printed in descending order
        by count, and if the count is the same for separate keywords,
        they are sorted alphabetically.
    """
    if counts is None:
        counts = {}

    # URL for the Reddit API endpoint to get hot posts in a subreddit
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=100"
    # Adding a custom User-Agent header to prevent Too Many Requests error
    headers = {'User-Agent': 'Custom User Agent'}
    # Parameters for pagination
    params = {'after': after} if after else {}
    # Making a GET request to the API
    response = requests.get(url, headers=headers,
                            params=params, allow_redirects=False)
    # Checking if the response is successful
    # (status code 200) and if the subreddit exists
    if response.status_code == 200:
        data = response.json()
        if 'data' in data and 'children' in data['data']:
            # Extracting titles from the response JSON
            # and counting occurrences of keywords
            for post in data['data']['children']:
                title = post['data']['title'].lower()
                for word in word_list:
                    if title.count(word.lower()) > 0:
                        counts[word.lower()] = counts.get(
                            word.lower(), 0) + title.count(word.lower())
            # Recursively call the function with
            # the 'after' parameter for pagination
            if data['data']['after']:
                return count_words(
                    subreddit, word_list, data['data']['after'], counts)
            else:
                # Sort the counts dictionary by count (descending)
                # and then by keyword (ascending)
                sorted_counts = sorted(
                    counts.items(), key=lambda x: (-x[1], x[0]))
                # Print the sorted counts
                for word, count in sorted_counts:
                    print(f"{word}: {count}")
        else:
            # If the subreddit exists but no posts are found, print nothing
            return
    else:
        # If the status code is not 200, it means the subreddit is invalid
        return
