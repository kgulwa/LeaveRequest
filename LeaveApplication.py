import os
import sqlite3
import registration
import datetime
import string
import secrets
from googleapiclient.discovery import build
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
client_id = os.getenv("GOOGLE_CLIENT_ID")
client_secret = os.getenv("GOOGLE_CLIENT_SECRET")
SCOPES = ["https://www.googleapis.com/auth/calendar"]

# Leave entitlements
leave_entitlement = {
    "Annual Leave": 21,
    "Sick Leave": 30,
    "Maternity Leave": 120,
    "Family Responsibility Leave": 3,
}

# Employee Data Storage
employee_list = []
employee_passwords = {}
employee_leave_balance = {}

# Database Setup
def create_database():
    connection = sqlite3.connect('leave_request.db')
    cursor = connection.cursor()

    cursor.execute(''' CREATE TABLE IF NOT EXISTS employees(
        id TEXT PRIMARY KEY,
        name TEXT,
        department TEXT
    )''')

    cursor.execute(''' CREATE TABLE IF NOT EXISTS leave_requests(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        employee_id TEXT,
        leave_type TEXT,
        days_requested INTEGER,
        start_date TEXT,
        end_date TEXT,
        FOREIGN KEY(employee_id) REFERENCES employees(id)
    )''')

    connection.commit()
    connection.close()

# Google Calendar Authentication
def authenticate_google_calendar():
    creds = None
    if os.path.exists("token.json"):
        creds = Credentials.from_authorized_user_file("token.json")
    
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            client_config = {
                "installed": {
                    "client_id": client_id,
                    "client_secret": client_secret,
                    "redirect_uris": ["http://localhost"],
                    "auth_uri": "https://accounts.google.com/o/oauth2/auth",
                    "token_uri": "https://oauth2.googleapis.com/token",
                }
            }
            flow = InstalledAppFlow.from_client_config(client_config, SCOPES)
            creds = flow.run_local_server(port=0)

        with open("token.json", "w") as token:
            token.write(creds.to_json())

    try:
        return build("calendar", "v3", credentials=creds)
    except Exception as error:
        print("Google Calendar authentication failed:", error)
        return None

# Employee Registration
def register_employee(employee_id, name, department):
    connection = sqlite3.connect('leave_request.db')
    cursor = connection.cursor()

    cursor.execute('''INSERT INTO employees(id, name, department) VALUES (?, ?, ?)''', (employee_id, name, department))
    connection.commit()
    connection.close()

    employee_list.append(employee_id)
    employee_leave_balance[employee_id] = leave_entitlement.copy()
    print(f"Employee {name} registered successfully!")

# Leave Application
def apply_leave(employee_id, leave_type, days_requested, start_date, end_date):
    if employee_id not in employee_list:
        print("Error: Employee not found. Please register first.")
        return

    if leave_type not in leave_entitlement:
        print("Error: Invalid leave type.")
        return

    if days_requested <= 0:
        print("Error: Number of days must be greater than zero.")
        return

    if employee_leave_balance[employee_id][leave_type] < days_requested:
        print("Error: Insufficient leave balance.")
        return
    
    employee_leave_balance[employee_id][leave_type] -= days_requested
    print(f"Leave approved! {employee_id} has {employee_leave_balance[employee_id][leave_type]} days left for {leave_type}.")
    
    connection = sqlite3.connect('leave_request.db')
    cursor = connection.cursor()
    cursor.execute('''INSERT INTO leave_requests(employee_id, leave_type, days_requested, start_date, end_date) VALUES (?, ?, ?, ?, ?)''',
                   (employee_id, leave_type, days_requested, start_date, end_date))
    connection.commit()
    connection.close()
    
    service = authenticate_google_calendar()
    if service:
        create_leave_event(service, employee_id, leave_type, start_date, end_date)

# Create Google Calendar Event
def create_leave_event(service, employee_name, leave_type, start_date, end_date):
    event = {
        "summary": f"{employee_name} - {leave_type}",
        "start": {"dateTime": start_date, "timeZone": "UTC"},
        "end": {"dateTime": end_date, "timeZone": "UTC"},
    }
    try:
        event_result = service.events().insert(calendarId="primary", body=event).execute()
        print(f"Leave event created: {event_result['summary']} from {event_result['start']['dateTime']} to {event_result['end']['dateTime']}")
    except Exception as e:
        print("Failed to create event:", e)

# Check Leave Balance
def check_leave_balance(employee_id):
    if employee_id not in employee_list:
        print("Error: Employee not found.")
        return
    print(f"\nLeave balance for {employee_id}:")
    for leave_type, days_left in employee_leave_balance[employee_id].items():
        print(f"{leave_type}: {days_left} days remaining.")

# Get Leave History
def get_leave_history(employee_id):
    connection = sqlite3.connect('leave_request.db')
    cursor = connection.cursor()
    cursor.execute('''SELECT leave_type, days_requested, start_date, end_date FROM leave_requests WHERE employee_id = ?''', (employee_id,))
    rows = cursor.fetchall()
    connection.close()
    
    if not rows:
        print("No leave history found.")
    else:
        for row in rows:
            print(f"Leave Type: {row[0]}, Days: {row[1]}, Start: {row[2]}, End: {row[3]}")

if __name__ == "__main__":
    create_database()
    empl_id = input("Enter your Employee ID: ").strip()
    leave_type = input("Enter leave type: ").strip()
    days = int(input("Enter number of days: ").strip())
    start_date = input("Enter leave start date (YYYY-MM-DD): ").strip() + "T09:00:00"
    end_date = input("Enter leave end date (YYYY-MM-DD): ").strip() + "T17:00:00"

    apply_leave(empl_id, leave_type, days, start_date, end_date)
    check_leave_balance(empl_id)
