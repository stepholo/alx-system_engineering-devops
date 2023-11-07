#!/usr/bin/python3
"""Module to write function top_ten"""

import requests


def top_ten(subreddit):
    """Function that queries the Reddit API and prints
        the titles of the first 10 hot posts listed for a given subreddit
    """
    user_agent = 'Custom User Agent'
    headers = {'User-Agent': user_agent}
    url = f'https://www.reddit.com/r/{subreddit}/hot.json?limit=10'

    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200 and not response.is_redirect:
        data = response.json()
        posts = data['data']['children']
        for post in posts:
            title = post['data']['title']
            print(title)
    else:
        print(None)
