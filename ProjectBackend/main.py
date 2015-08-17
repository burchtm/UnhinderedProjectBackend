from datetime import date
import datetime
import os
import time

from google.appengine.ext import ndb
import jinja2
import webapp2

from models import Announcement
from models import Event


jinja_env = jinja2.Environment(loader=jinja2.FileSystemLoader(os.path.dirname(__file__)), autoescape=True)

PARENT_KEY = ndb.Key("Entity", 'ministry_root')

class MainHandler(webapp2.RequestHandler):
    def get(self):
        events = Event.query(ancestor=PARENT_KEY).order(-Event.last_touch_date_time).fetch()
        announcements = Announcement.query(ancestor=PARENT_KEY).order(-Announcement.last_touch_date_time).fetch()
        template = jinja_env.get_template("templates/ministry.html")
        self.response.out.write(template.render({'events': events, 'announcements': announcements}))

class InsertAction(webapp2.RequestHandler):
    def post(self):
        entity_key_urlsafe = self.request.get("entity_key")
        if (self.request.get('type') == 'Event'):
            if entity_key_urlsafe:
                event_key = ndb.Key(urlsafe=entity_key_urlsafe)
                event = event_key.get()
                timestamp = datetime.datetime.strptime(self.request.get("date"), "%Y-%m-%dT%H:%M")
                event.date = timestamp.date()
                event.time = timestamp.time()
                event.title = self.request.get("title")
                event.description = self.request.get("description")
                event.put()
            else:
                timestamp = datetime.datetime.strptime(self.request.get("date"), "%Y-%m-%dT%H:%M")
                new_event = Event(parent=PARENT_KEY,
                                       date=timestamp.date(),
                                       time=timestamp.time(),
                                       title=self.request.get('title'),
                                       description=self.request.get('description'))
                new_event.put()
        elif (self.request.get('type') == 'Announcement'):
            if entity_key_urlsafe:
                announcement_key = ndb.Key(urlsafe=entity_key_urlsafe)
                announcement = announcement_key.get()
                announcement.title = self.request.get("title")
                announcement.description = self.request.get("description")
                announcement.put()
            else:
                new_announcement = Announcement(parent=PARENT_KEY,
                                        title=self.request.get('title'),
                                        description=self.request.get('description'))
                new_announcement.put()
        self.redirect(self.request.referer)

class DeleteAction(webapp2.RequestHandler):
    def post(self):
        entity_key_urlsafe = self.request.get("entity_key")
        if(self.request.get('type') == 'Event'):
            event_key = ndb.Key(urlsafe=entity_key_urlsafe)
            event_key.delete()
        if(self.request.get('type') == 'Announcement'):
            announcement_key = ndb.Key(urlsafe=entity_key_urlsafe)
            announcement_key.delete()
        self.redirect(self.request.referer)

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ("/insert", InsertAction),
    ("/delete", DeleteAction)
], debug=True)
