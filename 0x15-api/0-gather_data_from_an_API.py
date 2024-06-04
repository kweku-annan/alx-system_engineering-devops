#!/usr/bin/python3
"""Accepts an employee ID and returns information"""
import requests
import sys

if __name__ == "__main__":
    userId = sys.argv[1]
    user = requests.get('https://jsonplaceholder.typicode.com/users/{}'
                        .format(userId))
    name = user.json().get('name')

    todos = requests.get('https://jsonplaceholder.typicode.com/todos')
    total_tasks = 0
    completed_tasks = 0
    task_title = ''

    for task in todos.json():
        if task.get('userId') == int(userId):
            total_tasks += 1
            if task.get('completed'):
                completed_tasks += 1
                task_title += "\t {}\n".format(task.get('title'))
    print('Employee {} is done with tasks({}/{}):'.format(
        name, completed_tasks, total_tasks))
    print(task_title, end="")
