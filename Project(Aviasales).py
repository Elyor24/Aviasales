import csv
import os
from datetime import datetime
from colorama import Fore, Style, init


init(autoreset=True)

BOOKINGS_FILE = "Nabijonov&Jurakulova.csv"


def initialize_csv(file_name):
    if not os.path.exists(file_name):
        with open(file_name, mode="w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Booking ID", "Departure", "Destination", "Date", "Class", "Seats", "Rows", "Total Price", "Payment Method", "Status"])


def save_booking(data, file_name):
    with open(file_name, mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(data)


class FlightBooking:
    def __init__(self, departure, destination, flight_date, class_type, seats, seat_rows, payment_method):
        self.departure = departure
        self.destination = destination
        self.flight_date = flight_date
        self.class_type = class_type
        self.seats = seats
        self.seat_rows = seat_rows
        self.payment_method = payment_method
        self.status = "Confirmed"
        self.total_price = 0
        self.prices = {"economy": 200, "business": 400, "vip": 600}

    def calculate_price(self):
        if self.class_type in self.prices:
            self.total_price = self.prices[self.class_type] * self.seats
        else:
            self.total_price = 0
        return self.total_price

    def book(self):
        booking_id = f"B{int(datetime.now().timestamp())}"  # Unique ID
        self.calculate_price()
        return [
            booking_id, self.departure, self.destination, self.flight_date,
            self.class_type.capitalize(), self.seats, self.seat_rows,
            self.total_price, self.payment_method.capitalize(), self.status
        ]


def list_countries():
    return ["Uzbekistan", "Moscow", "New York", "Dubai", "China", "Qatar"]


def main():
    initialize_csv(BOOKINGS_FILE)
    print(Fore.CYAN + "\nWelcome to Nabijonov & Jurakulova Company!")

    while True:
        print(Fore.YELLOW + "\n1. Choose Country")
        print("2. Booking Flight")
        print("3. To-Do List")
        print("4. Exit")
        choice = input(Fore.GREEN + "Enter your choice: ")

        if choice == "1":  
            countries = list_countries()
            print(Fore.CYAN + "\nAvailable Countries:")
            for i, country in enumerate(countries, 1):
                print(Fore.MAGENTA + f"{i}. {country}")

            departure_index = int(input(Fore.GREEN + "\nSelect departure country (1-6): ")) - 1
            destination_index = int(input(Fore.GREEN + "Select destination country (1-6): ")) - 1
            
            if departure_index == destination_index:
                print(Fore.RED + "Departure and destination cannot be the same!")
                continue

            departure_country = countries[departure_index]
            destination_country = countries[destination_index]
            print(Fore.CYAN + f"\nSelected: {departure_country} to {destination_country}")

        elif choice == "2":  
            flight_date = input(Fore.GREEN + "\nEnter flight date (YYYY-MM-DD): ")
            class_type = input(Fore.GREEN + "Enter class type (economy, business, vip): ").lower()
            seats = int(input(Fore.GREEN + "Enter number of seats: "))
            seat_rows = input(Fore.GREEN + "Choose seat rows (e.g., A1, A2): ")

            confirm = input(Fore.GREEN + "\nDo you want to book a ticket? (Yes/No): ").lower()
            if confirm == "yes":
                payment_method = input(Fore.GREEN + "Choose payment method (Visa or Cash): ").lower()

                booking = FlightBooking(departure_country, destination_country, flight_date, class_type, seats, seat_rows, payment_method)
                booking_data = booking.book()
                save_booking(booking_data, BOOKINGS_FILE)

                print(Fore.GREEN + "\nBooking Confirmed!")
                print(Fore.CYAN + f"Departure: {departure_country} | Destination: {destination_country}")
                print(f"Date: {flight_date} | Class: {class_type.capitalize()} | Seats: {seats} | Rows: {seat_rows}")
                print(Fore.YELLOW + f"Total Price: ${booking.total_price} | Payment: {payment_method.capitalize()}")
            else:
                print(Fore.RED + "\nBooking cancelled.")

        elif choice == "3":  
            print(Fore.CYAN + "\nTo-Do List - Flight Bookings:")
            with open(BOOKINGS_FILE, mode="r") as file:
                reader = csv.reader(file)
                for row in reader:
                    print(Fore.YELLOW + str(row))

        elif choice == "4": 
            print(Fore.GREEN + "Thank you for using our service!")
            break

        else:
            print(Fore.RED + "Invalid choice. Please try again.")


main()