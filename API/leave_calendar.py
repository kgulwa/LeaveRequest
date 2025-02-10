import os
import datetime
from dotenv import load_dotenv
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from google.auth.transport.requests import Request

# Load environment variables from the .env file
load_dotenv()

# Fetch credentials from environment variables
client_id = os.getenv("GOOGLE_CLIENT_ID")
client_secret = os.getenv("GOOGLE_CLIENT_SECRET")
SCOPES = ["https://www.googleapis.com/auth/calendar"]

def authenticate_google_calendar():
    """Authenticate and return Google Calendar API service."""
    creds = None

    # Check if token.json exists to load saved credentials
    if os.path.exists("token.json"):
        creds = Credentials.from_authorized_user_file("token.json")

    # Authenticate if credentials are missing or invalid
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            # Corrected client_config format
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

        # Save credentials for future use
        with open("token.json", "w") as token:
            token.write(creds.to_json())

    try:
        # Build Google Calendar API service
        service = build("calendar", "v3", credentials=creds)

        # Get current time in RFC3339 format
        now = datetime.datetime.utcnow().isoformat() + "Z"

        # Fetch upcoming 10 events
        events_result = service.events().list(
            calendarId="primary", timeMin=now, maxResults=10, singleEvents=True, orderBy="startTime"
        ).execute()

        events = events_result.get("items", [])

        if not events:
            print("No upcoming events found.")
            return

        # Print event details
        for event in events:
            start = event["start"].get("dateTime", event["start"].get("date"))
            print(f"{start} - {event['summary']}")

    except Exception as error:
        print("An error occurred:", error)

if __name__ == "__main__":
    authenticate_google_calendar()
