#!/usr/bin/python3
"""Module to write function number_of_subscribers"""

import requests


def number_of_subscribers(subreddit):
    """Function that queries the Reddit API and returns the
        number of subscribers for a given subreddit
    """
    user_agent = 'Custom User Agent'
    headers = {'User-Agent': user_agent}
    url = f'https://www.reddit.com/r/{subreddit}/about.json'

    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200 and not response.is_redirect:
        data = response.json()
        subscribers_count = data['data']['subscribers']
        return subscribers_count
    else:
        return 0
