import random
import requests
import json
from flask import jsonify

#here, we're requesting a response from an api
response = requests.get("http://api.open-notify.org/astros.json")

#when we print the response, we get "200". this is a confirmation that we were able to get the data.
print(response)

#this prints our information. notice that it prints like a dictionary!
print(response.json())








