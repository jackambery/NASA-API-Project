
import config
import json
import requests
import webbrowser

class Picture:

    def __init__(self, month, day, year):
        
        # default day is today, triggered by date: 0/0/0
        if day == 0:
            response = requests.get("https://api.nasa.gov/planetary/apod/?api_key=" + config.API_KEY)
        
        else:
            response = requests.get("https://api.nasa.gov/planetary/apod/?api_key=" + config.API_KEY + "&date=" + str(year) + "-" + str(month) + "-" + str(day))

        self.data = json.loads(response.text)

    def __repr__(self):
        pass

    def printKeys(self):
        print(self.data.keys())

    def printVals(self):
        print(self.data.values())

    def openImage(self):
        webbrowser.open(self.data['url'])

    def getPhotographer(self):
        try:
            return(self.data['copyright'])
        except Exception as e:
            return "No photographer found."

    def getTitle(self):
        try:
            return(self.data['title'])
        except Exception as e:
            return "No title found."