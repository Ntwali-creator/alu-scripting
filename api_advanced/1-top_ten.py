#!/usr/bin/python3
"""Prints the title of the first 10 hot posts listed for a given subreddit"""

import requests


def top_ten(subreddit):
    """Prints the first 10 hot posts of a subreddit"""
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)

    headers = {
        "User-Agent": "ALU-api-project/1.0"
    }

    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        print(None)
        return

    try:
        posts = response.json()["data"]["children"]

        for post in posts[:10]:
            print(post["data"]["title"])

    except Exception:
        print(None)
