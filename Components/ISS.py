import requests
import json
from datetime import datetime
import time

class ISS():

    def __init__ (self):
        self.welcome = "Ladies and Gentlemen, welcome aboard the ISS!"
        self.response = requests.get("http://api.open-notify.org/iss-now.json").json() 
        self.iss_time = datetime.fromtimestamp(self.response['timestamp']).strftime('%H:%M:%S')


    def verify(self):
        if self.response['message'] ==  'success':
           return "Sucess! We're floating in space!"

        else:
           return "Ladies and Gentlemen, we're out of orbit!"

    def whos_aboard (self):
        return [names['name'] for names in requests.get("http://api.open-notify.org/astros.json").json()['people'] if names['craft'] == 'ISS']

    def position (self):
        self.iss_latitude = float(self.response['iss_position']['latitude'])
        self.iss_longitude = float(self.response['iss_position']['longitude'])

        return self.iss_latitude , self.iss_longitude 
