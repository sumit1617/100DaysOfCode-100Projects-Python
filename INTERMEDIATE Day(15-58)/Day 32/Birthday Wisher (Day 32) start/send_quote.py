import smtplib
import datetime as dt
import random


my_email = "sumitkumarsingh1817@gmail.com"
password = "sumit@1806"


now = dt.datetime.now()
weekday = now.weekday()
if weekday == 2:
    with open("quotes.txt") as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)


    print(quote)
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="milanrajani33@gmail.com",
            msg=f"Subject:Wednesday Motivation\n\n{quote}"
        )



# sahilsalian252002@gmail.com
# gargkrishna730@gmail.com
# sand.karan.kumar2003@gmail.com
# byadav.bipin@gmail.com