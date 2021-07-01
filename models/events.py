from models.event import *
import datetime

event1 = Event(datetime.date(2021, 8, 18), "festival", 6, "outdoors", "party time!")
event2 = Event(datetime.date(2021, 2, 25), "martial arts competition", 200, "meadowbank", "mortal kombat!")

events = [event1, event2]

def add_new_event(event):
    events.append(event)

