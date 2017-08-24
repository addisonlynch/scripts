#! /usr/bin/env python

import smtplib
import getpass


print("EMAIL DAEMON. WORKS FOR GMAIL ONLY\n\n")



#send email with simple text
def simple_message(send_from, send_to, msg):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    pwd = getpass.getpass("Enter your password for " + send_from + ": ")
    server.login(send_from, pwd)
    server.sendmail(send_from, send_to, msg)
    server.quit()


from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from email.MIMEBase import MIMEBase
from email import encoders


    
#send email with subject and attachment
def complex_message(send_from, send_to, subject, msg, att):
    mesg = MIMEMultipart()
    mesg['From'] = send_from
    mesg['To'] = send_to
    mesg['Subject'] = subject
    body  = msg

    mesg.attach(MIMEText(body, 'plain'))

    filename = "simple.py"
    attachment = open(att, "rb")

    part = MIMEBase('application', 'octet-stream')
    part.set_payload((attachment).read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', "attachment; filename = %s" % filename)
    mesg.attach(part)

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    pwd = getpass.getpass("Enter your password for " + send_from + ": ")
    server.login(send_from, pwd)
    text = mesg.as_string()
    server.sendmail(send_from, send_to, text)
    server.quit()
    

def main():

   # simple_message("ahlshop@gmail.com", "ahlshop@gmail.com", "hello world")
    complex_message("ahlshop@gmail.com", "willemvdb7@gmail.com", "Email attachment program", "Attached. Two functions, one for a simple message and one for a message with a subject and attachments. You may need to remove the shebang (#! /usr/bin/env python) first line to get the script to run on windows. (This message was sent from the script itself)", "./simple.py")
    

if __name__ == "__main__":
    main()





