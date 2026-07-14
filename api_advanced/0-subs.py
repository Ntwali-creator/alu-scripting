#!/usr/bin/python3
"""
Module for querying the Reddit API to get number of subscribers
"""
import requests


def number_of_subscribers(subreddit):
    """
    Queries the Reddit API and returns the number of subscribers
    for a given subreddit. Returns 0 if invalid.
    """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {
        'User-Agent': 'python:alu-reddit-app:v1.0 (by /u/Ntwali-creator)'
    }
    
    try:
        response = requests.get(url, headers=headers, timeout=10)
        if response.status_code == 200:
            data = response.json()
            return data['data']['subscribers']
        return 0
    except:
        return 0
