#!/usr/bin/python3
"""Accepts an employee ID and returns information"""
import csv
import requests
import sys

if __name__ == "__main__":
    userId = sys.argv[1]
    user = requests.get('https://jsonplaceholder.typicode.com/users/{}'
                        .format(userId))
    name = user.json().get('name')

    todos = requests.get('https://jsonplaceholder.typicode.com/todos')
    tasks = []

    for task in todos.json():
        data = []
        if task.get('userId') == int(userId):
            data.append(task.get('userId'))
            data.append(name)
            data.append(task.get('completed'))
            data.append(task.get('title'))
            tasks.append(data)

    filename = "{}.csv".format(userId)

    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(tasks)
