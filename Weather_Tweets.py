#!/usr/bin/env python
# coding: utf-8

# In[10]:


# Dependencies
import tweepy
import time
import json
import random
import requests as req
import datetime
from config import consumer_key, consumer_secret, access_token, access_token_secret, weather_api_key


# In[11]:


# Twitter API Keys
consumer_key = consumer_key
consumer_secret = consumer_secret
access_token = access_token
access_token_secret = access_token_secret


# In[ ]:


# Weather API Key


# In[12]:


print(query_url)


# In[15]:


# Create a function that gets the weather in London and Tweets it
def WeatherTweet():

    # Construct a Query URL for the OpenWeatherMap
    url = "http://api.openweathermap.org/data/2.5/weather?"
    city = "Washington, D.C."
    units = "imperial"
    query_url = url + "appid=" + weather_api_key + "&q=" + city + "&units=" + units

    print(query_url)

    weather_response = req.get(query_url)
    weather_json = weather_response.json()
    print(weather_json)
# Get the temperature from the response

#print(f"The weather API responded with: {weather_json}.")
    # Twitter credentials


    # Tweet the weather


    # Print success message


# In[ ]:


# Set timer to run every 1 hour


# In[ ]:




