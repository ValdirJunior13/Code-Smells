from abc import ABC, abstractmethod

# Interface Observer
class Observer(ABC):
    @abstractmethod
    def update(self, winner_name):
        pass

# Interface Subject
class Subject(ABC):
    @abstractmethod
    def add_observer(self, observer):
        pass

    @abstractmethod
    def remove_observer(self, observer):
        pass

    @abstractmethod
    def notify_observers(self, winner_name):
        pass