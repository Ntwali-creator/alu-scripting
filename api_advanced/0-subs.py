#!/usr/bin/python3
"""
Module for querying the Reddit API to get the number of subscribers
for a given subreddit.
"""

import requests


def number_of_subscribers(subreddit):
    """
    Queries the Reddit API and returns the number of subscribers
    for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit to query.

    Returns:
        int: The number of subscribers, or 0 if the subreddit is invalid.
    """
    if subreddit is None or not isinstance(subreddit, str):
        return 0

    # Set a custom User-Agent
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                      'AppleWebKit/537.36'
    }

    # Use the about.json endpoint (not the general .json endpoint)
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)

    try:
        response = requests.get(
            url,
            headers=headers,
            allow_redirects=False,  # Don't follow redirects for invalid subs
            timeout=10
        )

        if response.status_code == 200:
            data = response.json()
            # Get subscribers from the about endpoint
            return data.get('data', {}).get('subscribers', 0)
        else:
            return 0

    except requests.RequestException:
        return 0
