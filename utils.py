from datetime import datetime

def validate_date(date_string):
    """
    Validates if a date string is in the format YYYY-MM-DD and represents a valid date.
    Returns True if valid, False otherwise.
    """
    try:
        datetime.strptime(date_string, '%Y-%m-%d')
        return True
    except ValueError:
        return False

def get_yes_no_input(prompt):
    """
    Gets yes/no input from the user.
    Returns 'y' for yes, 'n' for no.
    """
    while True:
        choice = input(prompt).strip().lower()
        if choice in ['y', 'n']:
            return choice
        else:
            print("Please enter 'y' for yes or 'n' for no.")
