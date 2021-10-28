# Final Project Checkpoint #3
# CS 101: Checkpoint 3
# Filename: checkpoint3.py
#
# Name: John (Jack) Ambery
# Using a program to retrieve data from an API

import json
import requests
import webbrowser

def getData():
    response = requests.get("https://api.nasa.gov/planetary/apod/?api_key=qGPdOISKXp8YG2vqUX5KK9WjwVlelOIFqwWl29fx")
    data = json.loads(response.text)
    return data

def printKeys(data):
    print(data.keys())

def printVals(data):
    print(data.values())

def openImage(data):
    webbrowser.open(data['url'])

def getPhotographer(data):
    return(data['copyright'])

def getTitle(data):
    return(data['title'])

#very basic menu
def menu():
    print("select 1 for keys")
    print("select 2 for values")
    print("select 3 to open today's image of the day online")
    print("select 4 to see who owns the image")
    print("select 5 to see the title of the image")
    print("select 0 to quit")

def process(data):
    while True:
        menu()

        userSelection = int(input("Please make a selection:\n"))
        if userSelection == 1:
            printKeys(data)
        elif userSelection == 2:
            printVals(data)
        elif userSelection == 3:
            openImage(data)
        elif userSelection == 4:
            print(getPhotographer(data))
        elif userSelection == 5:
            print(getTitle(data))
        elif userSelection == 0:
            exit()
        else:
            print("invalid selection")


def main():
    data = getData()
    process(data)

if __name__ == "__main__":
    main()

