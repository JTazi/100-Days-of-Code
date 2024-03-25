# -*- coding: utf-8 -*-
"""
Created on Wed Jan 24 11:48:58 2024

@author: jtazioli
"""
import requests as re

KIWI_URL = "https://api.tequila.kiwi.com/"

LOCATION_ENDPOINT = "v2/search"
KIWI_HEADER = {
    "accept": "application/json",
    "apikey":"bUPz9MqTjNd2jngKUHVhIZdjAQj7NSzG"}

# 'BJS,LON,ROM,SEL,TYO'
def check_flights(iata_code,price):
    #step1 is to get location IDs using locations api
    
    loc_params = {
            'fly_from':'ORD',
            'fly_to':iata_code,
            'date_from':'19/03/2024',
            'date_to':'19/07/2024',
            'nights_in_dst_from':6,
            'nights_in_dst_to':7,
            'ret_from_diff_city':False,
            'ret_to_diff_city':False,
            'one_for_city':1,
            'one_per_date':0,
            'adults':1,
            'children':0,
            'adult_hold_bag':1,
            'adult_hand_bag':1,
            'only_working_days':False,
            'only_weekends':False,
            'partner_market':'us',
            'curr':'USD',
            'locale':'en',
            'price_to':price,
            'max_stopovers':2,
            'max_sector_stopovers':2,
            'vehicle_type':'aircraft',
            'limit':20
        }
    
    #returns JSON of "locations":["id","name"]
    response = re.get(url=f"{KIWI_URL}{LOCATION_ENDPOINT}",headers=KIWI_HEADER,params=loc_params)
    return response.json()
    # loc_code = (response.json()["locations"]["id"],response.json()["locations"]["name"])
    # print(loc_code)
    
    #step2 use location IDs to search for flights using search API
    