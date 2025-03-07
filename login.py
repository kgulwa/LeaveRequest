import sqlite3

def login_employee():
    print("\n--- Employee Login ---")
    
    while True:
        employee_id = input("Enter your Employee ID: ").strip()
        password = input("Enter your Password: ").strip()

        # Connect to the database
        connection = sqlite3.connect('leave_request.db')
        cursor = connection.cursor()

        # Check if employee exists
        cursor.execute('SELECT name FROM employees WHERE id = ? AND password = ?', (employee_id, password))
        employee = cursor.fetchone()

        connection.close()

        if employee:
            print(f"\nWelcome back, {employee[0]}! What would you like to do today?")
            return True  # Successful login
        else:
            print("\n❌ Invalid Employee ID or Password. Please try again.")
            retry = input("Do you want to try again? (yes/no): ").strip().lower()
            if retry != "yes":
                print("\nYou can register as a new user if you do not have an account.")
                return False  # Exit if the user doesn't want to retry
