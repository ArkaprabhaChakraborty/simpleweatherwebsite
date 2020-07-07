import requests
import json
from flask import Flask, request, redirect , url_for , render_template
import urllib.request
import os


access  = "1f134b83b86790053df58f4222a205c8"



'''
api_response = api_result.json()
print(api_response)
'''

app = Flask(__name__)

@app.route("/", methods = ["GET","POST"])
def home():
    return render_template("index.html")

@app.route("/weatherupdate", methods = ["GET","POST"])
def weather():
    city = request.form.get('city')
    params = {
      'access_key': access,
      'query': city}
    api_result = requests.get('http://api.weatherstack.com/current', params)
    api_result = api_result.json()
    name = api_result['location']['name']
    country = api_result['location']['country']
    region = api_result['location']['region']
    lat = api_result['location']['lat']
    lon = api_result['location']['lon']
    time = api_result['location']['localtime']
    temp = api_result['current']['temperature']
    icon = api_result['current']['weather_icons']
    ic = str(icon).replace("['","")
    ic = ic.replace("']","")
    img_url = ic
    img_name = "/home/arkaprabha/Desktop/simpleweatherwebsite/theweatherapp/static/images/local-filename.png"
    urllib.request.urlretrieve(img_url,img_name)
    des = str(api_result['current']['weather_descriptions'])
    des = des.replace("['","")
    des = des.replace("']","")
    wind = api_result['current']['wind_speed']
    wind_degree = api_result['current']['wind_degree']
    wind_dir = api_result['current']['wind_dir']
    pressure = api_result['current']['pressure']
    precip = api_result['current']['precip']
    humid = api_result['current']['humidity']
    cc = api_result['current']['cloudcover']
    feels = api_result['current']['feelslike']
    vis = api_result['current']['visibility'] 
    return render_template("weather.html",temp  = temp, cc = cc,name = name,precip = precip,wind = wind,feels = feels,des = des,wind_dir = wind_dir,time = time, country = country,lat = lat, lon  = lon, wind_degree = wind_degree,pressure = pressure,humid = humid,vis = vis,region  = region)
if __name__ == "__main__":
    app.run(debug=True)
