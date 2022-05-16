from phonenumbers import parse
from phonenumbers import geocoder
from phonenumbers import carrier

unumber = input("Please Enter Some Phone Number : ")
number = parse(unumber)
print(geocoder.description_for_number(number,'en'))
print(carrier.name_for_number(number,'en'))
