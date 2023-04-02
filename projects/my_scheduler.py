#!/usr/bin/env python3
"""A simple reminder scheduler"""


import schedule
import time


def water_reminder():
    """remind me to drink water"""
    print("It's been an hour now. Drink a glass of water!")


def screen_time():
    """reminder to end screen time"""
    print("It's 9pm! Shut off the laptop screen.")


# After every hour water reminder is called
schedule.every().hour.do(water_reminder)

# Everyday at 9pm, shutdown the laptop
schedule.every().day.at("09:00").do(screen_time)

# Loop so that the scheduling task keeps running all the time
while True:
    # check whether a scheduled task is pending to run or not
    schedule.run_pending()
    time.sleep(1)
