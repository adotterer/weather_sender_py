import ezgmail
# import schedule
# import time
from weather_getter import write_memo

print("Logged into email: ", ezgmail.LOGGED_IN)
location = "Granite Falls, WA 98252"


def send_email():
    # write_memo(location)

    daily_memo = open("./memos/daily.txt", "r").read()
    print(daily_memo)
    # print(daily_memo)
    ezgmail.send('adotterer@gmail.com', "Forecast for " + location,
                 daily_memo, mimeSubtype='plain')
    ezgmail.send('mshipp08@gmail.com', "Forecast for " + location,
                 daily_memo, mimeSubtype='plain')


write_memo(location)
send_email()
# 7 13 * * 1-7 /Users/adott/Documents/PROJECTS/py_email/weather_sender.py
