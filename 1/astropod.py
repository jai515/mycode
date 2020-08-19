#!/usr/bin/env python3

import requests
import wget

# Accepts input from the user in format of YYY-MM-DD. This will be the date of the APOD you access!
user_date = input("Please enter a date after Jun 16, 1995 in the form of YYYY-MM-DD: ")
# Asks input from the user if they would like their image in High Definition or Standard Definition.
user_definition = input("Would you like an image in High Definition? (y/n) ").strip().lower()
is_hd = True if user_definition == "y" else False

# Concatenates the API URL which includes:
# Your own API key.
api_key = "MKoq4eDEGYINeuccIMzGyuC8Cn066AxNldEpEFgk"
# The date of the Astronomical Picture of the Day you'd like to access.
# Final URL should look something like this:
nasa_url =  f"https://api.nasa.gov/planetary/apod?date={user_date}&hd={is_hd}&api_key={api_key}"

# Uses the requests library to return and translate JSON.
nasa_response = requests.get(nasa_url).json()
# From the translated JSON, return the following:

date = nasa_response['date']
# Date of the picture
# Title of the picture
title = nasa_response['title']
# The text describing what the picture is all about.
description = nasa_response['explanation']
# From the translated JSON, use the wget library (or another library if you prefer)
# to download EITHER the HD image or the SD image depending on the user's input from earlier.
# This page shows you how to use wget: (https://likegeeks.com/downloading-files-using-python/#Using-wget)
hdurl = nasa_response['hdurl']
potatourl = nasa_response['url']
if is_hd is True:
    wget.download(hdurl, './')
else:
    wget.download(potatourl, './')
#
# Back up to GitHub (including the picture you downloaded), then access the picture on GitHub to bask in its cosmological beauty.

