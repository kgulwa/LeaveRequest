import registration
import datetime
from googleapiclient.discovery import build
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from dotenv import load_dotenv
import os

# Load environment variables from the .env file
load_dotenv()

# Fetch credentials from environment variables
client_id = os.getenv("GOOGLE_CLIENT_ID")
client_secret = os.getenv("GOOGLE_CLIENT_SECRET")
SCOPES = ["https://www.googleapis.com/auth/calendar"]

# Corrected list of valid leaves
valid_leave = ["Sick Leave", "Family Responsibility Leave", "Maternity Leave", "Paternity Leave", "Annual Leave"]

def authenticate_google_calendar():
    """Authenticate and return Google Calendar API service."""
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
        service = build("calendar", "v3", credentials=creds)
        return service
    except Exception as error:
        print("An error occurred while authenticating:", error)
        return None


def leave_application(employee_id, leave_type, days_requested, start_date, end_date):
    # Check if employee exists
    if employee_id not in registration.employee_leave_balance:
        print("Error: Employee not found. Please register first.")
        return

    # Keep prompting the user until a valid leave type is entered
    while leave_type not in valid_leave:
        print("Error: Invalid leave type. Please choose from the following options:")
        for leave in valid_leave:
            print(f"- {leave}")
        leave_type = input("Enter a valid leave type: ").strip()

    # Check if requested days are valid
    while True:
        if days_requested <= 0:
            print("Error: Number of days must be greater than zero.")
            days_requested = int(input("Enter the number of days again: "))
        else:
            break

    # Ensure the employee has a leave record for this leave type
    if leave_type not in registration.employee_leave_balance[employee_id]:
        print(f"Error: No leave record found for {leave_type}.")
        return

    # Check if employee has enough leave balance
    if registration.employee_leave_balance[employee_id][leave_type] >= days_requested:
        registration.employee_leave_balance[employee_id][leave_type] -= days_requested
        print(f"Leave approved! {employee_id} now has {registration.employee_leave_balance[employee_id][leave_type]} days left for {leave_type}.")

        # Create leave event in Google Calendar
        service = authenticate_google_calendar()
        if service:
            create_leave_event(service, employee_id, leave_type, start_date, end_date)
    else:
        print(f"Error: Insufficient leave balance. {employee_id} has only {registration.employee_leave_balance[employee_id][leave_type]} days left.")


def create_leave_event(service, employee_name, leave_type, start_date, end_date):
    event = {
        "summary": f"{employee_name} - {leave_type}",
        "start": {
            "dateTime": start_date,
            "timeZone": "UTC",
        },
        "end": {
            "dateTime": end_date,
            "timeZone": "UTC",
        },
    }

    try:
        # Creating the event in Google Calendar
        event_result = service.events().insert(calendarId="primary", body=event).execute()
        print(f"Leave event created: {event_result['summary']} from {event_result['start']['dateTime']} to {event_result['end']['dateTime']}")
    except Exception as e:
        print(f"An error occurred while creating the leave event: {e}")


def check_leave_balance(employee_id):
    if employee_id not in registration.employee_leave_balance:
        print("Error: Employee not found in the system. Please register first.")
        return

    print(f"\nLeave balance for {employee_id}:")
    for leave_type, days_left in registration.employee_leave_balance[employee_id].items():
        print(f"{leave_type}: {days_left} days remaining.")

def get_leave_history(employee_id):
    connection = sqlite3.connect('leave_request.db')
    cursor = connection.cursor()

    cursor.execute('''SELECT leave_type, days requested, start_date, end_date
                    FROM leave_requests WHERE employee_id = ? ''',(employee_id,))

    rows = cursor.fetchall()

    for row in rows:
        print(f"Leave Type: {row[0]}, Days Requested: {row[1]}, Start Date: {row[2]}, End Date: {row[3]}")

    connection.close()

if __name__ == "__main__":
    empl_id = input("Enter your Employee ID to apply for leave: ").strip()

    # Keep asking for leave type until a valid one is provided
    leave_type = input("Enter the type of leave you are applying for: ").strip()
    while leave_type not in valid_leave:
        print("Error: Invalid leave type. Please choose from the following options:")
        for leave in valid_leave:
            print(f"- {leave}")
        leave_type = input("Enter a valid leave type: ").strip()

    # Handle empty or invalid number of days
    while True:
        days_input = input("Enter the number of days: ").strip()
        if not days_input.isdigit():
            print("Error: Please enter a valid number.")
        else:
            days = int(days_input)
            if days > 0:
                break
            else:
                print("Error: Number of days must be greater than zero.")

    # Input for start and end dates
    start_date = input("Enter leave start date (YYYY-MM-DD): ").strip() + "T09:00:00"
    end_date = input("Enter leave end date (YYYY-MM-DD): ").strip() + "T17:00:00"

    leave_application(empl_id, leave_type, days, start_date, end_date)
    check_leave_balance(empl_id)
