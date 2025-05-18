class EventPlatform:
    def __init__(self):
        self.users = []
        self.events = []

    def register_user(self, user):
        if user not in self.users:
            self.users.append(user)

    def create_event(self, event):
        if event not in self.events:
            self.events.append(event)

    def get_events(self):
        return self.events
