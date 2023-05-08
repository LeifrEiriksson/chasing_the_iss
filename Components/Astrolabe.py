import geocoder
import geopy
import haversine
from geopy.geocoders import Nominatim
from haversine import Unit

from Components.InternationalSpaceStation import Iss
from Components.My_Location import Where_Am_I


class Astrolabe(Iss, Where_Am_I):

    def __init__(self):

        super().__init__()

    def distance_km(self):

        return round((haversine.haversine(self.position(), self.coordinates(), unit=Unit.KILOMETERS)), 2)

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

        self.lat_iss = self.long_iss = None

        self.lat_iss = "North" if self.position()[0] > 0 else "South"
        self.long_iss = "East" if self.position()[1] > 0 else "West"

        return f"ISS - Lat_issitude: {self.lat_iss} and Longitude: {self.long_iss}"

    def iss_complete_location(self):

        try:
            self.geolocation = Nominatim(user_agent="geoapiExercises")
            self.location = self.geolocation.reverse(
                str(self.position()[0])+","+str(self.position()[1])).raw['address']
            return self.location

        except:
            return "Did the ISS enter a black hole?"

    def iss_country(self):

        self.contry_loc = None

        self.country_loc = Astrolabe().iss_complete_location(
        )['country'] if 'country' in self.iss_complete_location() else "--"

        return self.country_loc
