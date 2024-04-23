#!/usr/bin/python3
"""
    Provides details on the progress of the
    TODO list for a specified employee ID.
"""
import requests
import sys
import csv


def get_employee_todo_progress(employee_id):
    """
    Fetches and displays the TODO list progress for a given employee ID.

    Args:
        employee_id (int): The ID of the employee.

    Returns:
        None
    """
    url = 'https://jsonplaceholder.typicode.com/'
    user_response = requests.get(url + f"users/{employee_id}")
    if user_response.status_code != 200:
        return

    user_data = user_response.json()
    employee_name = user_data['name']
    user_id = user_data['id']

    # Fetch todos
    todos_response = requests.get(url + f"todos?userId={employee_id}")
    if todos_response.status_code != 200:
        return

    todos_data = todos_response.json()

    # Display progress
    # print('Employee {} is done with tasks({}/{}):'
    #     .format(employee_name, len(completed_tasks), total_tasks))
    # print(f"{employee_name}: name of the employee")
    # print(f"{len(completed_tasks)}/{total_tasks}: number of completed tasks")

    # Export to CSV
    filename = f"{user_id}.csv"
    with open(filename, 'w', newline='') as csvfile:
        fieldnames = ['USER_ID', 'USERNAME',
                      'TASK_COMPLETED_STATUS', 'TASK_TITLE']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for task in todos_data:
            writer.writerow({
                'USER_ID': user_id,
                'USERNAME': employee_name,
                'TASK_COMPLETED_STATUS':
                    "True" if task['completed'] else "False",
                'TASK_TITLE': task['title']
            })


if __name__ == "__main__":
    """
    Entry point of the script.

    Checks if the script is being run as the main program. If so, it expects
    one command-line argument which is the employee ID. It then calls the
    get_employee_todo_progress function with the provided employee ID.
    """
    if len(sys.argv) != 2:
        sys.exit(1)

    employee_id = int(sys.argv[1])
    get_employee_todo_progress(employee_id)
