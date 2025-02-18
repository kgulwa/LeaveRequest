import sqlite3

def list_tables():
    """Fetch and display all table names in the database."""
    connection = sqlite3.connect('leave_request.db')
    cursor = connection.cursor()

    try:
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = cursor.fetchall()
        
        if not tables:
            print("No tables found in the database.")
            return []
        
        print("\nAvailable tables:")
        table_names = [table[0] for table in tables]
        for name in table_names:
            print(f"- {name}")
        
        return table_names

    except sqlite3.Error as e:
        print(f"An error occurred: {e}")
        return []
    finally:
        connection.close()

def view_table_data(table_name):
    """Fetch and display data from a specific table."""
    connection = sqlite3.connect('leave_request.db')
    cursor = connection.cursor()

    try:
        cursor.execute(f"SELECT * FROM {table_name};")  # Ensure proper SQL syntax
        rows = cursor.fetchall()

        if not rows:
            print(f"\nNo data found in '{table_name}'.")
        else:
            print(f"\nData from '{table_name}':")
            
            # Fetch column names
            cursor.execute(f"PRAGMA table_info({table_name});")
            columns = [column[1] for column in cursor.fetchall()]
            print(" | ".join(columns))  # Print column headers
            print("-" * 50)
            
            for row in rows:
                print(" | ".join(map(str, row)))

    except sqlite3.Error as e:
        print(f"An error occurred: {e}")
    finally:
        connection.close()

if __name__ == "__main__":
    tables = list_tables()
    if tables:
        table_name = input("\nEnter the table name you want to view: ").strip()
        if table_name in tables:
            view_table_data(table_name)
        else:
            print("Invalid table name. Please choose from the available tables.")
