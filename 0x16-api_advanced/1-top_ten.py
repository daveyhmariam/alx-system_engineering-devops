#!/usr/bin/python3
"""Queries the Reddit API and returns the number of subscribers
(not active users, total subscribers) for a given subreddit.
If an invalid subreddit is given, the function should return 0.
"""
import requests


def top_ten(subreddit):
    """ Returns total subscribers for subreddits

    Args:
        subreddit (str): community on the Reddit
        platform where users can submit posts, comment on posts,
        and engage with other users on specific topics.
    """
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    header = {"User-Agent": "MyRedditApp/1.0"}

    response = requests.get(url=url, headers=header, allow_redirects=False)
    if response.status_code == 404:
        print("None")
        return 0
    else:
        data = response.json().get("data")
        [print(cld["data"]["title"]) for cld in data["children"]]

