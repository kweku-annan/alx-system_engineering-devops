#!/usr/bin/python3
"""Accepts an employee ID and returns information"""
import json
import requests
import sys

if __name__ == "__main__":
    userId = sys.argv[1]
    user = requests.get('https://jsonplaceholder.typicode.com/users/{}'
                        .format(userId)).json()

    name = user.get('name')
    username = user.get('username')

    todos = requests.get('https://jsonplaceholder.typicode.com/todos').json()
    task_list = []
    data = {}

    for task in todos:
        task_data = {}
        if task.get('userId') == int(userId):
            task_data["task"] = task.get('title')
            task_data["completed"] = task.get('completed')
            task_data["username"] = username
            task_list.append(task_data)

    data[userId] = task_list

    file_path = f'{userId}.json'

    with open(file_path, 'w') as a_file:
        json.dump(data, a_file)
