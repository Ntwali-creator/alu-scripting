# API Advanced - Reddit API Project

This project contains Python scripts that interact with the Reddit API to retrieve and analyze data from subreddits.

## Requirements

- Python 3.4.3+
- Requests module
- PEP 8 style
- All files executable

## Tasks

### 0. How many subs?
File: 0-subs.py
Function: def number_of_subscribers(subreddit)
Returns the number of subscribers for a given subreddit. Returns 0 if invalid.

### 1. Top Ten
File: 1-top_ten.py
Function: def top_ten(subreddit)
Prints the titles of the first 10 hot posts for a given subreddit. Prints None if invalid.

### 2. Recurse it!
File: 2-recurse.py
Function: def recurse(subreddit, hot_list=[])
Returns a list containing the titles of all hot articles for a given subreddit using recursion. Returns None if invalid.

### 3. Count it!
File: 3-count.py
Function: def count_words(subreddit, word_list)
Parses the title of all hot articles and prints a sorted count of given keywords (case-insensitive).

## Usage

# Task 0 - Get subscribers
python3 0-main.py programming

# Task 1 - Top 10 hot posts
python3 1-main.py programming

# Task 2 - All hot posts (recursive)
python3 2-main.py programming

# Task 3 - Count keywords
python3 3-main.py programming 'python java javascript react scala'

## Author

James Ntwali - ALU Student

## License

This project is for educational purposes as part of the ALU curriculum.
