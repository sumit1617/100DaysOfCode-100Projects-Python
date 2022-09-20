import smtplib


my_email = "ss5933070@outlook.com"
password = "sumit4734"


with smtplib.SMTP("smtp.outlook.com") as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(from_addr=my_email,
                        to_addrs= "sumrat1806@gmail.com",
                        msg="Hello smtp working")



# https://medium.freecodecamp.org/send-emails-using-code-4fcea9df63f

# import the smtplib module. It should be included in Python by default
# import smtplib
# # set up the SMTP server
# sender_m = "ss59330070@outlook.com"
# password = "sumit4734"
# s = smtplib.SMTP(host='smtp-mail.outlook.com', port=587)
# s.starttls()
# s.login(sender_m, password)
#
# import smtplib
# import time
#
# server = smtplib.SMTP_SSL('host',port=587)
# server.ehlo()
# server.login(sender_m, password)
#
# server.ehlo()
#
# print ('server working fine')
#
# time.sleep(5)
#
# sender = sender_m
#
# receivers = ["shubhamboghara444@gmail.com"]
#
# subject = "SMTP e-mail Test"
#
# msg = "This is an automated message being sent by Python. Python is the mastermind behind    this."
#
# server.sendmail(sender, receivers, subject, msg)
#
# print ('sending email to outlook')
#
# server.quit()