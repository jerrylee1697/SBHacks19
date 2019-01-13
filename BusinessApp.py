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
    def __init__(self, name, phone, email, EID, menu, JSON):
        self.name = name
        self.phone = phone
        self.email = email
        self.EID = EID
        self.menu = menu
        self.JSON = JSON

def retrieveFromDB():
    # bus = Business('SubREEE', 1234567890, 'subway@aol.com', 5)
    connection = pymysql.connect(host='35.236.23.230',
                             user='root',
                             password='',
                             db='businesses')
    crsr = connection.cursor()
    name = input('Business Name: ')
    phone = input('Phone Number: ')
    email = input('Email: ')
    EID = input('EID: ')
    menu = input('Menu: ')
    JSON = getCredentials()
    sql = "INSERT INTO data (name, phone, email, EId, cal, menu) VALUES (%s, %s, %s, %s, %s, %s)"
    val = (name, phone, email, EID, JSON, menu)
    crsr.execute(sql, val)
    connection.commit()
    # crsr.execute("SELECT * FROM entries")  
    # ans = crsr.fetchall()  
    # for json in ans:
        # if json is not None:
        #     print(json)
    # if ans is not None:
    #     getCredentials(json.dumps(ans))


def getCredentials():
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
    return getEvents(creds)

def getEvents(creds):
    service = build('calendar', 'v3', http=creds.authorize(Http()))

    # Call the Calendar API
    now = datetime.datetime.utcnow().isoformat() + 'Z' # 'Z' indicates UTC time
    print('Getting the upcoming 10 events')
    events_result = service.events().list(calendarId='primary', timeMin=now,
                                        maxResults=1000, singleEvents=True,
                                        orderBy='startTime').execute()
    events = events_result.get('items', [])

    if not events:
        print('No upcoming events found.')

    daysOpen = []
    for event in events:
        # start = event['start'].get('dateTime', event['start'].get('date'))
        # Start Info
        startInfo = str({event['start'].get('dateTime')})
        endInfo = str({event['end'].get('dateTime')})
        date = startInfo[2:12]
        startTime = startInfo[13:18]
        endTime = endInfo[13:18]
        if date == 'one}': continue
        if 'description' in event:
            # print(event['description'])
            daysOpen.append({date : [startTime, endTime, event['description']]})
        else:
            daysOpen.append({date : [startTime, endTime, 'No Specials Today']})
    # print(daysOpen)
    JSONFile = json.dumps(daysOpen, sort_keys=False, indent=4)
    return JSONFile
if __name__ == '__main__':
    # getCredentials()
    retrieveFromDB()