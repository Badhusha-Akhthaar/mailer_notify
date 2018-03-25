import sendgrid
import os
from sendgrid.helpers.mail import *
from urllib.request import urlopen
import urllib
import requests
import cssutils
import sys
import re
import schedule
import time
from datetime import datetime
from bs4 import BeautifulSoup

def main():
  url_main='https://www.amazon.in/dp/B077T6Q42N/?coliid=I2I1CTWJQKPMR1&colid=EQ037QQ2NU8G&psc=0&ref_=lv_ov_lig_dp_it'
  source=requests.get(url_main).text
  soup=BeautifulSoup(source,'lxml')
  rate=soup.find('span',{'id':'priceblock_saleprice'}).text
  fl=int(float(rate))
  if fl < 300:
    sg = sendgrid.SendGridAPIClient(apikey='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')
    from_email = Email("test@example.com")
    to_email = Email("akhthaaralibadhusha@gmail.com")
    subject = "Time to buy"
    content = Content("text/plain", "Rate has been reduced")
    mail = Mail(from_email, subject, to_email, content)
    response = sg.client.mail.send.post(request_body=mail.get())
    print(response.status_code)
    print(response.body)
    print(response.headers)
    
    

schedule.every(60).minutes.do(job)

while 1:
    schedule.run_pending()
    time.sleep(1)






















