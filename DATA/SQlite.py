import sqlite3

def list_contents():
    # Connect to the SQLite database
    connection = sqlite3.connect('leave_request.db')
    cursor = connection.cursor()

    # List contents of the employees table
    print("Contents of the 'employees' table:")
    cursor.execute('SELECT * FROM employees')
    employees = cursor.fetchall()
    if employees:
        for row in employees:
            print(row)
    else:
        print("No records found in 'employees' table.")

    # List contents of the leave_requests table
    print("\nContents of the 'leave_requests' table:")
    cursor.execute('SELECT * FROM leave_requests')
    leave_requests = cursor.fetchall()
    if leave_requests:
        for row in leave_requests:
            print(row)
    else:
        print("No records found in 'leave_requests' table.")

    # Close the connection
    connection.close()

# Run the function to list the contents
if __name__ == "__main__":
    list_contents()
