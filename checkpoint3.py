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
    image = json.loads(response.text)
    print("Data:", image)
    webbrowser.open(image['url'])

def printKeys():
    print("keys")

def printVals():
    print("vals")

#example of a menu
def menu():
    print("select 1 for keys")
    print("select 2 for values")
    print("select 3 to quit")


def main():
    getData()

    menu()
    userSelection = int(input("Please make a selection:\n"))
    if userSelection == 1:
        printKeys()
    elif userSelection == 2:
        printVals()

if __name__ == "__main__":
    main()

