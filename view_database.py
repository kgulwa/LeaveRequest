import sqlite3

def view_table(table_name):
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


if __name__ = "__main__":
    print("Available tables: employees, leave_requests")
    table_name = input("Enter the table name to view data: ").strip()
    view_table_data(table_name)