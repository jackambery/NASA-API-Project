# Final Project for CS101 Intro to Computing
# Name: John (Jack) Ambery
# Filename: NASAPicOfTheDay.py
#
# Using a program to retrieve data from an API and implements a looping menu
#
# This project is for Introduciton to Computing Final Project

import json
import requests
import webbrowser
import config

def getData():
    response = requests.get("https://api.nasa.gov/planetary/apod/?api_key=" + config.API_KEY)
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

def askForDate():
    day = input("What is the day you would like? (8th = 08, 23rd = 23)\n")
    month = input("What is the month you would like? (March = 03)\n")
    year = input("What is the year you would like?\n")
    return day + "/" + month + "/" + year

#very basic menu
def menu():
    # print("Select 1 for keys")
    # print("Select 2 for values")
    print("Select 1 to open today's image of the day online")
    print("Select 4 to see the details of today's image")
    print("Select 3 to enter your own day")
    print("Select 0 to quit")

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
        print("\n")


def main():
    data = getData()
    process(data)

if __name__ == "__main__":
    main()

