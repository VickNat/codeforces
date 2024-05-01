import phonenumbers
from phonenumbers import geocoder

phone_number = "+83082255"
parsed_number = phonenumbers.parse(phone_number)
country = geocoder.description_for_number(parsed_number, "en")
print(f"The phone number {phone_number} is registered in {country}")