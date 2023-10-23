#!/usr/bin/python3
"""Module to define function get_data"""


if __name__ == '__main__':
    import requests
    from sys import argv
    import csv

    emp_id = int(argv[1])
    url_todos = f'https://jsonplaceholder.typicode.com/user/{emp_id}/todos'
    url_user = f'https://jsonplaceholder.typicode.com/users/{emp_id}'

    response_todos = requests.get(url_todos)
    response_user = requests.get(url_user)

    if response_todos.status_code == 200:
        data_todos = response_todos.json()

    if response_user.status_code == 200:
        data_user = response_user.json()

    filename = f'{emp_id}.csv'
    username = data_user.get('username')
    with open(filename, 'w', newline='') as csvfile:
        fieldnames = [
                'USER_ID',
                'USERNAME',
                'TASK_COMPLETED_STATUS',
                'TASK_TITLE'
                ]
        writer = csv.DictWriter(
                csvfile, fieldnames=fieldnames,
                quotechar='"', quoting=csv.QUOTE_NONNUMERIC
                )

        for task in data_todos:
            complete = 'True' if task['completed'] else 'False'
            task_title = task['title']
            writer.writerow({
                'USER_ID': f'{emp_id}',
                'USERNAME': username,
                'TASK_COMPLETED_STATUS': complete,
                'TASK_TITLE': task_title
                })
