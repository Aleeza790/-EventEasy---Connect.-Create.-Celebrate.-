from models.platform import EventPlatform
from models.user import User

platform = EventPlatform()

# ✅ Changed organizer name to 'Aliza'
user1 = User("Aliza", "sadiqalik056@gmail.com", role="organizer")
user2 = User("Batool", "batoolfatima897@gmail.com", role="attendee")

platform.register_user(user1)
platform.register_user(user2)
