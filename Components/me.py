import geocoder
from datetime import datetime
import time

class Where_am_I():

    def __init__(self, nome):
        self.nome = nome
        self.current_time = datetime.now().strftime('%H:%M:%S')

    def current_location_name (self):
        return geocoder.ip('me')
    
    def coordinates(self):
        self.latitude = geocoder.ip('me').lat
        self.longitude = geocoder.ip('me').lng

        return self.latitude , self. longitude