import sqlite3

def recreate_table():
    # Connect to the SQLite database
    connection = sqlite3.connect('leave_request.db')
    cursor = connection.cursor()

    # Drop the existing table if it exists
    cursor.execute('DROP TABLE IF EXISTS leave_requests')

    # Recreate the table with the correct schema
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS leave_requests (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            employee_id TEXT,
            leave_type TEXT,
            days_requested INTEGER,
            start_date TEXT,
            end_date TEXT,
            days_remaining INTEGER,  -- Adding the 'days_remaining' column
            FOREIGN KEY(employee_id) REFERENCES employees(id)
        )
    ''')

    connection.commit()

    # Verify the schema of the leave_requests table
    cursor.execute("PRAGMA table_info(leave_requests);")
    schema = cursor.fetchall()
    print("\nTable Schema for 'leave_requests' table:")
    for column in schema:
        print(column)

    connection.close()
    print("Table 'leave_requests' recreated successfully.")

def list_contents():
    # Connect to the SQLite database
    connection = sqlite3.connect('leave_request.db')
    cursor = connection.cursor()

    # List contents of the employees table
    print("\nContents of the 'employees' table:")
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

# Run the function to recreate the table and then list the contents
if __name__ == "__main__":
    recreate_table()  # Recreate the leave_requests table
    list_contents()  # Then list the contents
