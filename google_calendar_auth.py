import os
import pickle
import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors
from google.auth.transport.requests import requests


#Function to authenticate user

def authenticate_google_account():
    SCOPES = ["https://ww.googleapis.com/auth/calendar.readonly", "https://ww.googleapis.com/auth/calendar"]
    creds = None

    #check if token.pickle file exists. It stores the user's credentials

    if os.path.exists("token.pickle"):
        with open("token.pickle", "rb") as token:
            creds = pickle.load(token)

    #check if there are no valid credentials available, prompt user to login

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request()) #refresh the credentials if they are expired

        else:  #if no valid credentials are provided then let user login.
            
            flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES) #path to credentials file

            creds = flow.run_local_server(port=0)# opens window for authentication

        with open("token.pickle", "wb") as token:
            pickle.dump(creds, token)

    return creds
           

def get_google_calendar_service():
    creds = authenticate_google_account() # Authenticate user
    service = googleapiclient.discovery.build("calendar", "v3", credentials=creds) #create service object
    return service