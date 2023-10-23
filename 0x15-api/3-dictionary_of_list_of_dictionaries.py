#!/usr/bin/python3
"""Module to define function get_data"""


if __name__ == '__main__':
    import requests
    import json

    url_todos = 'https://jsonplaceholder.typicode.com/todos'
    url_user = 'https://jsonplaceholder.typicode.com/users'

    response_todos = requests.get(url_todos)
    response_user = requests.get(url_user)

    if response_todos.status_code == 200:
        data_todos = response_todos.json()

    if response_user.status_code == 200:
        data_user = response_user.json()

    filename = 'todo_all_employees.json'
    data = {}

    for user in data_user:
        username = user['username']
        user_id = user['id']
        user_task = []
        for dat in data_todos:
            if user_id == dat['userId']:
                new_dict = {
                    "task": dat.get('title'),
                    "completed": dat.get('completed'),
                    "username": username
                    }
                user_task.append(new_dict)
        data[user_id] = user_task
    with open(filename, "w") as f:
        json.dump(data, f, indent=None)
