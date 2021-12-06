# Final Project Checkpoint #2
# CS 101: Checkpoint 2
# Filename: checkpoint2.py
#
# Name: John (Jack) Ambery
# Using a program to retrieve data from an API

import json
import requests

response = requests.get("https://api.nasa.gov/planetary/apod/?api_key=qGPdOISKXp8YG2vqUX5KK9WjwVlelOIFqwWl29fx")

image = json.loads(response.text)

print("Data:", image)

