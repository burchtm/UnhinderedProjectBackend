'''
Created on Jul 29, 2015

@author: burchtm, johnsoaa
'''
import endpoints
import protorpc
from datetime import date

from models import Event
from models import Announcement
from models import DailyVerse
import main

@endpoints.api(name="ministry", version="v1", description="Ministry API")
class MinistryApi(protorpc.remote.Service):
    """" API for the CRUD methods """
    pass
    
    #Methods will be either methods (returns a single object) or query methods (return a collection)
    
    @Event.method(name="event.insert", path="event/insert", http_method="POST")
    def event_insert(self, request):
        """insert or update an event"""
        if request.from_datastore:
            my_event = request
        else:
            my_event = Event(parent=main.PARENT_KEY, date=request.date, time=request.time, title=request.title, description=request.description)
        my_event.put()
        return my_event

    @Event.query_method(query_fields=("limit", "order", "pageToken"), name="event.list", path="event/list", http_method="GET")
    def event_list(self, query):
        """get all the events"""
        # We could add filters
        return query
    
    @Event.method(request_fields=("entityKey",), name="event.delete", path="event/delete/{entityKey}", http_method="DELETE")
    def event_delete(self, request):
        """ Delete an event if its there """
        if not request.from_datastore:
            raise endpoints.NotFoundException("Event to be deleted not found")
        
        request.key.delete()
        return Event(title='deleted')

    @Announcement.method(name="announcement.insert", path="announcement/insert", http_method="POST")
    def announcement_insert(self, request):
        """insert or update an announcement"""
        if request.from_datastore:
            my_announcement = request
        else:
            my_announcement = Announcement(parent=main.PARENT_KEY, title=request.title, description=request.description)
        my_announcement.put()
        return my_announcement

    @Announcement.query_method(query_fields=("limit", "order", "pageToken"), name="announcement.list", path="announcement/list", http_method="GET")
    def announcement_list(self, query):
        """get all the announcements"""
        # We could add filters
        return query
    
    @Announcement.method(request_fields=("entityKey",), name="announcement.delete", path="announcement/delete/{entityKey}", http_method="DELETE")
    def announcement_delete(self, request):
        """ Delete an announcement if its there """
        if not request.from_datastore:
            raise endpoints.NotFoundException("Announcement to be deleted not found")
        
        request.key.delete()
        return Announcement(title='deleted')

    @DailyVerse.method(request_fields=(), name="verse.today", path="verse/today", http_method="GET")
    def daily_verse(self, request):
        verse_query = DailyVerse.query(DailyVerse.last_touch_date == date.today())
        return verse_query.get()

app = endpoints.api_server([MinistryApi], restricted = False)