from __future__ import print_function
import datetime
from googleapiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools
import pymysql
import json

# If modifying these scopes, delete the file token.json.
SCOPES = 'https://www.googleapis.com/auth/calendar.readonly'

def getCredentials():
    """Shows basic usage of the Google Calendar API.
    Prints the start and name of the next 10 events on the user's calendar.
    """
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    store = file.Storage('token.json')
    creds = store.get()
    print('Type: ', type(creds))
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
                                        maxResults=1000, singleEvents=True,
                                        orderBy='startTime').execute()
    events = events_result.get('items', [])

    if not events:
        print('No upcoming events found.')
    for event in events:
        # start = event['start'].get('dateTime', event['start'].get('date'))
        start = event['start'].get('dateTime')
        end = event['end'].get('dateTime', event['end'].get('date'))
        # description = event['description']
        # print('start: ', str(event['start'].get('dateTime'))[0:10])
        startInfo = str({event['start'].get('dateTime')})
        endInfo = str({event['end'].get('dateTime')})
        date = startInfo[0:12]
        startTime = startInfo[13:18]
        endTime = endInfo[13:18]
        print(date)
        if 'description' in event:
            print([date, [startTime, endTime, event['description']]])
        else:
            print([date, [startTime, endTime, None]])
        # print(datetime.datetime.today().strftime('%Y-%m-%d'))
        # print('end: ', end, ' ', event['summary'])
        # print('end: ', event['end'].get('dateTime'), ' ', event['end'].get('date'))
        # if 'description' in event:
        #     print(event['description'])

def test():
    connection = pymysql.connect(host='35.236.23.230',
                             user='root',
                             password='',
                             db='businesses')
    crsr = connection.cursor()

    body = 'subway message hello'
    splitString = body.split()
    count = 0
    businessName = ""
    print(splitString)
    for i in splitString:
        if i == 'message':
            break
        if count != 0:
            businessName = businessName + ' '
        businessName = businessName + i
        count = count + 1

    entry = ("SELECT * FROM data WHERE name='%s'" % businessName)
    crsr.execute(entry)
    records = crsr.fetchall()[0]
    print(records[0])
    # name, phone, email, EId, cal, menu
    json1_data = json.loads(records[4])
    datapoints = json1_data

    print(datapoints)

if __name__ == '__main__':
    # getCredentials()
    test()