from Components import ISS
from Components import Where_Am_I
from Components import Astrolabe
from Components import ImageOfDay

test_1 = ISS.ISS()
print(test_1.welcome)
print(test_1.response)
print(test_1.iss_time)
print(test_1.whos_aboard())
print(test_1.position())
print(test_1.verify())

test_2 = Where_Am_I.Where_am_I()
print(test_2.current_location_name())
print(test_2.coordinates())

test_3 = Astrolabe.Astrolabe()
print(test_3.distance_km())
print(test_3.match())
print(test_3.compass_ISS())
print(test_3.iss_country())

test_4 = ImageOfDay.ImageOfDay()
print(test_4.validate_key())
print(test_4.get_image())
print(test_4.get_explanation())
