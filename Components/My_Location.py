import time
from datetime import datetime

import geocoder
import geopy
from geopy.geocoders import Nominatim


class Where_am_I():

    def __init__(self, nome=None):
        
        self.nome = nome
        self.current_time = datetime.now().strftime('%H:%M:%S')

    def current_location_name (self):

        return geocoder.ip('me')
    
    def my_coordinates(self):

        self.latitude = geocoder.ip('me').lat
        self.longitude = geocoder.ip('me').lng

        return self.latitude , self.longitude
    
