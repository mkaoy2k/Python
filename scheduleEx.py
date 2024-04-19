"""This is an example to schedule a routine job
via 'schedule' Module."""
import schedule
import time
import datetime


def take_break():
    print("It's time for a coffee break")
    print(f'===>{datetime.datetime.now()}')


# schedule a job to run in every 5-10 seconds interval randomly
schedule.every(5).to(10).seconds.do(take_break)

while True:
    # Checks whethr a scheduled task is pending to run or not
    schedule.run_pending()
    time.sleep(1)
