# -*- coding: utf-8 -*-
"""
Created on Fri Jul 22 22:29:08 2022

@author: pagar
"""

from datetime import datetime
#from playsound import playsound
alarm_time = input("Enter the time of alarm to be set: HH:MM:SS\n")
alarm_hour = alarm_time[0:2]                    #size of numbers
alarm_minute = alarm_time[3:5]
alarm_seconds= alarm_time[6:8]
alarm_period = alarm_time[9:11].upper()              #am-pm
print("Setting up alarm..")
while True:
    now = datetime.now()
    current_hour = now.strftime("%I")
    current_minute = now.strftime("%M")
    current_seconds = now.strftime("%S")
    current_period = now.strftime("%p")
    if(alarm_period == current_period):
        if(alarm_hour == current_hour):
            if(alarm_minute == current_minute):
                if(alarm_seconds == current_seconds):
                    print("Wakeup buddy!!")
                    #playsound(audio)
                    break