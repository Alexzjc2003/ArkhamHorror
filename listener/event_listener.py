from event.event_type import EventType

def Handle(event_type:EventType):
  def decorator(func):
    func._event_type = event_type
    return func
  return decorator


class EventListener:
  def __init__(self):
    pass

