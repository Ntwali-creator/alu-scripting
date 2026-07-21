#!/usr/bin/python3
"""Prints the title of the first 10 hot posts listed for a given subreddit"""

import requests


def top_ten(subreddit):
    """Prints the first 10 hot posts of a subreddit"""
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)

    headers = {
        "User-Agent": "ALU-api-project/1.0"
    }

    try:
        response = requests.get(url, headers=headers,
                                allow_redirects=False)

        data = response.json()
        posts = data.get("data", {}).get("children")

        if posts is None:
            print(None)
            return

        for post in posts[:10]:
            print(post.get("data", {}).get("title"))

    except Exception:
        print(None)
