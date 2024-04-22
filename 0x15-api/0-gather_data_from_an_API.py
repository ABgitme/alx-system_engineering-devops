#!/usr/bin/python3
# handle fetching of TODO list progress
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
    employee_name = user_data['name']

    # Fetch todos
    todos_response = requests.get(url + f"todos?userId={employee_id}")
    if todos_response.status_code != 200:
        return

    todos_data = todos_response.json()
    total_tasks = len(todos_data)
    completed_tasks = [todo for todo in todos_data if todo['completed']]

    # Display progress
    print(f"Employee {employee_name} is done with tasks\
        ({len(completed_tasks)}/{total_tasks}):")
    # print(f"{employee_name}: name of the employee")
    # print(f"{len(completed_tasks)}/{total_tasks}: number of completed tasks")

    for task in completed_tasks:
        print(f"\t{task['title']}")


if __name__ == "__main__":
    """
    Entry point of the script.

    Checks if the script is being run as the main program. If so, it expects
    one command-line argument which is the employee ID. It then calls the
    get_employee_todo_progress function with the provided employee ID.
    """
    import sys
    if len(sys.argv) != 2:
        sys.exit(1)

    employee_id = int(sys.argv[1])
    get_employee_todo_progress(employee_id)
