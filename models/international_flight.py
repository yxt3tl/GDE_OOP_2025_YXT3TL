from models.flight import Flight

class InternationalFlight(Flight):
    def __init__(self, flight_number, destination, departure):
        super().__init__(flight_number, destination, price=2525, departure=departure)

    def info(self):
        return f"InternationalFlight - {self.flight_number}: {self.destination}, Price: {self.price} Fabatka, Departure: {self.departure}"