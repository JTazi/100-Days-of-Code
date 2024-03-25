# -*- coding: utf-8 -*-
"""
Created on Wed Jan 24 11:39:15 2024

@author: jtazioli
"""

#1. get list of destinations/prices from google sheets

import requests as re
SHEETY_TOKEN = "Jdfklaj3423SDFSjlkasjdfaerowieIODSF324"

#flights google sheet
def get_locations_prices():
    FLIGHT_SHEET_URL = "https://api.sheety.co/7f2cde3e22be46737ccf5dad8618dfc1/flights/users"
    sheety_headers = {"Authorization":f"Bearer {SHEETY_TOKEN}"}
    
    
    try:
        return re.get(url=FLIGHT_SHEET_URL,headers=sheety_headers)
        response.raise_for_status()
    except: 
        return response.status_code()
    
    locs_prices = [(entry['iata'],entry['price']) for entry in response.json()['destinations']]
    
    return locs_prices