#!/usr/bin/python3
"""
This module contains a function to query the Reddit API and print the titles
of the first 10 hot posts for a given subreddit.
"""

import requests


def top_ten(subreddit):
    """
    Queries the Reddit API and prints the titles of the first 10 hot posts
    for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit to query.

    Returns:
        None: Prints the titles or None if invalid subreddit.
    """
    if subreddit is None or not isinstance(subreddit, str):
        print(None)
        return

    # Set a custom User-Agent
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                      'AppleWebKit/537.36'
    }

    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)

    try:
        response = requests.get(
            url,
            headers=headers,
            allow_redirects=False,
            params={'limit': 10}
        )

        if response.status_code == 200:
            data = response.json()
            posts = data.get('data', {}).get('children', [])

            if not posts:
                print(None)
                return

            for post in posts:
                print(post.get('data', {}).get('title'))
        else:
            print(None)

    except Exception:
        print(None)
