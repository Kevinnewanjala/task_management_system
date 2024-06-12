from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from database.connection import Base

class Name(Base):
    __tablename__ = "names"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    role = Column(String)

    tasks = relationship("Task", back_populates="owner")

    def __init__(self, name, role):
        self.name = name
        self.role = role

def create_name(session, name, role):
    try:
        existing_name = session.query(Name).filter_by(name=name).first()
        if existing_name:
            print("Name with the same name already exists!")
            return
        
        name = Name(name=name, role=role)
        session.add(name)
        session.commit()
        print("Name created successfully!")
    except Exception as e:
        print("Error occurred while creating name:", e)

def read_names(session):
    try:
        names = session.query(Name).all()
        print("Names:")
        for name in names:
            print(f"ID: {name.id}, Name: {name.name}, Role: {name.role}")
    except Exception as e:
        print("Error occurred while reading names:", e)

def delete_name(session, name_id):
    try:
        name = session.query(Name).filter_by(id=name_id).first()
        if name:
            session.delete(name)
            session.commit()
            print("Name deleted successfully!")
        else:
            print("Name not found.")
    except Exception as e:
        print("Error occurred while deleting name:", e)

def get_yes_no_input(prompt):
    while True:
        choice = input(prompt).lower()
        if choice in ['y', 'n']:
            return choice
        else:
            print("Please make a selection!")

def update_name(session, name_id):
    try:
        name = session.query(Name).filter_by(id=name_id).first()
        if name:
            updated = False  # Flag to track if any updates were made
            update_name = get_yes_no_input("Update name? (y/n): ")
            if update_name == 'y':
                new_name = input("Enter new name: ")
                if new_name != name.name:
                    name.name = new_name
                    updated = True
            
            update_role = get_yes_no_input("Update role? (y/n): ")
            if update_role == 'y':
                new_role = input("Enter new role: ")
                if new_role != name.role:
                    name.role = new_role
                    updated = True
            
            if updated:
                session.commit()
                print("Name updated successfully!")
            else:
                print("No changes made.")
        else:
            print("Name not found!")
    except Exception as e:
        print("Error occurred while updating name:", e)
