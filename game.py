from collections import defaultdict
import inspect

from event import Event, EventType
from investigator import Investigator
from listener import EventListener


class Game:
  
  _handlers:dict[EventType, list] = defaultdict(list)
  _investigators:list[Investigator] = []


  @classmethod
  def triggerEvent(cls, event:Event):
    for func in cls._handlers[event.type]:
      func(event)
    

  @classmethod
  def registerListener(cls, listener:EventListener):
    for name, method in inspect.getmembers(listener, inspect.ismethod):
      if hasattr(method, "_event_type"):
        cls._handlers[method._event_type].append(method)


  @classmethod
  def addInvestigator(cls, investigator:Investigator):
    cls._investigators.append(investigator)   


  @classmethod
  def getInvestigators(cls):
    return cls._investigators