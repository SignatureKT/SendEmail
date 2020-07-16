from email.message import EmailMessage
import os, smtplib, sys

#Set environment variable or Enter string to use
EMAIL_ADDRESS = os.environ.get('MAIL_TEST') if os.environ.get('MAIL_TEST') else ''
EMAIL_PASSWORD = os.environ.get('PASSWORD_TEST') if os.environ.get('PASSWORD_TEST') else ''

fileDir = './emailFile'
if not os.path.isdir(fileDir):
    os.mkdir(fileDir)

#Add to this list the messages to different emails
emailList = []
#Add to the subject of the email
subject = 'Your Subject'
#Add to the body of the email
body = 'Your Body'
for index in range(len(emailList)):
    msg = EmailMessage()
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = email
    with open(f'{fileDir}/subject.txt', 'w+') as f:
        f.write(subject)
        msg['Subject'] = f.read()
    with open(f'{fileDir}/body.txt', 'w+') as f:
        f.write(body)
        msg.set_content(f.read())
        
    #sends the message 
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
        server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        
        server.send_message(msg)
        server.close()
