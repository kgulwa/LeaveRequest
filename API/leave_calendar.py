import os
import datetime
from google.oauth2.creds import creds
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from google.auth.transport.request import Request 


# Define API settings
CLIENT_SECRET_FILE = "client_secret.json"
SCOPES = ["https://www.googleapis.com/auth/calendar"]



def authenticate_google_calendar():
    """Authenticate and return Google Calendar API service."""
    creds = None

    if os.path.exists("token.json"): #Loads existing credentials if there are any
        creds = Credentials.from_authorized_user_file("token.json")

    if not creds or not creds.valid: # performs authentication if invalid credentials are provided or they do not exist at all
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())

        else:
            flow = InstalledAppFlow.from_client_secrets_file("client_secret.json", SCOPES)
            creds = flow.run_local_server(port= 0)

        with open("token.json", "w") as token: #saves credentials for future purposes
            token.write(creds.to_json())

    try:
        service = build("calendar", "v3", credentials=creds)


        now = dt.datetime.now().isoformat() + "Z"

        events_result = service.events().list(calendarId = "primary", timeMin = now, maxResults =10, singleEvents = True, OrderBy = "startTime")

    except HttpError as error:
        print("An Error occured:", error)

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
