import sqlite3

def create_database():
    connection = sqlite3.connect('leave_request.db')
    cursor = connection.cursor()

    # Create employees table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS employees(
        id INTEGER PRIMARY KEY,
        name TEXT, 
        department TEXT 
    )''')

    # Create leave_requests table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS leave_requests(
        id INTEGER PRIMARY KEY,
        employee_id INTEGER,
        leave_type TEXT,
        days_requested INTEGER,
        start_date TEXT,
        end_date TEXT,
        FOREIGN KEY(employee_id) REFERENCES employees(id)
    )''')

    connection.commit()
    connection.close()

create_database()
