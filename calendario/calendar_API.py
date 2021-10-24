import os
from google.oauth2 import service_account
import googleapiclient.discovery
import datetime

CAL_ID= os.environ['CAL_ID']
SCOPES = ['https://www.googleapis.com/auth/calendar']
SERVICE_ACCOUNT_FILE = 'calendario/google-credentials.json'


def create_event():
    print("RUNNING TEST_CALENDAR()")

    credentials = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)
    service = googleapiclient.discovery.build('calendar', 'v3', credentials=credentials)

    
    # CREATE A NEW EVENT

    new_event = {
    'summary': "Pedido 21",
    'description': '1 Torta de chocolate',
    'start': {
        'date': f"{datetime.date.today()+ datetime.timedelta(days=3)}",
        'timeZone': 'America/New_York',
    },
    'end': {
        'date': f"{datetime.date.today() + datetime.timedelta(days=4)}",
        'timeZone': 'America/New_York',
    },
    }
    service.events().insert(calendarId=CAL_ID, body=new_event).execute()
    print('Event created')

    

