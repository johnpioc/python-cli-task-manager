import time
import os
from database.database_helper import setup_database


def display_tasks_and_commands():
    print("You currently have no tasks")
    print()
    print("> add-task - add a new task")
    print("> toggle-complete n - toggles the completion of task n")
    print("> update-task-name n - update the name of task n")
    print("> delete-task n - deletes tasks n")
    print("> q - quit the application")
    print()

def parse_user_input(user_input):
    if user_input == "":
        return False, "Empty input, please try again"

    components = user_input.split(" ")
    command = components[0]

    match command:
        case _:
            return False, "Invalid input, please try again"

def main():

    print("Welcome to the task manager.")
    print()

    setup_database()

    while True:
        display_tasks_and_commands()
        user_input = input("Type a command: ")
        print()

        status, error_message = parse_user_input(user_input)
        if status is False:
            print(error_message)
            time.sleep(3)
            continue


main()