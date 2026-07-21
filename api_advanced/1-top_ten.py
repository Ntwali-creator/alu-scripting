#!/usr/bin/python3
"""
Module for querying the Reddit API and printing the top 10 hot posts.
"""

import requests


def top_ten(subreddit):
    """
    Prints the titles of the first 10 hot posts for a given subreddit.
    If invalid subreddit, prints None.
    """
    if subreddit is None or type(subreddit) is not str:
        print(None)
        return

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "MyBot/1.0"}
    params = {"limit": 10}

    try:
        response = requests.get(
            url,
            headers=headers,
            params=params,
            allow_redirects=False
        )

        if response.status_code == 200:
            data = response.json()
            posts = data.get("data", {}).get("children", [])

            if posts:
                for post in posts:
                    print(post.get("data", {}).get("title"))
            else:
                print(None)
        else:
            print(None)

    except Exception:
        print(None)
