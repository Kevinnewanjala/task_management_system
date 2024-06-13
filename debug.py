# debug.py

from datetime import datetime  # Correct import for datetime
from database.connection import create_db_session
from models.name import create_name, read_names, update_name, delete_name
from models.task import create_task, read_tasks, update_task, delete_task
from models.label import create_label, read_labels, update_label, delete_label
from utils import validate_date, get_yes_no_input

def main():
    session = create_db_session()

    while True:
        print("\nMenu:")
        menu_options = [
            "Create Name",
            "Read Names",
            "Update Name",            "Delete Name",
            "Create Task",
            "Read Tasks",
            "Update Task",
            "Delete Task",
            "Create Label",
            "Read Labels",
            "Update Label",
            "Delete Label",
            "Validate Date",
            "Exit"
        ]
        for index, option in enumerate(menu_options, start=1):
            print(f"{index}. {option}")

        choice = input("Enter your choice: ")

        if choice == "1":
            name_data = {
                "name": input("Enter name: ").strip(),
                "role": input("Enter role: ").strip()
            }
            if not all(name_data.values()):
                print("Kindly make a valid entry to proceed.")
                continue
            create_name(session, **name_data)
        elif choice == "2":
            read_names(session)
        elif choice == "3":
            name_id = input("Enter name ID to update: ").strip()
            if not name_id:
                print("Kindly make a valid entry to proceed.")
                continue
            update_name(session, int(name_id))
        elif choice == "4":
            name_id = input("Enter name ID to delete: ").strip()
            if not name_id:
                print("Kindly make a valid entry to proceed.")
                continue
            delete_name(session, int(name_id))
        elif choice == "5":
            task_data = {
                "title": input("Enter task title: ").strip(),
                "description": input("Enter task description: ").strip(),
                "due_date": input("Enter due date (YYYY-MM-DD): ").strip(),
                "name_id": input("Enter name ID: ").strip()
            }
            if not all(task_data.values()):
                print("Kindly make a valid entry to proceed.")
                continue
            try:
                task_data["due_date"] = datetime.strptime(task_data["due_date"], '%Y-%m-%d').date()
                if task_data["due_date"] < datetime.now().date():
                    print("Due date must be a future date.")
                else:
                    create_task(session, **task_data)
            except ValueError:
                print("Invalid date format. Please enter the due date in YYYY-MM-DD format.")
        elif choice == "6":
            read_tasks(session)
        elif choice == "7":
            task_id = input("Enter task ID to update: ").strip()
            if not task_id:
                print("Kindly make a valid entry to proceed.")
                continue
            update_task(session, int(task_id))
        elif choice == "8":
            task_id = input("Enter task ID to delete: ").strip()
            if not task_id:
                print("Kindly make a valid entry to proceed.")
                continue
            delete_task(session, int(task_id))
        elif choice == "9":
            label_data = {
                "name": input("Enter label name: ").strip(),
                "task_id": input("Enter task ID: ").strip()
            }
            if not all(label_data.values()):
                print("Kindly make a valid entry to proceed.")
                continue
            create_label(session, **label_data)
        elif choice == "10":
            read_labels(session)
        elif choice == "11":
            label_id = input("Enter label ID to update: ").strip()
            if not label_id:
                print("Kindly make a valid entry to proceed.")
                continue
            update_label(session, int(label_id))
        elif choice == "12":
            label_id = input("Enter label ID to delete: ").strip()
            if not label_id:
                print("Kindly make a valid entry to proceed.")
                continue
            delete_label(session, int(label_id))
        elif choice == "13":
            date_string = input("Enter date to validate (YYYY-MM-DD): ").strip()
            if validate_date(date_string):
                print("Date is valid.")
            else:
                print("Invalid date format or date is not valid.")
        elif choice == "14":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
