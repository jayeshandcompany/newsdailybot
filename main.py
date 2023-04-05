import requests
from requests import Request
import  smtplib,ssl
from datetime import  datetime
import pytz
IST=pytz.timezone('Asia/Kolkata')
date=str(datetime.now(IST))
mon=datetime.now(IST)
date1=date.split(' ')[0]
y=date1.split('-')[0]
d=date1.split('-')[2]
hour=int((date.split(' ')[1]).split(':')[0])
min=str((date.split(' ')[1]).split(':')[1])
if hour>12:
    hour=hour-12
elif hour==0:
    hour=hour+12
m=mon.strftime("%B")
pdate=f"{d}-{m}-{y}".strip()
sub1=f" Done sir👍 for {pdate}"
th="All the Emails are successfully sent boss!"
success = f"""\
Subject: {sub1}

{th}
"""
success=success.encode('utf-8','ignore').decode()
sender_email="newsbyjayeshbot@gmail.com"

password="************* "

apiKey = "your api key"
key= {
"sortBy": "top",
"apiKey" : "f7a3dc5eadb04968a812681696d393c4"
}
main_url="https://newsapi.org/v2/top-headlines?country=us&apiK"
res=requests.get("https://newsapi.org/v2/top-headlines?country=in&apiKey=f7a3dc5eadb04968a812681696d393c4")
articles=res.json()
title=articles['articles']
result= []
link=[]
#print(title)
message=""
for i in title:
    result.append(i['title'])
    link.append(i['url'])
    head=str(i['title'])

    message=message+" "+head+ " : "+i['url']+"\n"

message=message.encode('utf-8','ignore').decode()
sub=(f"{pdate} Today's Top new's  at time {hour} : {min} 📰").encode('utf-8','ignore').decode()
end="For Feedback Mail us at ❤️:  jayeshandcompany@gmail.com"
end=end.encode('utf-8','ignore').decode()
context = ssl.create_default_context()
message2 = f"""\
Subject: {sub}

{message}

{end}
"""


message3=message2.encode('utf-8','ignore')
success=success.encode('utf-8','ignore')
try:
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL('smtp.gmail.com',465, context=context) as server:
        server.login(sender_email, password)
        with open('emails.txt', 'r') as file:
            for recieve in file:
                server.sendmail(sender_email,recieve, message3)
        server.sendmail(sender_email,'jayeshdarda9@gmail.com',success)


except Exception as e:
    server.sendmail(sender_email, 'jayeshdarda9@gmail.com', e)
