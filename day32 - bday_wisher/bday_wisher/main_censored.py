##################### Extra Hard Starting Project ######################
import pandas as pd
import datetime as dt
from random import randint
import smtplib

#-------------------send email
my_email = "CENSORED"
app_pw = "CENSORED"

def send_email(message,address):
    with smtplib.SMTP("smtp.gmail.com",port=587) as connection:
        connection.starttls()
        connection.login(user = my_email, password = app_pw)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=f"{address}",
            msg=f"Subject:Happy Birthday!\n\n{message}")

# 1. Update the birthdays.csv
df = pd.read_csv('birthdays.csv')
birthdays = df.to_dict('records')
#dict format: [{'name':asdf},{'email':asdf},{'year':asdf},{'month':asdf},{'day':asdf}]

# 2. Check if today matches a birthday in the birthdays.csv
now = dt.datetime.now()
current_month,current_day = now.month,now.day

#empty list to store birthday email recipients
birthday_data = []
 

for record in birthdays:
    if current_month == record['month'] and current_day == record['day']:
        birthday_data.append((record['name'],record['email']))

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
for name,email in birthday_data:
    #select template
    template = str(randint(1,3))
    with open(f'letter_templates/letter_{template}.txt','r') as temp:
        message = temp.read()
        
    custom_message = message.replace('[NAME]',name)
    
    # 4. Send the letter generated in step 3 to that person's email address.
    send_email(custom_message,email)
