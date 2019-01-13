from __future__ import print_function
import datetime
from googleapiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools
import pymysql
import json



# If modifying these scopes, delete the file token.json.
SCOPES = 'https://www.googleapis.com/auth/calendar.readonly'

class Business:
    def __init__(self, name, phone, email, EID):
        self.name = name
        self.phone = phone
        self.email = email
        self.EID = EID

def retrieveFromDB():
    bus = Business('SubREEE', 1234567890, 'subway@aol.com', 5)
    connection = pymysql.connect(host='35.236.23.230',
                             user='root',
                             password='',
                             db='businesses')
    crsr = connection.cursor()
    crsr.execute("SELECT cred FROM entries")  
    ans = crsr.fetchall()  
    # for json in ans:
        # if json is not None:
        #     print(json)
    if ans is not None:
        print(ans)
        
        getCredentials(json.dumps(ans))


def getCredentials(json):
    """Shows basic usage of the Google Calendar API.
    Prints the start and name of the next 10 events on the user's calendar.
    """
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    store = file.Storage('token.json')
    creds = store.get()
    # print('Type: ', type(creds))

    if not creds or creds.invalid:
        flow = client.flow_from_clientsecrets('credentials.json', SCOPES)
        creds = tools.run_flow(flow, store)
    getEvents(creds)

def getEvents(creds):
    service = build('calendar', 'v3', http=creds.authorize(Http()))

    # Call the Calendar API
    now = datetime.datetime.utcnow().isoformat() + 'Z' # 'Z' indicates UTC time
    print('Getting the upcoming 10 events')
    events_result = service.events().list(calendarId='primary', timeMin=now,
                                        maxResults=10, singleEvents=True,
                                        orderBy='startTime').execute()
    events = events_result.get('items', [])

    if not events:
        print('No upcoming events found.')

    daysOpen = {}
    for event in events:
        # start = event['start'].get('dateTime', event['start'].get('date'))
        # Start Info
        startInfo = str({event['start'].get('dateTime')})
        endInfo = str({event['end'].get('dateTime')})
        date = startInfo[0:10]
        startTime = startInfo[11:16]
        endTime = endInfo[11:16]
        if 'description' in event:
            print(event['description'])

if __name__ == '__main__':
    # getCredentials()
    retrieveFromDB()