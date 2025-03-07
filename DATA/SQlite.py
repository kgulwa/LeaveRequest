import sqlite3

def recreate_employees_table():
    # Connect to the SQLite database
    connection = sqlite3.connect('leave_request.db')
    cursor = connection.cursor()

    # Drop the existing employees table if it exists
    cursor.execute('DROP TABLE IF EXISTS employees')

    # Recreate the employees table with an added password column
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS employees (
            id TEXT PRIMARY KEY,  -- Employee ID
            name TEXT NOT NULL,
            department TEXT NOT NULL,
            password TEXT NOT NULL  -- New column for storing hashed passwords
        )
    ''')

    connection.commit()

    # Verify the schema of the employees table
    cursor.execute("PRAGMA table_info(employees);")
    schema = cursor.fetchall()
    print("\nTable Schema for 'employees' table:")
    for column in schema:
        print(column)

    connection.close()
    print("Table 'employees' recreated successfully.")

def recreate_leave_requests_table():
    # Connect to the SQLite database
    connection = sqlite3.connect('leave_request.db')
    cursor = connection.cursor()

    # Drop the existing leave_requests table if it exists
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
            days_remaining INTEGER,
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

# Run both functions to recreate tables
if __name__ == "__main__":
    recreate_employees_table()
    recreate_leave_requests_table()
