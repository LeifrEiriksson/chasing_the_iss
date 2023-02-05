import geocoder
import geopy
import math
from geopy.geocoders import Nominatim
import haversine 
from haversine import Unit
from Components import ISS
from Components import Where_Am_I

class Astrolabe(ISS.ISS, Where_Am_I.Where_am_I):
    
    def __init__(self):
        super().__init__()


    def distance_km(self):   
       return round((haversine.haversine(self.position(),self.coordinates(), unit = Unit.KILOMETERS)),2)


    def match(self):

        if self.distance_km() <= 100:
            return "Are you aboard?"
        elif self.distance_km() <= 250:
            return "The ISS is really closer you!"
        elif self.distance_km() <= 500:
            return "The ISS is approaching!"
        elif self.distance_km() <= 650:
            return "The ISS is approaching!"
        elif self.distance_km() <= 1000:
            return "I think I saw something in the sky"
        else:
            return "The ISS is so far..."


    def compass_ISS(self):

        self.lat_iss =  self.long_iss = None

        if self.position()[0] > 0:
            self.lat_iss = "North"
        else:
            self.lat_iss = "South"

        if self.position()[1] > 0:
            self.long_iss =  "East"
        else:
            self.long_iss = "West"

        return f"ISS - Lat_issitude: {self.lat_iss} and Longitude: {self.long_iss}"

    def iss_country(self):
        
        try:
            self.geolocation = Nominatim(user_agent="geoapiExercises")
            self.location = self.geolocation.reverse(str(self.position()[0])+","+str(self.position()[1])).raw['address']
            return self.location

        except:
            return "Did the ISS enter a black hole?"