#dependencies
import requests
from datetime import datetime
import smtplib
import time

#constants
MY_LAT = 51.507351 # Your latitude
MY_LONG = -0.127758 # Your longitude
my_email = "CENSORED"
app_pw = "CENSORED"
destination = "CENSORED"
msg = "Go outside and see the ISS."

#functions
#Your position is within +5 or -5 degrees of the ISS position.
def check_iss_pos(iss_lat,iss_lng):
    lat=False
    lng=False
    if iss_lat > MY_LAT-5 and iss_lat < MY_LAT + 5:
        lat = True
    if iss_lng > MY_LONG-5 and iss_lng < MY_LONG + 5:
        lng = True
    if lat and lng:
        return True
    else:
        return False

def check_night(sr,ss,curr):
    if curr < sr or curr > ss:
        return True
    else:
        return False

def send_email(message,address):
    with smtplib.SMTP("smtp.gmail.com",port=587) as connection:
        connection.starttls()
        connection.login(user = my_email, password = app_pw)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=f"{address}",
            msg=f"Subject:ISS OVERHEAD\n\n{message}")

run = True
while  run == True:
    #get ISS location from API
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()
    
    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])
    
    
    #get sunrise and sunset data from API
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }
    
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
    
    
    
    
    #-------------------send email
    
    time_now = datetime.now()
    #If the ISS is close to my current position
    if  check_iss_pos(iss_latitude,iss_longitude):
    # and it is currently dark
        if check_night(sunrise,sunset,time_now.hour):
    # Then send me an email to tell me to look up.
            send_email(msg,destination)
    # BONUS: run the code every 60 seconds.
    time.sleep(60)


