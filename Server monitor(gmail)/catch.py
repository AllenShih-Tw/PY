import requests
from requests.auth import HTTPBasicAuth
import smtplib
from email.mime.text import MIMEText
from datetime import datetime
from bs4 import BeautifulSoup

dateTimeObj = datetime.now()
Realtime = dateTimeObj.strftime("%Y-%m-%d %H:%M:%S")
print([Realtime])
# url = 'https://www.google.com.tw/?gws_rd=ssl'
url = 'http://www.123123.com/'
r = requests.get(url, auth=HTTPBasicAuth('clmadmin', 'delta999'))
sr = str(r)
print("Web Requests responese:",sr)
mailtext = """web status report-%s
    %s""" % (Realtime, sr)
def gmail():
    gmail_user = 'allendx789@gmail.com'
    gmail_password = 'Allendx78789'  # your gmail password
    msg = MIMEText(mailtext)
    msg['Subject'] = "Web Status Report - %s" % (Realtime)
    msg['From'] = gmail_user
    msg['To'] = 'allendx123@gmail.com'
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.ehlo()
    server.login(gmail_user, gmail_password)
    server.send_message(msg)
    server.quit()
    print('Email sent!')
def make_count2():
    try:
        r = open("count2.txt", "r")
        content = r.read()
    except IOError:
        w = open("count2.txt", "w")
        w.write("0")
        w.close()
def make_count3():
    try:
        r = open("count3.txt", "r")
        content = r.read()
    except IOError:
        w = open("count3.txt", "w")
        w.write("0")
        w.close()

make_count2()
make_count3()


s = (sr[11:14])
sample = int(s)

if sample is 200:
    r = open("count2.txt", "r")
    content = r.read()
    Icontent = int(content)
    Icontent = 0
    Scontent = str(Icontent)
    w = open("count2.txt", "w")
    w.write(Scontent)
    w.close()

if sample is not 200:
    r = open("count2.txt", "r")
    content = r.read()
    Icontent = int(content)
    if Icontent < 3:
        Icontent = Icontent+1
        Scontent = str(Icontent)
        w = open("count2.txt", "w")
        w.write(Scontent)
        w.close()
        gmail()
    else:
        Icontent = Icontent+1
        Scontent = str(Icontent)
        w = open("count2.txt", "w")
        w.write(Scontent)
        w.close()




url2 = 'https://scp.deltaww.com/ccm/service/com.ibm.team.repository.service.internal.IServerStatusRestService/databaseStatus'
r2 = requests.get(url2, auth=HTTPBasicAuth('clmadmin', 'delta999'))
sr2 = str(r2)
s2 = (sr2[11:14])
sample2 = int(s2)

if sample2==200:
    r = requests.get(url2, auth=HTTPBasicAuth('clmadmin', 'delta999'))
    soup = BeautifulSoup(r.text, "xml")
    code = soup.find('code').text
    print("Database status:",code)
    mailtext2 = """DateBase status report-%s
    Status:%s""" % (Realtime, code)


    def gmail2():
        gmail_user = 'allendx789@gmail.com'
        gmail_password = 'Allendx78789'  # your gmail password
        msg = MIMEText(mailtext2)
        msg['Subject'] = "DataBase Status Report - %s" % (Realtime)
        msg['From'] = gmail_user
        msg['To'] = 'allendx123@gmail.com'
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.ehlo()
        server.login(gmail_user, gmail_password)
        server.send_message(msg)
        server.quit()
        print('Email2 sent!')

    if code == "OK":
        r = open("count3.txt", "r")
        content = r.read()
        Icontent = int(content)
        Icontent = 0
        Scontent = str(Icontent)
        w = open("count3.txt", "w")
        w.write(Scontent)
        w.close()
    else:
        r = open("count3.txt", "r")
        content = r.read()
        Icontent = int(content)
        if Icontent < 4:
            Icontent = Icontent+1
            Scontent = str(Icontent)
            w = open("count3.txt", "w")
            w.write(Scontent)
            w.close()
            gmail2()
        if Icontent >= 3:
            Icontent = Icontent+1
            Scontent = str(Icontent)
            w = open("count3.txt", "w")
            w.write(Scontent)
            w.close()