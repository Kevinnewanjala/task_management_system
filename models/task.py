from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship
from database.connection import Base
from datetime import datetime, timedelta

class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String)
    created_date = Column(Date, default=datetime.now().date())
    due_date = Column(Date)
    priority = Column(String)

    name_id = Column(Integer, ForeignKey("names.id"))
    owner = relationship("Name", back_populates="tasks")
    labels = relationship("Label", back_populates="task", cascade="all, delete-orphan")

    @staticmethod
    def calculate_priority(due_date):
        today = datetime.now().date()
        if due_date <= today + timedelta(days=7):
            return "Urgent"
        elif due_date <= today + timedelta(days=14):
            return "Quite Urgent"
        else:
            return "Not Urgent"

def create_task(session, title, description, due_date, name_id):
    try:
        priority = Task.calculate_priority(due_date)
        task = Task(title=title, description=description, due_date=due_date, priority=priority, name_id=name_id)
        session.add(task)
        session.commit()
        print("Task created successfully.")
    except Exception as e:
        print("Error occurred while creating task:", e)

def read_tasks(session):
    try:
        tasks = session.query(Task).all()
        print("Tasks:")
        for task in tasks:
            print(f"ID: {task.id}, Title: {task.title}, Description: {task.description}, Due Date: {task.due_date}, Created Date: {task.created_date}, Priority: {task.priority}, Name ID: {task.name_id}")
    except Exception as e:
        print("Error occurred while reading tasks:", e)

def delete_task(session, task_id):
    try:
        task = session.query(Task).filter_by(id=task_id).first()
        if task:
            session.delete(task)
            session.commit()
            print("Task deleted successfully.")
        else:
            print("Task not found.")
    except Exception as e:
        print("Error occurred while deleting task:", e)

def get_yes_no_input(prompt):
    while True:
        choice = input(prompt).lower()
        if choice in ['y', 'n']:
            return choice
        else:
            print("Please make a choice!")

def update_task(session, task_id):
    try:
        task = session.query(Task).filter_by(id=task_id).first()
        if task:
            changes_made = False

            update_title = get_yes_no_input("Update title? (y/n): ")
            if update_title == 'y':
                new_title = input("Enter new title: ")
                task.title = new_title
                changes_made = True
            
            update_description = get_yes_no_input("Update description? (y/n): ")
            if update_description == 'y':
                new_description = input("Enter new description: ")
                task.description = new_description
                changes_made = True
            
            update_due_date = get_yes_no_input("Update due date? (y/n): ")
            if update_due_date == 'y':
                new_due_date = input("Enter new due date (YYYY-MM-DD): ")
                try:
                    new_due_date = datetime.strptime(new_due_date, '%Y-%m-%d').date()
                    if new_due_date < datetime.now().date():
                        print("Due date must be a future date.")
                    else:
                        task.due_date = new_due_date
                        task.priority = Task.calculate_priority(new_due_date)
                        changes_made = True
                except ValueError:
                    print("Invalid date format. Please enter the due date in YYYY-MM-DD format.")
            
            update_name_id = get_yes_no_input("Update name ID? (y/n): ")
            if update_name_id == 'y':
                new_name_id = int(input("Enter new name ID: "))
                task.name_id = new_name_id
                changes_made = True
            
            if changes_made:
                session.commit()
                print("Task updated successfully.")
            else:
                print("No changes made.")
        else:
            print("Task not found.")
    except Exception as e:
        print("Error occurred while updating task:", e)
