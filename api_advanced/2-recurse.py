#!/usr/bin/python3
"""
Module for recursively querying the Reddit API to get all hot posts
from a given subreddit.
"""

import requests


def recurse(subreddit, hot_list=[], after=None):
    """
    Recursively queries the Reddit API and returns a list containing
    the titles of all hot articles for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit to query.
        hot_list (list): List to accumulate post titles (default: []).
        after (str): Pagination parameter for next page (default: None).

    Returns:
        list: List of all hot post titles, or None if invalid subreddit.
    """
    if subreddit is None or not isinstance(subreddit, str):
        return None

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "ALU-api-project/1.0"}
    params = {"limit": 100, "after": after} if after else {"limit": 100}

    try:
        response = requests.get(
            url,
            headers=headers,
            params=params,
            allow_redirects=False
        )

        if response.status_code != 200:
            return None

        data = response.json()
        children = data.get("data", {}).get("children", [])
        after_param = data.get("data", {}).get("after")

        if not children:
            return hot_list if hot_list else None

        for child in children:
            hot_list.append(child.get("data", {}).get("title"))

        if after_param is not None:
            return recurse(subreddit, hot_list, after_param)
        else:
            return hot_list

    except Exception:
        return None
