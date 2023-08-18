import phonenumbers
from phonenumbers import geocoder, carrier
phone_number1 = phonenumbers.parse("+919448023805")
phone_number2 = phonenumbers.parse("+918762573010")
phone_number3 = phonenumbers.parse("+919741457422")
phone_number4 = phonenumbers.parse("+917411106347")

print("\nPhone Number Location\n")
print(geocoder.description_for_number(phone_number1,"en"))
print(geocoder.description_for_number(phone_number2, "en"))
print(geocoder.description_for_number(phone_number3, "en"))
print(geocoder.description_for_number(phone_number4, "en"))
