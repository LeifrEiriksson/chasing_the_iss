import json
import time
from datetime import datetime

import requests


class Iss():

    def __init__ (self):

        self.response = requests.get("http://api.open-notify.org/iss-now.json").json() 
        self.iss_time = datetime.fromtimestamp(self.response['timestamp']).strftime('%H:%M:%S')


    def whos_aboard (self):

        if self.resonse["message"] == "success": 

            return [names['name'] for names in requests.get("http://api.open-notify.org/astros.json").json()['people'] if names['craft'] == 'ISS']
        
        else:

            return "Out of orbit."

    def position_iss (self):

        self.iss_latitude = float(self.response['iss_position']['latitude'])
        
        self.iss_longitude = float(self.response['iss_position']['longitude'])

        self.lat_iss = "North" if self.iss_latitude > 0 else "South"

        self.long_iss =  "East" if self.iss_longitude > 0 else "West"


        return self.lat_iss, self.iss_latitude , self.long_iss, self.iss_longitude 
    
    def iss_complete_location(self):
        
        try:

            self.geolocation = Nominatim(user_agent="geoapiExercises")

            self.location = self.geolocation.reverse(str(self.position()[0])+","+str(self.position()[1])).raw['address']

            return self.location     

        except:
            
            return "Did the ISS enter a black hole?"
        
    def iss_country(self):

        self.contry_loc = None

        self.country_loc = self.iss_complete_location()['country'] if 'country' in self.iss_complete_location() else "--"

        return self.country_loc