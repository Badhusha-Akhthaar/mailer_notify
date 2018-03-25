import urllib
import re
import schedule
import time
from datetime import datetime

def job():
    print("Hello")
schedule.every(10).minutes.do(job)
schedule.every().hour.do(job)
schedule.every().day.at("22:17").do(job)
schedule.every(1).seconds.do(job)

while 1:
    schedule.run_pending()
    time.sleep(1)