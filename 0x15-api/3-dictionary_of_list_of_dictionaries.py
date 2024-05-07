#!/usr/bin/python3
"""using this REST API, for a given employee ID, returns
    information about his/her TODO list progress.

"""
import json
import requests
import sys

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    users = requests.get(url + "users").json()
    all_dict = dict()
    for user in users:
        user_id = user["id"]
        todos = requests.get(url + "todos", params={"userId": user_id}).json()
        user_list = []
        for todo in todos:
            user_dict = {}
            user_dict["username"] = user["name"]
            user_dict["task"] = todo["title"]
            user_dict["completed"] = todo["completed"]
            user_list.append(user_dict)
        all_dict[user_id] = user_list
    with open("todo_all_employees.json", "w") as f:
        json.dump(all_dict, f, indent=4)
            