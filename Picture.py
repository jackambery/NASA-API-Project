
import config
import json
import requests
import webbrowser

class Picture:

    def __init__(self, month, day, year):

        #sets a standard file for everything to be written to
        self.outFile = "outfile.txt"
        
        # default day is today, triggered by date: 0/0/0
        if day == 0:
            response = requests.get("https://api.nasa.gov/planetary/apod/?api_key=" + config.API_KEY)
        
        else:
            response = requests.get("https://api.nasa.gov/planetary/apod/?api_key=" + config.API_KEY + "&date=" + str(year) + "-" + str(month) + "-" + str(day))

        self.data = json.loads(response.text)

    def __repr__(self):
        return "This is image is \"" + self.getTitle() + "\" by " + self.getPhotographer() + ".\n" + self.getExplanation()

    def openImage(self):
        webbrowser.open(self.data['url'])

    def getTitle(self):
        try:
            return(self.data['title'])
        except Exception as e:
            return "No title found."

    def getPhotographer(self):
        try:
            return(self.data['copyright'])
        except Exception as e:
            return "No photographer found."

    def getExplanation(self):
        try:
            return(self.data['explanation'])
        except Exception as e:
            return "No description found."

    def appendDescription(self):
         with open(self.outFile, "a") as outfile:
             outfile.write(self.__repr__())
