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


def view_table(table_name):
    #Fetch and display data from a specific table

    connection = sqlite3.connect('leave_request.db')
    cursor = connection.cursor


    try:
        cursor.execute(f"SELECT * FROM {table_name}")
        rows = cursoe.fetchall()

        if not rows:
            print(f"\nNo data found in table '{table_name}' .")

        else:
            print(f"\nData from '{table_name}': ")
            for row in rows:
                print(row)


    except sqlite3.Error as e:
        print(f"An error occured: {e}")

    finally:
        connection.close()


if __name__ == "__main__":
    tables = list_tables()

    if tables:
        table_name = input("\nEnter the table name you want to view: ").strip()
        if table_name in tables:
            view_table(table_name)
        else:
            print("Invalid table name. Please choose from the available tables list.")