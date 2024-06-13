from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from database.connection import Base

# Define the Name class, representing the names table in the database
class Name(Base):
    __tablename__ = "names"

    # Columns in the names table
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    role = Column(String)

    # Relationship to the Task class (one-to-many)
    tasks = relationship("Task", back_populates="owner")

    # Constructor to initialize a Name object
    def __init__(self, name, role):
        self.name = name
        self.role = role

# Function to create a new name in the database
def create_name(session, name, role):
    try:
        existing_name = session.query(Name).filter_by(name=name).first()
        if existing_name:
            print("Name with the same name already exists!")
            return
        
        new_name = Name(name=name, role=role)  # Using a dictionary to pass name details
        session.add(new_name)
        session.commit()
        print("Name created successfully!")
    except Exception as e:
        print("Error occurred while creating name:", e)

# Function to read and display all names from the database
def read_names(session):
    try:
        names = session.query(Name).all()  # Querying all names from the database
        print("Names:")
        for name in names:
            # Creating a dictionary to format and display name information
            name_data = {
                "id": name.id,
                "name": name.name,
                "role": name.role
            }
            print(f"Name Data: {name_data}")
    except Exception as e:
        print("Error occurred while reading names:", e)

# Function to delete a name from the database
def delete_name(session, name_id):
    try:
        name = session.query(Name).filter_by(id=name_id).first()  # Querying the name by ID
        if name:
            session.delete(name)  # Deleting the name from the session
            session.commit()
            print("Name deleted successfully!")
        else:
            print("Name not found.")
    except Exception as e:
        print("Error occurred while deleting name:", e)

# Function to prompt user for yes/no input and validate the choice
def get_yes_no_input(prompt):
    while True:
        choice = input(prompt).lower()
        if choice in ['y', 'n']:  # Using a list to validate yes/no input
            return choice
        else:
            print("Please make a selection!")

# Function to update an existing name in the database
def update_name(session, name_id):
    try:
        name = session.query(Name).filter_by(id=name_id).first()  # Querying the name by ID
        if name:
            updated = False  # Flag to track if any updates were made

            update_name = get_yes_no_input("Update name? (y/n): ")
            if update_name == 'y':
                new_name = input("Enter new name: ")
                if new_name != name.name:
                    name.name = new_name  # Updating name
                    updated = True
            
            update_role = get_yes_no_input("Update role? (y/n): ")
            if update_role == 'y':
                new_role = input("Enter new role: ")
                if new_role != name.role:
                    name.role = new_role  # Updating role
                    updated = True
            
            if updated:
                session.commit()  # Committing changes to the database
                print("Name updated successfully!")
            else:
                print("No changes made.")
        else:
            print("Name not found!")
    except Exception as e:
        print("Error occurred while updating name:", e)
