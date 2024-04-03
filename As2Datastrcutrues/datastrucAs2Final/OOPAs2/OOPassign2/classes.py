class Artwork:
    def __init__(self, title, artist, date_of_creation, historical_significance):
        self._title = title
        self._artist = artist
        self._date_of_creation = date_of_creation
        self._historical_significance = historical_significance

    def get_title(self):
        return self._title

    def set_title(self, title):
        self._title = title

    def get_artist(self):
        return self._artist

    def set_artist(self, artist):
        self._artist = artist

    def get_date_of_creation(self):
        return self._date_of_creation

    def set_date_of_creation(self, date_of_creation):
        self._date_of_creation = date_of_creation

    def get_historical_significance(self):
        return self._historical_significance

    def set_historical_significance(self, historical_significance):
        self._historical_significance = historical_significance


class Exhibition:
    def __init__(self, name, duration, location):
        self._name = name
        self._duration = duration
        self._location = location

    # Getter and setter methods for name attribute
    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name

    # Getter and setter methods for duration attribute
    def get_duration(self):
        return self._duration

    def set_duration(self, duration):
        self._duration = duration

    # Getter and setter methods for location attribute
    def get_location(self):
        return self._location

    def set_location(self, location):
        self._location = location

from enum import Enum


class VisitorCategory(Enum):
    ADULT = "Adult"
    CHILD = "Child"
    STUDENT = "Student"
    SENIOR_CITIZEN = "Senior citizen"
    TEACHER = "Teacher"


class Visitor:
    def __init__(self, name, age, category):
        self.name = name
        self.age = age
        self.category = category

    # Getters and setters for attributes
    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_age(self):
        return self.age

    def set_age(self, age):
        self.age = age

    def get_category(self):
        return self.category

    def set_category(self, category):
        self.category = category

from enum import Enum

class TicketType(Enum):
    GENERAL_ADMISSION = "General Admission"
    CHILD = "Child Ticket"
    STUDENT = "Student Ticket"
    SENIOR_CITIZEN = "Senior Citizen Ticket"
    GROUP = "Group Ticket"
    SPECIAL_EVENT = "Special Event Ticket"



class Ticket:
    def __init__(self, ticket_id, price, purchase_date, discount):
        self._ticket_id = ticket_id
        self._price = price
        self._purchase_date = purchase_date
        self._discount = discount

    # Getters and setters for attributes
    def get_ticket_id(self):
        return self._ticket_id

    def set_ticket_id(self, ticket_id):
        self._ticket_id = ticket_id

    def get_price(self):
        return self._price

    def set_price(self, price):
        self._price = price

    def get_purchase_date(self):
        return self._purchase_date

    def set_purchase_date(self, purchase_date):
        self._purchase_date = purchase_date

    def get_discount(self):
        return self._discount

    def set_discount(self, discount):
        self._discount = discount

    def calculate_price(self):
        # Pricing logic based on visitor category and discount
        if self._discount:
            return self._price * (1 - self._discount / 100)
        else:
            return self._price



from enum import Enum

class EventType(Enum):
    TOURS = "Tours"
    MUSICAL_CONCERTS = "Musical Concerts"
    LIGHTSHOWS = "Lightshows"
    FUNDRAISER = "Fundraiser"

class Event:
    def __init__(self, name, event_type, location):
        self._name = name
        self._event_type = event_type
        self._location = location

    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name

    def get_event_type(self):
        return self._event_type

    def set_event_type(self, event_type):
        self._event_type = event_type

    def get_location(self):
        return self._location

    def set_location(self, location):
        self._location = location

class Museum:
    def __init__(self, name, location):
        self._name = name
        self._location = location
        self._artworks = []
        self._exhibitions = []

    def add_artwork(self, artwork):
        self._artworks.append(artwork)

    def get_artworks(self):
        return self._artworks

    def add_exhibition(self, exhibition):
        self._exhibitions.append(exhibition)

    def get_exhibitions(self):
        return self._exhibitions

    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name

    def get_location(self):
        return self._location

    def set_location(self, location):
        self._location = location

    def open_exhibition(self, exhibition):
        self._exhibitions.append(exhibition)

    def add_event(self, event):
        self._events.append(event)