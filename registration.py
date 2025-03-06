import string
import secrets
import sqlite3

# Leave entitlement dictionary
leave_entitlement = {
    "Annual Leave": 21,
    "Sick Leave": 30,
    "Maternity Leave": 120,
    "Family Responsibility Leave": 3,
}

# Function to get employee name
def employee_name():
    while True:
        name = input("Enter your full name: ").strip()
        if any(char.isdigit() for char in name):
            print("Name cannot contain any numerical values.")
        else:
            return name

# Function to get employee ID number
def employee_id_number():
    while True:
        id_number = input("Enter your ID number: ").strip()
        if not id_number.isdigit():
            print("ID number can only contain numerical values.")
        elif len(id_number) != 13:
            print("ID number must be exactly 13 digits. Please try again.")
        else:
            return id_number

# Function to generate Employee ID
def generate_employee_id(name, id_no):
    return f"{name[:3].upper()}{id_no[4:8]}"

# Function to generate a random password
def generate_password(length=12):
    alphabet = string.ascii_letters + string.digits
    return ''.join(secrets.choice(alphabet) for _ in range(length))

# Function to initialize employee leave balance
def register_leave_balance(employee_id):
    connection = sqlite3.connect('leave_request.db')
    cursor = connection.cursor()

    for leave_type, days in leave_entitlement.items():
        cursor.execute('''INSERT INTO leave_requests (employee_id, leave_type, days_remaining)
                          VALUES (?, ?, ?)''', (employee_id, leave_type, days))

    connection.commit()
    connection.close()
    print(f"Leave balance initialized for {employee_id}.")

# Function to register an employee in the database
def register_employee(employee_id, name, department):
    connection = sqlite3.connect('leave_request.db')
    cursor = connection.cursor()

    # Check if employee already exists by their employee_id
    cursor.execute('''SELECT * FROM employees WHERE id = ?''', (employee_id,))
    existing_employee = cursor.fetchone()

    if existing_employee:
        print(f"Employee with ID {employee_id} already exists. Please log in.")
        connection.close()
        return

    try:
        # Insert new employee if they do not already exist
        cursor.execute('''INSERT INTO employees (id, name, department) 
                          VALUES (?, ?, ?)''', (employee_id, name, department))
        
        connection.commit()
        print(f"Employee {employee_id} registered successfully.")

    except sqlite3.Error as e:
        print(f"An error occurred while registering the employee: {e}")

    finally:
        connection.close()

# Main execution function
def main():
    print("Good Day!! Welcome to Employee Registration.")
    name = employee_name()
    id_number = employee_id_number()
    employee_id = generate_employee_id(name, id_number)
    department = input("Enter your department: ").strip()
    
    password = generate_password()
    
    print(f"\nYour auto-generated Employee ID is {employee_id}")
    print("*Remember this ID for future references.*")
    print(f"Your auto-generated password is: {password}")
    print("*Keep it safe and DO NOT share with anyone.*")

    # Register the employee and their leave balance
    register_employee(employee_id, name, department)
    register_leave_balance(employee_id)

# Run the main function
if __name__ == "__main__":
    main()
