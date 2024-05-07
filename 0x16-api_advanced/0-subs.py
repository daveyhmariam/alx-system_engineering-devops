#!/usr/bin/python3
''' fetching subreddit data'''
import requests


def number_of_subscribers(subreddit):
    '''finding the number of subscribers for a valid subreddit'''
    response = requests.get(f'https://reddit.com/r/{subreddit}/about.json')

    if response.status_code != 200:
        return 0

    return response.json().get('data', {}).get('subscribers')
