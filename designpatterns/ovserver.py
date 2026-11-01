from abc import ABC, abstractmethod
from __future__ import annotations
from typing import List
from random import randrange

class Subject(ABC):

  @abstractmethod
  def attach(self, observer: Observer) -> None:
    pass

  @abstractmethod
  def detach(self, observer: Observer) -> None:
    pass

  @abstractmethod
  def notify(self) -> None:
    pass


class ConcreteSubject(Subject):

  _state : int = None
  _observers: List[Observer] = []

  def attach(self, observer: Observer) -> None:
    print("Subject: Attached an observer")
    self._observers.append(observer)

  def detach(self, observer):
    print("Subject: Detached an observer")
    self._observers.remove(observer)

  def notify(self):
    print("Subject: Notifying observers")
    for i in self._observers:
      i.update(self)

