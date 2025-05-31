from models.flight import Flight

class DomesticFlight(Flight):
    def __init__(self, flight_number, destination, departure):
        super().__init__(flight_number, destination, price=25, departure=departure)

    def info(self):
        return f"DomesticFlight - {self.flight_number}: {self.destination}, Price: {self.price} Fabatka, Departure: {self.departure}"