
from google.appengine.ext import ndb

from endpoints_proto_datastore.ndb.model import EndpointsModel


class Event(EndpointsModel):
    """ An event. """
    _message_fields_schema = ("entityKey", "date", "time", "title", "description", "last_touch_date_time")
    date = ndb.StringProperty()
    time = ndb.StringProperty()
    title = ndb.StringProperty()
    description = ndb.StringProperty()
    last_touch_date_time = ndb.DateTimeProperty(auto_now=True)
    
class Announcement(EndpointsModel):
    """ An announcement. """
    _message_fields_schema = ("entityKey", "title", "description", "last_touch_date_time")
    title = ndb.StringProperty()
    description = ndb.StringProperty()
    last_touch_date_time = ndb.DateTimeProperty(auto_now=True)
    