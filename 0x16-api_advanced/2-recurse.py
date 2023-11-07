#!/usr/bin/python3
"""Module to write function recurse"""

import requests


def recurse(sub, hot_list=[], after=None):
    """Recursive function that queries the Reddit API and returns
        a list containing the titles of all hot articles for
        a given subreddit. If no results are found for the given subreddit,
        the function should return None.
    """
    user_agent = 'Custom User Agent'
    headers = {'User-Agent': user_agent}
    url = f'https://www.reddit.com/r/{sub}/hot.json?limit=100&after={after}'

    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200 and not response.is_redirect:
        data = response.json()
        posts = data['data']['children']
        for post in posts:
            title = post['data']['title']
            hot_list.append(title)

        after = data['data']['after']
        if after:
            return recurse(subreddit, hot_list, after)
        else:
            return hot_list
    else:
        return None
