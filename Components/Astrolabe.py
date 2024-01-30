import geocoder
import geopy
import haversine
from geopy.geocoders import Nominatim
from haversine import Unit

from Components.InternationalSpaceStation import Iss
from Components.My_Location import Where_Am_I


class Astrolabe(Iss, Where_am_I):
    
    def __init__(self):

        super().__init__()

    def distance_km(self):   

       return round((haversine.haversine(self.position_iss(),self.my_coordinates(), unit = Unit.KILOMETERS)),2)
    