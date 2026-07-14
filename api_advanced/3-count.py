#!/usr/bin/python3
"""
Module for querying the Reddit API and counting keywords in hot posts
"""
import requests
import re


def count_words(subreddit, word_list, after=None, word_count=None):
    """
    Recursively queries the Reddit API, parses the title of all hot articles,
    and prints a sorted count of given keywords (case-insensitive).
    """
    if word_count is None:
        word_count = {}
        word_list = [word.lower() for word in word_list]
    
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {
        'User-Agent': 'python:alu-reddit-app:v1.0 (by /u/Ntwali-creator)'
    }
    params = {'limit': 100}
    
    if after:
        params['after'] = after
    
    try:
        response = requests.get(url, headers=headers, params=params, timeout=10)
        if response.status_code != 200:
            if word_count:
                print_results(word_count, word_list)
            return
        
        data = response.json()
        children = data['data']['children']
        
        if not children:
            if word_count:
                print_results(word_count, word_list)
            return
        
        for child in children:
            title = child['data']['title'].lower()
            words = re.findall(r'[a-zA-Z0-9]+', title)
            for word in words:
                if word in word_list:
                    word_count[word] = word_count.get(word, 0) + 1
        
        after = data['data']['after']
        if after:
            return count_words(subreddit, word_list, after, word_count)
        else:
            print_results(word_count, word_list)
            return
    except:
        if word_count:
            print_results(word_count, word_list)
        return


def print_results(word_count, word_list):
    """Prints results in descending order by count."""
    if not word_count:
        return
    
    total_counts = {}
    for word in set(word_list):
        total_counts[word] = word_count.get(word, 0)
    
    total_counts = {k: v for k, v in total_counts.items() if v > 0}
    
    if not total_counts:
        return
    
    sorted_items = sorted(total_counts.items(), key=lambda x: (-x[1], x[0]))
    
    for word, count in sorted_items:
        print(f"{word}: {count}")
