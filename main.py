import smtplib
from Fetcher import Fetcher
from email.message import EmailMessage
from confidential import *
from variables import *


server = smtplib.SMTP('smtp.gmail.com' ,587)
server.starttls()
server.login(EMAIL, KEY)

fetcher=Fetcher()

guardianHeadlines=fetcher.getGuardianHeadlines()
aljazeeraHeadlines=fetcher.getAlJazeeraHeadlines()
printHeadlines=fetcher.getPrintHeadlines()
toiHeadlines=fetcher.getTOIHeadlines()

mail = EmailMessage()
mail['Subject'] = "Here are today's headlines"
mail['from'] = EMAIL

for i in subscribers.keys():

    mail['to']=i

    content="""\n"""

    if ALJAZEERA in subscribers[i]:
        content+="Here are the headlines from Al Jazeera:\n"
        for j in aljazeeraHeadlines.keys():
            content=content+j+": "+aljazeeraHeadlines[j]+"\n"
        content+="\n"

    if GUARDIAN in subscribers[i]:
        content+="Here are the headlines from The Guardian:\n"
        for j in guardianHeadlines.keys():
            content=content+j+": "+guardianHeadlines[j]+"\n"
        content+="\n"

    if PRINT in subscribers[i]:
        content+="Here are the headlines from The Print:\n"
        for j in printHeadlines.keys():
            content=content+j+": "+printHeadlines[j]+"\n"
        content+="\n"

    if TOI in subscribers[i]:
        content+="Here are the headlines from The Times of India:\n"
        for j in toiHeadlines.keys():
            content=content+j+": "+toiHeadlines[j]+"\n"
        content+="\n"

    print(content)
    mail.set_content(content)
    server.send_message(mail)
    print('Mail sent to ',i)

    del mail['to']

server.quit()
