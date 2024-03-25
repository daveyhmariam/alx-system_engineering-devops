#!/usr/bin/python3
"""
retrieves and displays the completed tasks
of a specific employee from a JSON API.
"""
import json
import requests
from sys import argv


def main():
    '''getting data for an api'''
    url = f'https://jsonplaceholder.typicode.com/users/{argv[1]}'
    url2 = f'https://jsonplaceholder.typicode.com/users/{argv[1]}/todos'
    response = requests.get(url)
    name = response.json().get('username', None)
    json_dict = []
    response = requests.get(url2)

    for task in response.json():
        dic = {}
        dic['task'] = task.get('title')
        dic['completed'] = task.get('completed')
        dic['username'] = name
        json_dict.append(dic)

    filename = argv[1] + '.json'

    with open(filename, 'w', encoding='utf-8') as f:
        json.dump({argv[1]: json_dict}, f)


if __name__ == '__main__':
    main()
