#!/usr/bin/python3

import requests
  
URL= 'http://api.open-notify.org/iss-now.json'
def main():
    # requests.get() sends GET request to the URL
    # .json() strips JSON off the response and translates into Python!
    resp= requests.get(URL).json()
    # print(resp)

    print(f"CURRENT LOCATION OF THE ISS: Lon: {resp['iss_position']['longitude]} Lat: {resp['iss_position']['latitude']}")
main()

