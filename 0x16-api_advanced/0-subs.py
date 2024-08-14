#!/usr/bin/python3
"""Contains a function that queries the Reddit API"""
import requests


def number_of_subscribers(subreddit):
    """Read reddit API and return number subscribers """
    headers = {'user-agent': '/u/Kweku-Annan API Python'}
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    client = requests.session()
    client.headers = headers
    r = client.get(url, allow_redirects=False)
    if r.status_code == 200:
        return (r.json()["data"]["subscribers"])
    else:
        return (0)
