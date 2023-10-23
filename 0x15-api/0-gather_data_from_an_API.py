#!/usr/bin/python3
"""Module to define function get_data"""


if __name__ == '__main__':
    import requests
    from sys import argv

    emp_id = int(argv[1])
    url_todos = f'https://jsonplaceholder.typicode.com/user/{emp_id}/todos'
    url_user = f'https://jsonplaceholder.typicode.com/users/{emp_id}'

    response_todos = requests.get(url_todos)
    response_user = requests.get(url_user)

    if response_todos.status_code == 200:
        data_todos = response_todos.json()

    if response_user.status_code == 200:
        data_user = response_user.json()

    name = data_user.get('name')
    title = []
    task_c = 0
    uncomplete_task = 0

    for di_ct in data_todos:
        if di_ct.get('completed') is True:
            task_c += 1
            title.append(di_ct.get('title'))
        else:
            uncomplete_task += 1

    total = task_c + uncomplete_task

    print(f'Employee {name} is done with tasks({task_c}/{total}):')
    for titl in title:
        print(f'\t {titl}')
