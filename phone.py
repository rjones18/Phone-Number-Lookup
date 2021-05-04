import phonenumbers
from numbers import number
from phonenumbers import geocoder
from phonenumbers import timezone

ch_number = phonenumbers.parse(number, 'CH')
print(geocoder.description_for_number(ch_number, 'en'))


gb_number = phonenumbers.parse(number, 'GB')
print(timezone.time_zones_for_number(gb_number))

