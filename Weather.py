from datetime import datetime

import requests

import os

api_key = '339f56268cde62d357b8da718cc08c77'  #From the openweather website
location = input("Enter the city name: ")
#Creating a .txt file with the name given by user
fileName = input("Give a Filename: ") +  ".txt"
complete_api_link = "https://api.openweathermap.org/data/2.5/weather?q="+location+"&appid="+api_key
api_link = requests.get(complete_api_link)
api_data = api_link.json()

#create variables to store and display data
temp_city = ((api_data['main']['temp']) - 273.15)
weather_desc = api_data['weather'][0]['description']
hmdt = api_data['main']['humidity']
wind_spd = api_data['wind']['speed']
date_time = datetime.now().strftime("%d %b %Y | %I:%M:%S %p")

print ("-------------------------------------------------------------")
print ("Weather Stats for - {}  || {}".format(location.upper(), date_time))
print ("-------------------------------------------------------------")

print ("Current temperature is: {:.2f} deg C".format(temp_city))
print ("Current weather desc  :",weather_desc)
print ("Current Humidity      :",hmdt, '%')
print ("Current wind speed    :",wind_spd ,'kmph')

# The following two lines can be used to create a .txt file in PC with the content directly from the website link (in api format)
#with open('weather report.txt','wb') as file:
 #   file.write(api_link.content)

# Only useful(the info we want) info is given to the .txt file
myFile = open(fileName,'w')
myFile.write("Date & Time           :" + format(date_time))
myFile.write("\n")
myFile.write("Name of the City      :" + location.upper())
myFile.write("\n")
myFile.write("Current temperature is: " + format(temp_city,".2f") + " deg C")
myFile.write("\n")
myFile.write("Current weather desc  : " + weather_desc)
myFile.write("\n")
myFile.write("Current Humidity      : " + str(hmdt) + "%")
myFile.write("\n")
myFile.write("Current wind speed    : " + str(wind_spd) + "kmph")
myFile.close()  #Closing the file

os.startfile(fileName) # Opening(Displaying) the .txt file
# Instaed of displaying, this .txt file can be seen in our PC