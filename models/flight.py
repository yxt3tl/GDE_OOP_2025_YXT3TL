from abc import ABC, abstractmethod

class Flight(ABC):
    
    def __init__(self, fligth_number, destination, departure, price):
        self.flight_number = fligth_number
        self.destination = destination
        self.departure = departure #It should be datetime
        self.price = price
          

    @abstractmethod
    def info(self):
        pass