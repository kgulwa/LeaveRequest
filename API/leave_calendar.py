import os
import datetime
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

# Define API settings
CLIENT_SECRET_FILE = "client_secret.json"
SCOPES = ["https://www.googleapis.com/auth/calendar.readonly"]
TOKEN_FILE = "token.json"

def authenticate_google_calendar():
    """Authenticate and return Google Calendar API service."""
    credentials = None

    # Load existing credentials if they exist
    if os.path.exists(TOKEN_FILE):
        credentials = Credentials.from_authorized_user_file(TOKEN_FILE)

    # If credentials are invalid or don't exist, perform authentication
    if not credentials or not credentials.valid:
        flow = InstalledAppFlow.from_client_secrets_file(CLIENT_SECRET_FILE, SCOPES)
        credentials = flow.run_local_server(port=0)

        # Save credentials for future use
        with open(TOKEN_FILE, "w") as token:
            token.write(credentials.to_json())

    return build("calendar", "v3", credentials=credentials)

def view_calendar():
    """Retrieve and display upcoming events from Google Calendar."""
    service = authenticate_google_calendar()
    
    # Get the next 10 events
    now = datetime.datetime.utcnow().isoformat() + "Z"
    events_result = (
        service.events()
        .list(calendarId="primary", timeMin=now, maxResults=10, singleEvents=True, orderBy="startTime")
        .execute()
    )
    events = events_result.get("items", [])

    if not events:
        print("No upcoming events found.")
        return

    for event in events:
        start = event["start"].get("dateTime", event["start"].get("date"))
        print(f"{start} - {event['summary']}")

if __name__ == "__main__":
    view_calendar()
