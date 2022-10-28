from subprocess import call
import time
import os
import glob
import smtplib
import base64
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText  
import sys



username="Ann Lia"   #insert your username
password="pass@248"  #insert your password
userinput=input("Enter your username:")
if userinput==username:
    passinput=input("Enter your password:") 
    if passinput==password:
        print("Thank you for logging in!")
    else:
            gmail_user = "iotdemopan@gmail.com"
            gmail_pwd = "Pantechiot@2021"
            FROM = 'iotdemopan@gmail.com'
            TO = ['annliajeejo08@gmail.com'] #insert your mail id

            msg = MIMEMultipart()
            time.sleep(1)
            msg['Subject']="SECURITY BREACH"

            body="SOMEONE TRIED TO LOGIN TO YOUR ACCOUNT AND FAILED"
            msg.attach(MIMEText(body,'plain'))
            time.sleep(1)

            try:
                server = smtplib.SMTP("smtp.gmail.com",587) #or port 465 doesn't seem to work!
                print ("smtp.gmail")
                server.ehlo()
                print("ehlo")
                server.starttls()
                print("starttls")
                server.login(gmail_user, gmail_pwd)
                print("reading mail & password")
                server.sendmail(FROM, TO, msg.as_string())
                print("from")
                server.close()
                print("successfully sent the mail")
            except:
                print("failed to send mail")

else:
    print('You are not registered in our database.')

                
    
