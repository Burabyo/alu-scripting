#!/usr/bin/python3
"""
1-main: Entry script to fetch top 10 posts from a subreddit.
"""

import sys

try:
    top_ten = __import__('top_ten').top_ten  # Ensure file is named `top_ten.py`
except ModuleNotFoundError:
    print("Error: 'top_ten.py' not found. Ensure the script exists in the same directory.")
    sys.exit(1)

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        top_ten(sys.argv[1])
