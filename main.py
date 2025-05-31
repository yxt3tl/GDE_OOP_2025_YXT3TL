import datetime

from models.airline import Airline
from models.domestic_flight import DomesticFlight
from models.international_flight import InternationalFlight
from services.ticket_booking import TicketBooking


def menu():
    
    # Initialization of 3 Flights
    airline = Airline("HighFly Airlines")
    airline.add_flight(DomesticFlight("S25", "Szeged", datetime.datetime(2025, 7, 4, 5, 0)))
    airline.add_flight(DomesticFlight("T25", "Eger", datetime.datetime(2025, 7, 4, 5, 30)))
    airline.add_flight(InternationalFlight("N2525", "Maputo", datetime.datetime(2025, 7, 12, 5, 0)))

    # Initialization of 6 Bookings
    ticket_booking = TicketBooking()
    ticket_booking.create_booking(airline.search_flight('S25'), 1)
    ticket_booking.create_booking(airline.search_flight('T25'), 3)
    ticket_booking.create_booking(airline.search_flight('S25'), 1)
    ticket_booking.create_booking(airline.search_flight('T25'), 3)
    ticket_booking.create_booking(airline.search_flight('N2525'), 1)
    ticket_booking.create_booking(airline.search_flight('N2525'), 3)

    while True:
        print("\n--- Flight Ticket Booking System ---")
        print("1. List of Flights")
        print("2. List of Bookings ")
        print("3. Ticket Booking")
        print("4. Cancellation of a Ticket Booking")
        print("0. Exit")

        choice = input("An option is to be chosen: ")

        if choice == "1":
            for info in airline.list_flights():
                print(info)
        elif choice == "2":
            ticket_booking.list_bookings()
        elif choice == "3":
            print("Available Flights:")
            for info in airline.list_flights():
                print(info)
            flight_number = input("Flight Number to be reserved: ")
            flight_number = airline.search_flight(flight_number)
            if flight_number:
                try:
                    number_of_tickets = int(input("How many tickets would you like to reserve? "))
                    if number_of_tickets <= 0:
                        print("Invalid number.")
                    else:
                        ticket_booking.create_booking(flight_number, number_of_tickets)
                except ValueError:
                    print("Invalid number.")
            else:
                print("No such reservation in the system.")
        elif choice == "4":
            booking_id = input("Booking with ID to be cancelled: ")
            ticket_booking.cancel_booking(booking_id)
        elif choice == "0":
            print("Exit.")
            break
        else:
            print("Invalid input.")

def main():



    # Start User Interface
    menu()

if __name__ == "__main__":
    main()
