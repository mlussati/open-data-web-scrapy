import schedule
import time

def job(t):
    print ("I'm working...", t)
    return

schedule.every().day.at("10:55").do(job,'It is 10:55')

while True:
    schedule.run_pending()
    time.sleep(60) # wait one minute