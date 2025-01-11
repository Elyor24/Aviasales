

Nabijonov & Jurakulova Flight Booking System

This is a Python-based flight booking system for Nabijonov & Jurakulova Company. It allows users to book flights, view available countries, and maintain a to-do list of flight bookings. The application utilizes CSV files to store booking details and uses the colorama library to enhance console output.

Features


	•	Country Selection: Users can select departure and destination countries from a predefined list.
	•	Flight Booking: Users can input flight details such as date, class type, seats, and payment method, then confirm bookings.
	•	Price Calculation: Automatically calculates the total price based on the selected class and the number of seats.
	•	Booking Records: Saves all bookings in a CSV file for easy record-keeping.
	•	To-Do List: Allows users to view all saved flight bookings in a tabular format.

Prerequisites


Before running the program, ensure you have the following installed:


	1.	Python 3.6 or higher
	2.	Required libraries:
	  •	colorama

You can install colorama using pip:


pip install colorama

How to Run


	1.	Clone or download the repository to your local machine.
	2.	Navigate to the project directory.
	3.	Run the script using:

python flight_booking.py


File Structure

	•	flight_bookings.csv: Automatically created CSV file to store flight booking records.
	•	flight_booking.py: Main script for running the flight booking system.

Usage

	1.	Start the program and follow the prompts to choose a departure and destination country.
	2.	Input flight details such as the date, class type, and number of seats.
	3.	Confirm your booking and choose a payment method.
	4.	View your bookings using the “To-Do List” option.

Example

Here’s how a typical booking process might look:

	1.	Select a departure country: 1 (USA)
	2.	Select a destination country: 2 (Germany)
	3.	Enter flight details:
	•	Date: 2025-01-20
	•	Class: economy
	•	Seats: 2
	•	Rows: A1, A2
	4.	Confirm the booking: yes
	5.	Choose payment method: card
	6.	View the “To-Do List” to see the booking record.

Improvements and Contributions



This project is a basic implementation. Future enhancements may include:

	•	Adding a user interface (web or desktop).
	•	Expanding the list of countries dynamically from an API.
	•	Implementing additional payment options.
	•	Providing more detailed error handling.

Contributions are welcome! Feel free to fork this repository and submit a pull request with your changes.
