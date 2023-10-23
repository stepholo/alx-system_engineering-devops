#!/usr/bin/python3
"""Module to define function get_data"""


if __name__ == '__main__':
    import requests
    from sys import argv
    import json

    emp_id = int(argv[1])
    url_todos = f'https://jsonplaceholder.typicode.com/user/{emp_id}/todos'
    url_user = f'https://jsonplaceholder.typicode.com/users/{emp_id}'

    response_todos = requests.get(url_todos)
    response_user = requests.get(url_user)

    if response_todos.status_code == 200:
        data_todos = response_todos.json()

    if response_user.status_code == 200:
        data_user = response_user.json()

    filename = f'{emp_id}.json'
    username = f"{data_user.get('username')}"
    user_id = f"{emp_id}"
    data = {user_id: []}
    for dat in data_todos:
        task = dat.get('title')
        complete = dat.get('completed')
        new_dict = {
                "task": task,
                "completed": complete,
                "username": username
                }
        data[user_id].append(new_dict)
    with open(filename, "w") as f:
        json.dump(data, f, indent=None)
