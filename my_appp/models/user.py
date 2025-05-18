class User:
    def __init__(self, username, email, role="attendee"):
        self.username = username
        self.email = email
        self.role = role
        self.bookings = []  # Public list

    def book_event(self, event):
        if event in self.bookings:
            print(f"{self.username} already booked '{event.title}'.")
        else:
            self.bookings.append(event)
            event.add_attendee(self)
            print(f"{self.username} booked '{event.title}'.")

    def get_bookings(self):
        return self.bookings
