#!/usr/bin/python3
"""Accepts an employee ID and returns information"""
import json
import requests
import sys

if __name__ == "__main__":
    userId = sys.argv[1]
    user = requests.get('https://jsonplaceholder.typicode.com/users/{}'
                        .format(userId))
    name = user.json().get('name')

    todos = requests.get('https://jsonplaceholder.typicode.com/todos')
    task_data_list = []
    data = {}

    for task in todos.json():
        task_data = {}
        if task.get('userId') == int(userId):
            task_data["task"] = task.get('title')
            task_data["completed"] = task.get('completed')
            task_data["username"] = name
            task_data_list.append(task_data)

    data[userId] = task_data_list

    file_path = f'{userId}.json'

    with open(file_path, 'w') as a_file:
        json.dump(data, a_file)
