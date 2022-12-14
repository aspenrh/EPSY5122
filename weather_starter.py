import urllib.request
import urllib.parse
import json
# Adapted from Python for Everyone (Horstmann & Necaise)

# Sign up for an Open Weather account:
# https://home.openweathermap.org/users/sign_up
# go to API keys, copy and paste

# API stands for Application Programming Interface
# It is the way that data can be transferred between programs
# In this case, we are going to pull data from a website (Open Weather)
#   into our Python programming environment

# ask user for the name of the location
city1 = input("Enter the name of a city: ")
city2 = input("Enter the name of another city: ")
city3 = input("Enter the name of yet another city: ")

# write the URL
params1 = {"appid":"1d20f16c25f2e32a35903a57a0a86f6d", "q": city1, "units": "imperial"}
arguments1 = urllib.parse.urlencode(params1) # convert params to a URL encoding


#print(arguments) # ever see this in a URL??? anything after a "?" is a parameter

# retrieve weather information
address = "http://api.openweathermap.org/data/2.5/weather"
url1 = address + "?" + arguments1 # see!

print(url1)

webData = urllib.request.urlopen(url1) # Open a connection to URL
results1 = webData.read().decode('UTF-8')
webData.close() # CLOSE THE CONNECTION!

# convert JSON to a Python dictionary
data1 = json.loads(results1)



params2 = {"appid":"1d20f16c25f2e32a35903a57a0a86f6d", "q": city2, "units": "imperial"}
arguments2 = urllib.parse.urlencode(params2) # convert params to a URL encoding


#print(arguments) # ever see this in a URL??? anything after a "?" is a parameter

# retrieve weather information
address = "http://api.openweathermap.org/data/2.5/weather"
url2 = address + "?" + arguments2 # see!

print(url2)

webData = urllib.request.urlopen(url2) # Open a connection to URL
results2 = webData.read().decode('UTF-8')
webData.close() # CLOSE THE CONNECTION!

# convert JSON to a Python dictionary
data2 = json.loads(results2)


params3 = {"appid":"1d20f16c25f2e32a35903a57a0a86f6d", "q": city3, "units": "imperial"}
arguments3 = urllib.parse.urlencode(params3) # convert params to a URL encoding


#print(arguments) # ever see this in a URL??? anything after a "?" is a parameter

# retrieve weather information
address = "http://api.openweathermap.org/data/2.5/weather"
url3 = address + "?" + arguments3 # see!

print(url3)

webData = urllib.request.urlopen(url3) # Open a connection to URL
results3 = webData.read().decode('UTF-8')
webData.close() # CLOSE THE CONNECTION!

# convert JSON to a Python dictionary
data3 = json.loads(results3)

# print(data['main']['temp'])

print("The current temperature in", city1, "is", data1["main"]["temp"], "F.")
print("The current temperature in", city2, "is", data2["main"]["temp"], "F.")
print("The current temperature in", city3, "is", data3["main"]["temp"], "F.")

print("The current humidity in", city1, "is", data1["main"]["humidity"], "percent.")
print("The current humidity in", city2, "is", data2["main"]["humidity"], "percent.")
print("The current humidity in", city3, "is", data3["main"]["humidity"], "percent.")

print("It currently feels like", data1["main"]["feels_like"], "F in", city1)
print("It currently feels like", data2["main"]["feels_like"], "F in", city2)
print("It currently feels like", data3["main"]["feels_like"], "F in", city3)
