#!/usr/bin/python3
"""
Module for querying the Reddit API to get top 10 hot posts
"""
import requests


def top_ten(subreddit):
    """
    Queries the Reddit API and prints the titles of the first 10 hot posts
    for a given subreddit. Prints None if invalid.
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {
        'User-Agent': 'python:alu-reddit-app:v1.0 (by /u/Ntwali-creator)'
    }
    params = {'limit': 10}
    
    try:
        response = requests.get(url, headers=headers, params=params, allow_redirects=False, timeout=10)
        if response.status_code != 200:
            print(None)
            return
        
        data = response.json()
        children = data['data']['children']
        
        if not children:
            print(None)
            return
        
        for child in children:
            print(child['data']['title'])
    except Exception:
        print(None)
