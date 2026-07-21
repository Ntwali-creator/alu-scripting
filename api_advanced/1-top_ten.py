#!/usr/bin/python3
<<<<<<< HEAD
"""Prints the title of the first 10 hot posts listed for a given subreddit"""
=======
"""
Module for querying the Reddit API and printing the top 10 hot posts
for a given subreddit.
"""
>>>>>>> Final: Task 1 complete with all checks passing

import requests


def top_ten(subreddit):
<<<<<<< HEAD
    """Main function"""
    URL = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
=======
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

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "PostmanRuntime/7.35.0"}
    params = {"limit": 10}
>>>>>>> Final: Task 1 complete with all checks passing

    HEADERS = {"User-Agent": "PostmanRuntime/7.35.0"}
    try:
<<<<<<< HEAD
        RESPONSE = requests.get(URL, headers=HEADERS, allow_redirects=False)
        HOT_POSTS = RESPONSE.json().get("data").get("children")
        [print(post.get('data').get('title')) for post in HOT_POSTS]
=======
        response = requests.get(
            url,
            headers=headers,
            params=params,
            allow_redirects=False
        )

        if response.status_code == 200:
            data = response.json()
            children = data.get("data", {}).get("children", [])

            if not children:
                print(None)
                return

            for child in children:
                title = child.get("data", {}).get("title")
                if title:
                    print(title)
        else:
            print(None)

>>>>>>> Final: Task 1 complete with all checks passing
    except Exception:
        print(None)
