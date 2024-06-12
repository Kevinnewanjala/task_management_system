
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database.connection import Base

class Label(Base):
    __tablename__ = "labels"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    task_id = Column(Integer, ForeignKey("tasks.id", ondelete="CASCADE"), nullable=False)

    task = relationship("Task", back_populates="labels")

    def __init__(self, name, task_id):
        self.name = name
        self.task_id = task_id

def create_label(session, name, task_id):
    try:
        existing_label = session.query(Label).filter_by(name=name).first()
        if existing_label:
            print("Label with the same name already exists.")
            return
        
        label = Label(name=name, task_id=task_id)
        session.add(label)
        session.commit()
        print("Label created successfully.")
    except Exception as e:
        print("Error occurred while creating label:", e)

def read_labels(session):
    try:
        labels = session.query(Label).all()
        print("Labels:")
        for label in labels:
            print(f"ID: {label.id}, Name: {label.name}, Task ID: {label.task_id}")
    except Exception as e:
        print("Error occurred while reading labels:", e)

def delete_label(session, label_id):
    try:
        label = session.query(Label).filter_by(id=label_id).first()
        if label:
            session.delete(label)
            session.commit()
            print("Label deleted successfully.")
        else:
            print("Label not found.")
    except Exception as e:
        print("Error occurred while deleting label:", e)

def get_yes_no_input(prompt):
    while True:
        choice = input(prompt).lower()
        if choice in ['y', 'n']:
            return choice
        else:
            print("Please make a selection!")

def update_label(session, label_id):
    try:
        label = session.query(Label).filter_by(id=label_id).first()
        if label:
            changes_made = False

            update_name = get_yes_no_input("Update label name? (y/n): ")
            if update_name == 'y':
                new_name = input("Enter new name: ")
                label.name = new_name
                changes_made = True
            
            update_task_id = get_yes_no_input("Update task ID? (y/n): ")
            if update_task_id == 'y':
                new_task_id = int(input("Enter new task ID: "))
                label.task_id = new_task_id
                changes_made = True
            
            if changes_made:
                session.commit()
                print("Label updated successfully.")
            else:
                print("No changes made.")
        else:
            print("Label not found.")
    except Exception as e:
        print("Error occurred while updating label:", e)
