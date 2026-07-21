#!/usr/bin/python3
<<<<<<< HEAD
"""
Module for querying the Reddit API to get the number of subscribers
for a given subreddit.
"""
=======
"""Return the number of subscribers of a given subreddit"""
>>>>>>> 09d3bb5657f04f34c05f11e302b4f8bede8471bb

import requests


def number_of_subscribers(subreddit):
<<<<<<< HEAD
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

    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {"User-Agent": "PostmanRuntime/7.35.0"}

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)

        if response.status_code == 200:
            data = response.json()
            return data.get("data", {}).get("subscribers", 0)
        else:
            return 0
=======
    """function that fetches number_of_subscribers"""
    URL = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    HEADERS = {"User-Agent": "PostmanRuntime/7.35.0"}

    try:
        RESPONSE = requests.get(URL, headers=HEADERS, allow_redirects=False)
        return RESPONSE.json().get("data").get("subscribers")
>>>>>>> 09d3bb5657f04f34c05f11e302b4f8bede8471bb

    except Exception:
        return 0
