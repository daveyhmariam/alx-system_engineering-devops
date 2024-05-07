#!/usr/bin/python3
"""Queries the Reddit API and returns the number of subscribers
(not active users, total subscribers) for a given subreddit.
If an invalid subreddit is given, the function should return 0.
"""
import requests


def number_of_subscribers(subreddit):
    """ Returns total subscribers for subreddits

    Args:
        subreddit (str): community on the Reddit
        platform where users can submit posts, comment on posts,
        and engage with other users on specific topics.
    """
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    header = {"User-Agent": "learner"}

    response = requests.get(url=url, headers=header, allow_redirects=False)
    if response.status_code == 404:
        return 0
    else:
        data = response.json()
        return data.get("data")["subscribers"]
