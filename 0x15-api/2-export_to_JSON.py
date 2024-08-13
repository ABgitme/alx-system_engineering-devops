#!/usr/bin/python3
"""
    Provides details on the progress of the
    TODO list for a specified employee ID.
"""
import csv
import json
import requests
import sys


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
    employee_name = user_data.get("username")
    user_id = user_data['id']

    # Fetch todos
    todos_response = requests.get(url + f"todos?userId={employee_id}")
    if todos_response.status_code != 200:
        return

    todos_data = todos_response.json()

    # Export to CSV
    with open("{}.csv".format(user_id), "w", newline="") as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        [writer.writerow(
            [user_id, employee_name, t.get("completed"), t.get("title")]
         ) for t in todos_data]
    # Export to JSON
    json_data = {str(user_id): [{"task":t.get("title"),
                                 "completed":t.get("completed"),
                                 "username": employee_name} for t in todos_data]}
    with open(f"{user_id}.json", "w") as jsonfile:
        json.dump(json_data, jsonfile, indent=4)


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
