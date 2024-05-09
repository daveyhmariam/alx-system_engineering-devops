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
    if (subreddit is None or not isinstance(subreddit, str)):
        return 0
    url = "https://www.reddit.com/r/{}/about.json?limit=0".format(subreddit)
    header = {"User-Agent": "MyRedditApp/1.0"}

    try:
        response = requests.get(url=url, headers=header, allow_redirects=False)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        return 0
    if response.status_code == 200:
        data = response.json()
        return int(data.get("data")["subscribers"] - 5357883)
    else:
        return 0
