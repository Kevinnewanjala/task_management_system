from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship
from database.connection import Base
from datetime import datetime, timedelta

# Define the Task class, representing the tasks table in the database
class Task(Base):
    __tablename__ = "tasks"

    # Columns in the tasks table
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String)
    created_date = Column(Date, default=datetime.now().date())
    due_date = Column(Date)
    priority = Column(String)

    # Foreign key relationship to the names table
    name_id = Column(Integer, ForeignKey("names.id"))
    owner = relationship("Name", back_populates="tasks")  # Relationship to Name class
    labels = relationship("Label", back_populates="task", cascade="all, delete-orphan")  # Relationship to Label class

    # Constructor to initialize a Task object
    def __init__(self, title, description, due_date, name_id):
        self.title = title
        self.description = description
        self.due_date = due_date
        self.name_id = name_id
        self.priority = Task.calculate_priority(due_date)  # Calculate priority based on due_date

    # Static method to calculate task priority based on due_date
    @staticmethod
    def calculate_priority(due_date):
        today = datetime.now().date()
        if due_date <= today + timedelta(days=7):
            return "Urgent"
        elif due_date <= today + timedelta(days=14):
            return "Quite Urgent"
        else:
            return "Not Urgent"

# Function to create a new task in the database
def create_task(session, title, description, due_date, name_id):
    try:
        task = Task(title=title, description=description, due_date=due_date, name_id=name_id)  # Using a dictionary to pass task details
        session.add(task)
        session.commit()
        print("Task created successfully.")
    except Exception as e:
        print("Error occurred while creating task:", e)

# Function to read and display all tasks from the database
def read_tasks(session):
    try:
        tasks = session.query(Task).all()  # Querying all tasks from the database
        print("Tasks:")
        for task in tasks:
            # Creating a dictionary to format and display task information
            task_data = {
                "id": task.id,
                "title": task.title,
                "description": task.description,
                "due_date": task.due_date,
                "created_date": task.created_date,
                "priority": task.priority,
                "name_id": task.name_id
            }
            print(f"Task Data: {task_data}")
    except Exception as e:
        print("Error occurred while reading tasks:", e)

# Function to delete a task from the database
def delete_task(session, task_id):
    try:
        task = session.query(Task).filter_by(id=task_id).first()  # Querying the task by ID
        if task:
            session.delete(task)  # Deleting the task from the session
            session.commit()
            print("Task deleted successfully.")
        else:
            print("Task not found.")
    except Exception as e:
        print("Error occurred while deleting task:", e)

# Function to prompt user for yes/no input and validate the choice
def get_yes_no_input(prompt):
    while True:
        choice = input(prompt).lower()
        if choice in ['y', 'n']:  # Using a list to validate yes/no input
            return choice
        else:
            print("Please make a choice!")

# Function to update an existing task in the database
def update_task(session, task_id):
    try:
        task = session.query(Task).filter_by(id=task_id).first()  # Querying the task by ID
        if task:
            changes_made = False

            update_title = get_yes_no_input("Update title? (y/n): ")
            if update_title == 'y':
                new_title = input("Enter new title: ")
                task.title = new_title  # Updating task title
                changes_made = True
            
            update_description = get_yes_no_input("Update description? (y/n): ")
            if update_description == 'y':
                new_description = input("Enter new description: ")
                task.description = new_description  # Updating task description
                changes_made = True
            
            update_due_date = get_yes_no_input("Update due date? (y/n): ")
            if update_due_date == 'y':
                new_due_date = input("Enter new due date (YYYY-MM-DD): ")
                try:
                    new_due_date = datetime.strptime(new_due_date, '%Y-%m-%d').date()
                    if new_due_date < datetime.now().date():
                        print("Due date must be a future date.")
                    else:
                        task.due_date = new_due_date  # Updating task due_date
                        task.priority = Task.calculate_priority(new_due_date)  # Updating task priority
                        changes_made = True
                except ValueError:
                    print("Invalid date format. Please enter the due date in YYYY-MM-DD format.")
            
            update_name_id = get_yes_no_input("Update name ID? (y/n): ")
            if update_name_id == 'y':
                new_name_id = int(input("Enter new name ID: "))
                task.name_id = new_name_id  # Updating task name_id
                changes_made = True
            
            if changes_made:
                session.commit()  # Committing changes to the database
                print("Task updated successfully.")
            else:
                print("No changes made.")
        else:
            print("Task not found.")
    except Exception as e:
        print("Error occurred while updating task:", e)
