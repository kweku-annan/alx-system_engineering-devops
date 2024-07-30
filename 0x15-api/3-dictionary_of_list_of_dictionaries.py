#!/usr/bin/python3
"""Accepts an employee ID and returns information"""
import json
import requests
import sys

if __name__ == "__main__":
    users = requests.get('https://jsonplaceholder.typicode.com/users/').json()
    data = {}
    todos = requests.get('https://jsonplaceholder.typicode.com/todos').json()

    for user in users:
        userId = user.get('id')
        username = user.get('username')
        task_list = []
        for task in todos:
            task_data = {}
            if task.get('userId') == int(userId):
                task_data["task"] = task.get("title")
                task_data["completed"] = task.get("completed")
                task_data["username"] = username
                task_list.append(task_data)

        data[userId] = task_list

    file_path = f'todo_all_employees.json'

    with open(file_path, 'w') as a_file:
        json.dump(data, a_file)
