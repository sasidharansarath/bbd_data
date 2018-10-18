#!/usr/bin/env python
# coding: utf-8

# In[11]:


# https://api.darksky.net/forecast/[key]/[latitude],[longitude],[time]

import json, urllib
import datetime # https://docs.python.org/2/library/datetime.html
import requests # http://docs.python-requests.org/en/master/user/quickstart/
import pandas as pd
from pandas import Series, DataFrame
# from geopy.geocoders import Nominatim # https://pypi.org/project/geopy/

api_key = "e2bdab8f57436bcf7b634998ab5e3fa2" # https://darksky.net/dev/account


Berlin = [52.5143,13.3227] # https://www.gps-coordinates.net/
 
dt = datetime.datetime(2018,10,17,12,0,0)

timestamp = (dt - datetime.datetime(1970,1,1,0,0,0)).total_seconds() # https://www.tutorialspoint.com/How-to-convert-Python-date-to-Unix-timestamp

par = {'units':'si'}

url = "https://api.darksky.net/forecast/"+str(api_key)+"/"+str(Berlin[0])+","+str(Berlin[1])+","+str(int(timestamp))

weather = requests.get(url, params = par)

w_data = weather.json()

w_df = pd.DataFrame(w_data['hourly']['data'])

reqd_data = w_df[['time','apparentTemperature','humidity','cloudCover','summary']]

reqd_data['time_std'] = reqd_data['time'].apply(lambda x: datetime.datetime.utcfromtimestamp(int(x)))

reqd_data1 = reqd_data[['time_std','apparentTemperature','humidity','cloudCover','summary']]

print 'Latitude: ',Berlin[0],"",'Longitude: ',Berlin[1]
print
print 'InputDateTime: ', dt
print
print 'InputUNIXtime: ', int(timestamp)
print
print weather.url
print
print w_df.columns
print
print reqd_data1

if False:
    reqd_data1.to_csv(r"C:\Users\Sarath Sasidharan\Desktop\Required Weather Data.csv", index = None)


# In[ ]:




