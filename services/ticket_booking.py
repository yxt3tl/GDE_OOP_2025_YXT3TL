import datetime
import random


class TicketBooking:
    def __init__(self):
        self.bookings = {}

    def create_booking(self, flight, number_of_tickets):
        booking_id = random.randint(100000, 999999)
        if flight.departure < datetime.datetime.now():
            print("The booking time has already been closed.")
            return 0
        if str(booking_id) in self.bookings:
            self.bookings[str(booking_id)]['number_of_tickets'] += number_of_tickets
        else:
            self.bookings[str(booking_id)] = {'booking_id': str(booking_id), 'flight': flight, 'number_of_tickets': number_of_tickets }
        total_price = flight.price * number_of_tickets
        print(f"Successful reservation: {number_of_tickets} tickets to {flight.info()} flight . Price: {total_price} Fabatka. Booking ID: {str(booking_id)}")
        return total_price

    def cancel_booking(self, booking_id):
        if str(booking_id) in self.bookings:
            del self.bookings[str(booking_id)]
            print(f"Booking cancelled: {str(booking_id)}")
        else:
            print("No such reservation in the system.")


    def list_bookings(self):
        if not self.bookings:
            print("No reservation in the system.")
        for data in self.bookings.values():
            flight = data['flight']
            number_of_tickets = data['number_of_tickets']
            booking_id = data['booking_id']
            print(f"{flight.info()}, Number of tickets reserved: {number_of_tickets}, Booking ID: {booking_id}")