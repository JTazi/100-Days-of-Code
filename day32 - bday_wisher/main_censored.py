#python_emailer

# import smtplib

# my_email = "CENSORED"
# app_pw = "CENSORED"

# with smtplib.SMTP("smtp.gmail.com",port=587) as connection:
#     connection.starttls()
#     connection.login(user = my_email, password = app_pw)
#     connection.sendmail(
#         from_addr=my_email,
#         to_addrs="CENSORED",
#         msg="Subject:Python Emailer\n\nHello World!")


# import datetime as dt

# #returns current datetime
# now = dt.datetime.now()
# #2024-01-12 09:26:28.498449

# #returns int year
# print(now.year)

# #create custom datetime object
# date_of_birth = dt.datetime(year=1996,month=6,day=15,hour=8)
# print(date_of_birth)

"""OBJECTIVE: send a motivational quote via email on the current weekday (eventually set to monday)"""
#Hints:
    #1. use datetime module to opbtain the current day of the week
    #2. open quotes.txt file and obtain a list of quotes
    #3. use random module to pick a random quote from your list of quotes
    #4. use smtplib to send email to yourself
    
import datetime as dt
import smtplib
from random import randint

#--------------------get list of quotes
with open("quotes.txt", 'r') as f:
    quotes_list = f.readlines()
    
todays_quote = quotes_list[randint(0,len(quotes_list)-1)]
# print(quotes_list[0])

#--------------------get todays day
now = dt.datetime.now()
current_weekday = now.weekday()

#-------------------send email
my_email = "CENSORED"
app_pw = "CENSORED"

def send_quote(quote):
    with smtplib.SMTP("smtp.gmail.com",port=587) as connection:
        connection.starttls()
        connection.login(user = my_email, password = app_pw)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="CENSORED",
            msg=f"Subject:Motivation\n\n{quote}")


#----------------------test date and send email if right

if current_weekday == 4:
    send_quote(todays_quote)
