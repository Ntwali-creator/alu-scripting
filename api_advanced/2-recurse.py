#!/usr/bin/python3
"""
Module for querying the Reddit API to get all hot post titles recursively
"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """
    Recursively queries the Reddit API and returns a list containing
    the titles of all hot articles for a given subreddit.
    Returns None if invalid.
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {
        'User-Agent': 'python:alu-reddit-app:v1.0 (by /u/Ntwali-creator)'
    }
    params = {'limit': 100}
    
    if after:
        params['after'] = after
    
    try:
        response = requests.get(url, headers=headers, params=params, allow_redirects=False, timeout=10)
        if response.status_code != 200:
            return None if not hot_list else hot_list
        
        data = response.json()
        children = data['data']['children']
        
        if not children:
            return None if not hot_list else hot_list
        
        for child in children:
            hot_list.append(child['data']['title'])
        
        after = data['data']['after']
        if after:
            return recurse(subreddit, hot_list, after)
        return hot_list
    except Exception:
        return None if not hot_list else hot_list
