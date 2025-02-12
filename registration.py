import string
import secrets

# Global Variables
employee_list = []  # List of registered employees
employee_passwords = {}  # Stores Employee IDs and passwords.
employee_leave_balance = {}  # Stores Employee leave balances

# Leave entitlement dictionary
leave_entitlement = {
    "Annual Leave": 21,
    "Sick Leave": 30,
    "Maternity Leave": 120,
    "Family Responsibility Leave": 3,
}

# Function Definitions
def employee_name():
    while True:
        name = input("Enter your full name: ")
        if any(char.isdigit() for char in name):
            print("Name cannot contain any numerical values.")
        else:
            return name

def employee_id_number():
    while True:
        employee_id_number = input("Enter your ID number: ")

        if not employee_id_number.isdigit():
            print("ID number can only be numerical values.")
        elif len(employee_id_number) != 13:
            print("ID number must be exactly 13 digits. Please try again.")
        else:
            return employee_id_number

def generate_employee_id(name, id_no):
    return f"{name[:3].upper()}{id_no[4:8]}"

def existing_employee(employee_id):
    if employee_id not in employee_list:
        print("This is not a valid Employee ID. Double-check and try again.")
        return False
    return True

def generate_password(length=12):
    alphabet = string.ascii_letters + string.digits
    return ''.join(secrets.choice(alphabet) for _ in range(length))

def forgot_password(employee_id):
    if employee_id not in employee_passwords:
        print("Invalid Employee ID. Please check and try again.")
        return

    print(f"Password reset requested for Employee ID: {employee_id}")
    temp_password = generate_password(8)
    employee_passwords[employee_id] = temp_password
    print(f"Your temporary password is: {temp_password}. Please log in and reset your password.")

# Function to register employee leave balance
def register_leave_balance(employee_id):
    if employee_id not in employee_leave_balance:
        employee_leave_balance[employee_id] = leave_entitlement.copy()
        print(f"Leave balance initialized for {employee_id}.")


def register_employee(employee_id, nam, department):
    connection = sqlite3.connect('leave_request.db')
    cursor = connection.cursor()

    cursor.execute(''' INSERT INTO employees(id, name, department)
    VALUES(?,?,?)''',(employee_id, name< department))

    connection.commit()
    connection.close()