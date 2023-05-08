from io import BytesIO

import requests
from PIL import Image


class ImageOfDay():

    def __init__(self):
        self.about = "Welcome to the image of Day, by NASA."
        self.request = None

    def validate_key(self):
        self.answer = None
        self.key_nasa = None

        negative, positive = ["No", "no", "N", "n"], ["Yes", "yes", "Y", "y"]

        while self.answer not in negative or positive:
            self.answer = input("Do you have a Key? (Y/N)")

            if self.answer in negative:
                self.request = requests.get(
                    f"https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY").json()
                return "Now you're using the default Key (DEMO_KEY): \nHourly Limit: 30 requests per IP address per hour. \nDaily Limit: 50 requests per IP address per day."
                break

            elif self.answer in positive:
                self.key_nasa = input("Please, enter the key:")
                self.request = requests.get(
                    f"https://api.nasa.gov/planetary/apod?api_key={self.key_nasa}").json()
                break

            print("Please, answer correctly, Cosmonaut!")

    def get_image(self):
        if self.request != None:
            return requests.get(self.request['hdurl']), Image.open(BytesIO(requests.get(self.request['hdurl']).content)).show()
        else:
            print("Please, validate the key:")
            return self.validate_key(), requests.get(self.request['hdurl']), Image.open(BytesIO(requests.get(self.request['hdurl']).content)).show()

    def get_explanation(self):
        if self.request != None:
            return self.request['title'], self.request['explanation']
        else:
            print("Please, validate the key:")
            return self.validate_key(), self.request['title'], self.request['explanation']
