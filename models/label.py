from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database.connection import Base

class Label(Base):
    __tablename__ = "labels"

    id = Column(Integer, primary_key=True, index=True)  # Primary key for the Label table
    name = Column(String, unique=True, index=True)  # Name of the label, unique constraint
    task_id = Column(Integer, ForeignKey("tasks.id", ondelete="CASCADE"), nullable=False)  # ForeignKey to tasks table

    task = relationship("Task", back_populates="labels")  # Relationship with Task table

    def __init__(self, name, task_id):
        self.name = name
        self.task_id = task_id

def create_label(session, name, task_id):
    try:
        existing_label = session.query(Label).filter_by(name=name).first()  # Check if label with same name exists
        if existing_label:
            print("Label with the same name already exists.")
            return
        
        label = Label(name=name, task_id=task_id)  # Create new Label object
        session.add(label)  # Add Label to session
        session.commit()  # Commit transaction to database
        print("Label created successfully.")
    except Exception as e:
        print("Error occurred while creating label:", e)

def read_labels(session):
    try:
        labels = session.query(Label).all()  # Query all labels from database
        print("Labels:")
        for label in labels:
            label_data = {
                "id": label.id,
                "name": label.name,
                "task_id": label.task_id
            }
            print(f"Label Data: {label_data}")  # Print label data in dictionary format
    except Exception as e:
        print("Error occurred while reading labels:", e)

def delete_label(session, label_id):
    try:
        label = session.query(Label).filter_by(id=label_id).first()  # Query label by id
        if label:
            session.delete(label)  # Delete label from session
            session.commit()  # Commit transaction to database
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
        label = session.query(Label).filter_by(id=label_id).first()  # Query label by id
        if label:
            changes_made = False

            update_name = get_yes_no_input("Update label name? (y/n): ")
            if update_name == 'y':
                new_name = input("Enter new name: ")
                label.name = new_name  # Update label name
                changes_made = True
            
            update_task_id = get_yes_no_input("Update task ID? (y/n): ")
            if update_task_id == 'y':
                new_task_id = int(input("Enter new task ID: "))
                label.task_id = new_task_id  # Update task ID
                changes_made = True
            
            if changes_made:
                session.commit()  # Commit transaction to database if changes were made
                print("Label updated successfully.")
            else:
                print("No changes made.")
        else:
            print("Label not found.")
    except Exception as e:
        print("Error occurred while updating label:", e)
