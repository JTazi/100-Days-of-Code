# -*- coding: utf-8 -*-
"""
Created on Tue Mar 19 10:48:07 2024

@author: jtazioli
"""

from flight_data import check_flights 
from sheety_data import get_locations_prices
from send_text import send_text

locs_prices_lst = get_locations_prices()

for loc,price in locs_prices_lst:
    flight_results = check_flights(loc,price)
    if flight_results['_results']>0:
        text = (f"""{flight_results['data'][0]['cityFrom']}, 
{flight_results['data'][0]['cityTo']}, 
{flight_results['data'][0]['utc_departure']}, 
{flight_results['data'][0]['utc_arrival']}, 
${flight_results['data'][0]['price']}""")

        send_text([text])
        with open('flights.txt','a') as f:
            f.write(str(flight_results['data']))
    else:
        print("no flights found")