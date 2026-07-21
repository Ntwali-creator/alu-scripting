#!/usr/bin/python3
"""
Returns the number of subscribers from a subreddit
"""
import requests


def number_of_subscribers(subreddit):
    """Set a custom header user-agent and query Reddit API"""
    headers = {"User-Agent": "ALU-scripting API 0.1"}

    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)

    try:
        response = requests.get(
            url,
            headers=headers,
            timeout=30,
            allow_redirects=False
        )

    except requests.exceptions.RequestException:
        return 0

    if response.status_code == 200:
        json_data = response.json()
        subscriber_number = json_data.get("data", {}).get("subscribers", 0)
        return subscriber_number
    else:
        return 0
