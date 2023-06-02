import csv
import json
import datetime
import tkinter as tk
import time as t
import win10toast

#School Time Table

lesson_times = {
    "1": [datetime.time(8, 0), datetime.time(8, 45)],
    "2": [datetime.time(8, 45), datetime.time(9, 30)],
    "3": [datetime.time(9, 50), datetime.time(10, 35)],
    "4": [datetime.time(10, 35), datetime.time(11, 20)],
    "5": [datetime.time(11, 40), datetime.time(12, 25)],
    "6": [datetime.time(12, 30), datetime.time(13, 15)],
    "7": [datetime.time(13, 20), datetime.time(14, 5)],
    "8": [datetime.time(14, 5), datetime.time(14, 50)],
    "9": [datetime.time(15, 0), datetime.time(15, 45)],
    "10": [datetime.time(15, 45), datetime.time(16, 30)],
    "11": [datetime.time(16, 30), datetime.time(17, 15)],
}

monday = {
    "1": "Mathe",
    "2": "Mathe",
    "3": "Englisch",
    "4": "Englisch",
    "5": "Biologie",
    "6": "Biologie",
}

tuesday = {
    
}

wednesday = {
    
}

thursday = {
    "1": "Deutsch",
    "2": "Deutsch",
    "3": "Musik",
    "4": "Musik",
    "5": "Mathe",
    "6": "Mathe",
    "7": "Mittagspause",
    "8": "Biologie",
    "9": "Biologie",
}

friday = {
    
}


def print_whole_day(day, time):
    current_lesson = 0
    for key, value in day.items():
        if time >= lesson_times[key][0] and time <= lesson_times[key][1]:
            print("> " + value)
            current_lesson = key
        else:
            print("  " + value)
    
    next_lesson = str(int(current_lesson) + 1)
    next_lesson_name = day.get(next_lesson, "Ende der Schule")

    while True:
        time_until_end_of_lesson = datetime.timedelta(hours=lesson_times[next_lesson][1].hour, minutes=lesson_times[next_lesson][1].minute, seconds=lesson_times[next_lesson][1].second) - datetime.timedelta(hours=datetime.datetime.now().time().hour, minutes=datetime.datetime.now().time().minute, seconds=datetime.datetime.now().time().second)
        time_str = str(time_until_end_of_lesson).split(".")[0]
        hours, minutes, seconds = time_str.split(":")
        
        if int(hours) == 1 and int(minutes) == 0 and int(seconds) == 0:
            win10toast.ToastNotifier().show_toast("Schule", "Noch 1 Stunde bis " + next_lesson_name, duration=10)
        if int(hours) == 0 and int(minutes)%10 == 0 and int(seconds) == 0:
            win10toast.ToastNotifier().show_toast("Schule", f"Noch {minutes} Minuten bis " + next_lesson_name, duration=10)
        elif int(hours) == 0 and int(minutes) == 15 and int(seconds) == 0:
            win10toast.ToastNotifier().show_toast("Schule", "Noch 15 Minuten bis " + next_lesson_name, duration=10)
        elif int(hours) == 0 and int(minutes) == 5 and int(seconds) == 0:
            win10toast.ToastNotifier().show_toast("Schule", "Noch 5 Minuten bis " + next_lesson_name, duration=10)
        
        if time_until_end_of_lesson <= datetime.timedelta(0):
            print_whole_day(day, datetime.datetime.now().time())
        
        print("Noch " + time_str + " bis " + next_lesson_name, end="\r")

        t.sleep(1/5)


current_day = datetime.datetime.today().weekday()
current_time = datetime.datetime.now().time()

match current_day:
    case 0: print_whole_day(monday, current_time)
    case 1: print_whole_day(tuesday, current_time)
    case 2: print_whole_day(wednesday, current_time)
    case 3: print_whole_day(thursday, current_time)
    case 4: print_whole_day(friday, current_time)
    case _: print("No school today")
