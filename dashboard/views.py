
from __future__ import print_function
import datetime
from apiclient.discovery import build
from httplib2 import Http
from oauth2client import file as oauth_file, client, tools

from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.http import HttpResponse
from .models import Slot

SCOPES = 'https://www.googleapis.com/auth/calendar'

# Create your views here.
def dashBoard(request):
	if "username" in request.session:
		# id we use our database
		# all_slots = Slot.objects.all()
		# vacant_slot = []
		# booked_slot_user = []
		# for each_slot in all_slots:
		# 	each_slot = str(each_slot).split()
		# 	if each_slot[4]=="False":
		# 		vacant_slot.append([each_slot[0]+'T'+each_slot[1], each_slot[2]+'T'+each_slot[3]])
		# 	else:
		# 		if each_slot[5]==request.session["username"]:
		# 			booked_slot_user.append([each_slot[0]+'T'+each_slot[1], each_slot[2]+'T'+each_slot[3]])

		# No use of database
		# # return HttpResponse("<h2>"+str(all_slots[2])+"</h2>")
		vacant_slot = []
		booked_slot_user = []
		all_slots = get_All_Slots()
		for each_slot in all_slots:
			if each_slot[2]=="Available":
				vacant_slot.append(each_slot)
			elif each_slot[2]=="chit_chat_appointment":
				for attendee in each_slot[4]:
					if attendee["email"] == request.session["username"]:
						booked_slot_user.append(each_slot)
				
		# return HttpResponse("<h2>"+str(attendee["email"])+"</h2>")
		return render(request, 'dashboard/dashboard.html', {'booked_slot_user': booked_slot_user, 'vacant_slot': vacant_slot })
	else:
		return HttpResponseRedirect('/login')
 

def get_All_Slots():
	store = oauth_file.Storage('/media/sonu/Data/Atulit_Shubham_hyrelabs_django/atulit_project_calender/dashboard/token.json')
	creds = store.get()
	if not creds or creds.invalid:
	    flow = client.flow_from_clientsecrets('/media/sonu/Data/Atulit_Shubham_hyrelabs_django/atulit_project_calender/dashboard/credentials.json', SCOPES)
	    creds = tools.run_flow(flow, store)
	service = build('calendar', 'v3', http=creds.authorize(Http()))

	# Call the Calendar API
	now = datetime.datetime.utcnow().isoformat() + 'Z'  # 'Z' indicates UTC time
	print('Getting the upcoming 20 events')
	events_result = service.events().list(calendarId='primary', timeMin=now,
	                                      maxResults=20, singleEvents=True,
	                                      orderBy='startTime').execute()
	events = events_result.get('items', [])
	all_slots = []
	if not events:
	    return all_slots
	for event in events:
	    start = event['start']['dateTime']
	    end = event['end']['dateTime']
	    summary = event['summary']
	    id_ = event["id"]
	    attendees = []
	    if "attendees" in event:
	    	attendees = event["attendees"]
	    all_slots.append([start, end, summary, id_, attendees])
	return all_slots

def book_slots(request):
	id_ = request.GET.get("id")
	username = request.session["username"]
	result = update_event(username, id_)
	if result=="success":
		return HttpResponseRedirect('/dashBoard')
	return HttpResponse("<h2>Event not updated</h2>")

def update_event(username, id_):
	store = oauth_file.Storage('/media/sonu/Data/Atulit_Shubham_hyrelabs_django/atulit_project_calender/dashboard/token.json')
	creds = store.get()
	if not creds or creds.invalid:
	    flow = client.flow_from_clientsecrets('/media/sonu/Data/Atulit_Shubham_hyrelabs_django/atulit_project_calender/dashboard/credentials.json', SCOPES)
	    creds = tools.run_flow(flow, store)
	GCAL = build('calendar', 'v3', http=creds.authorize(Http()))


	# TIMEZONE = 'India/Los_Angeles'
	EVENT = {
		'summary': 'chit_chat_appointment',
	    'attendees': [
	        {'email': str(username)},
	    ],
	}
	EVENT_ID = id_
	e = GCAL.events().patch(calendarId='primary', eventId=EVENT_ID,
	        sendNotifications=True, body=EVENT).execute()

	if e['summary']=="chit_chat_appointment":
		return "success"
	else:
		return "fail"