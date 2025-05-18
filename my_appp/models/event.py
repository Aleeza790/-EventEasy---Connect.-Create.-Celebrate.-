class Event:
    def __init__(self, title, organizer, description, date, location, price):
        self.title = title
        self.organizer = organizer
        self.description = description
        self.date = date
        self.location = location
        self.price = price
        self.attendees = []

    def add_attendee(self, user):
        if user not in self.attendees:
            self.attendees.append(user)
