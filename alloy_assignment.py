import requests
from datetime import datetime
import re 

AUTH_TOKEN = ""

ALLOY_URL = "https://sandbox.alloy.co/v1/evaluations"

def validate_date(date_str):
	try:
		datetime.strptime(date_str, "%Y-%m-%d")
		return True
	except ValueError:
		return False

def validate_ssn(ssn):
	return ssn.isdigit() and len(ssn) == 9

def validate_email(email):
	return re.fullmatch(r"[^@]+@[^@]+\.[^@]+", email) is not None

def validate_state(state):
	return state.isalpha() and len(state) == 2

def validate_country(country):
	return country.upper() == "US"

def get_applicant_data():
	print("Enter applicant details:")
	
	while True:
		first_name = input("First Name: ")
		if first_name:
			break
		print("First name is required. Please provide a first name to proceed.")

	last_name = input("Last Name: ")

	while True:
		birth_date = input("Enter Date of Birth (YYYY-MM-DD): ")
		if validate_date(birth_date):
			break
		print("Invalid date format. Please use YYYY-MM-DD.")

	while True:
		ssn = input("Enter SSN (9 digits, no dashes): ")
		if validate_ssn(ssn):
			break
		print("SSN must be exactly 9 digits.")

	while True:
		email = input("Enter email address: ")
		if validate_email(email):
			break
		print("Invalid email format.")

	address_line1 = input("Address Line 1: ")
	address_line2 = input("Address Line 2: ")
	city = input("City: ")

	while True:
		state = input("State (2-letter code): ")
		if validate_state(state):
			break
		print("State must be a 2-letter code (e.g., NY, CA).")

	postal_code = input("Zip/Postal Code: ")

	while True:
		country = input("Country (must be 'US'): ")
		if validate_country(country):
			break
		print("Country must be 'US'.")

	return {
		"name_first": first_name,
		"name_last": last_name,
		"birth_date": birth_date,
		"document_ssn": ssn,
		"email_address": email,
		"addresses": [
		{
			"address_line_1": address_line1,
			"address_line_2": address_line2,
			"address_city": city,
			"address_state": state.upper(),
			"address_postal_code": postal_code,
			"address_country_code": country.upper()
		}
		]
       
	}

def submit_to_alloy(applicant_data):
	headers = {
		"accept": "application/json",
		"authorization": AUTH_TOKEN,
		"content-type": "application/json"
	}

	
	response = requests.post(ALLOY_URL, json=applicant_data, headers=headers)

	return response.json()


def main():
	print("Welcome to the Alloy Identity Evaluation Script")
	print("-----------------------------------------------")

	applicant_data = get_applicant_data()
	response = submit_to_alloy(applicant_data)

	try:
		outcome = response["summary"]["outcome"]

		if outcome == "Approved":
			print("Congratulations! You are approved.")
		elif outcome == "Manual Review":
			print("Your application is under review. Please wait for further updates.")
		elif outcome == "Denied":
			print("Unfortunately, we cannot approve your application at this time.")
		else:
			print("Unexpected response from Alloy: ", outcome)
	
	except:
		print("The response did not contain an outcome. Here's what we got instead:")
		print(response)

if __name__ == "__main__":
	main()

