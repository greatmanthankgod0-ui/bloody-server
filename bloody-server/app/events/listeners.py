from app.events.event_bus import event_bus
from app.events.events import USER_REGISTERED


def welcome(data):
    print(
        f"Welcome {data.username}"
    )


event_bus.subscribe(
    USER_REGISTERED,
    welcome,
)
