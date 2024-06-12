
from models.name import create_name, delete_name, update_name, read_names
from models.task import create_task, delete_task, update_task, read_tasks
from models.label import create_label, delete_label, update_label, read_labels
from database.connection import create_db_session
from datetime import datetime

def main():
    session = create_db_session()
    
    while True:
        print("\nMenu:")
        print("1. Create Name")
        print("2. Read Names")
        print("3. Update Name")
        print("4. Delete Name")
        print("5. Create Task")
        print("6. Read Tasks")
        print("7. Update Task")
        print("8. Delete Task")
        print("9. Create Label")
        print("10. Read Labels")
        print("11. Update Label")
        print("12. Delete Label")
        print("13. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            name = input("Enter name: ").strip()
            role = input("Enter role: ").strip()
            if not name or not role:
                print("Kindly make a valid entry to proceed.")
                continue
            create_name(session, name, role)
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
            title = input("Enter task title: ").strip()
            description = input("Enter task description: ").strip()
            due_date = input("Enter due date (YYYY-MM-DD): ").strip()
            name_id = input("Enter name ID: ").strip()
            if not title or not description or not due_date or not name_id:
                print("Kindly make a valid entry to proceed.")
                continue
            try:
                due_date = datetime.strptime(due_date, '%Y-%m-%d').date()
                if due_date < datetime.now().date():
                    print("Due date must be a future date.")
                else:
                    create_task(session, title, description, due_date, int(name_id))
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
            name = input("Enter label name: ").strip()
            task_id = input("Enter task ID: ").strip()
            if not name or not task_id:
                print("Kindly make a valid entry to proceed.")
                continue
            create_label(session, name, int(task_id))
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
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
