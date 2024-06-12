## Task Management System

### Introduction

The Task Management System is a command-line application that enables users to manage tasks, names, and labels using a relational database. Built with Python and SQLAlchemy, it provides a straightforward interface for performing CRUD operations on tasks, names, and labels while maintaining database integrity through cascading deletions.

# Features
Task Management: Add, view, update, and delete tasks.
Name Management: Add, view, update, and delete names associated with tasks.
Label Management: Add, view, update, and delete labels associated with tasks.
Automatic Priority Calculation: Prioritize tasks based on their due dates.
Database Integrity: Maintain database integrity using cascading deletions for tasks and labels.

## Prerequisites
Python 3.7 or higher
SQLAlchemy
SQLite (default database)

## Project Structure

├── app.py
├── models
│   ├── __init__.py
│   ├── name.py
│   ├── task.py
│   └── label.py
├── database
│   ├── __init__.py
│   └── connection.py
└── README.md

# Installation

1. Clone the repository
bash
Copy code
git clone https://github.com/yourusername/task-management-system.git
cd task-management-system
2. Create and activate a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
3. Install the required packages
pip install -r requirements.txt
4. Set up the database
python -c "from database.connection import Base, engine; Base.metadata.create_all(engine)"
Usage
Run the main application:
python app.py


## Code Overview

### app.py
The entry point of the application.
Contains the main menu loop for interacting with tasks, names, and labels.
Handles user input and directs it to the appropriate CRUD operations.
models/name.py
Defines the Name model with attributes: id, name, and role.
Relationships: A Name can have many tasks.
Functions:
create_name: Adds a new name to the database.
read_names: Retrieves and displays all names.
update_name: Updates an existing name based on user input.
delete_name: Deletes a name and all associated tasks.


### models/task.py
Defines the Task model with attributes: id, title, description, created_date, due_date, and priority.
Relationships: A Task is associated with a Name and can have many labels.
Functions:
create_task: Adds a new task with automatic priority calculation.
read_tasks: Retrieves and displays all tasks.
update_task: Updates an existing task based on user input.
delete_task: Deletes a task and all associated labels.
calculate_priority: Determines task priority based on the due date.

### models/label.py
Defines the Label model with attributes: id, name, and task_id.
Relationships: A Label is associated with a Task.
Functions:
create_label: Adds a new label to a task.
read_labels: Retrieves and displays all labels.
update_label: Updates an existing label based on user input.
delete_label: Deletes a label.


### database/connection.py
Sets up the database connection using SQLAlchemy.
Defines the Base class for model definitions.
Configures the database engine and session maker.
Provides a function to create a new database session.
Contributions
Contributions are welcome! Feel free to open issues or submit pull requests.

# License

MIT License

Copyright (c) 2024 Kevin Wanjala

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
