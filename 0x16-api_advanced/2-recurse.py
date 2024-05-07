#!/usr/bin/python3
"""
recursive function that queries the Reddit API
and returns a list containing the titles of all hot articles
for a given subreddit. If no results are found for the given subreddit,
the function should return None.
"""
import requests


def recurse(subreddit, hot_list=[], cnt=0, a=""):
    """Returns a list of titles of all hot posts on a given subreddit."""
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    headers = {
        "User-Agent": "myreddit api)"
    }
    param = {
        "after": a,
        "count": cnt,
        "limit": 100
    }
    response = requests.get(url,
                            headers=headers,
                            params=param,
                            allow_redirects=False)
    if response.status_code == 404:
        return None

    results = response.json().get("data")
    a = results.get("after")
    cnt += results.get("dist")
    for c in results.get("children"):
        hot_list.append(c.get("data").get("title"))

    if a is not None:
        return recurse(subreddit, hot_list, cnt, a)
    return hot_list
