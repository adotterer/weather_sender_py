import ezgmail
from weather_getter import write_memo
import schedule
import time

print(ezgmail.LOGGED_IN)
location = "Lake Kachess, WA"


def send_email():
    # write_memo(location)

    daily_memo = open("./memos/daily.txt", "r").read()
    print(daily_memo)
    # print(daily_memo)
    ezgmail.send('adotterer@gmail.com', "Forecast for " + location,
                 daily_memo, mimeSubtype='plain')
    ezgmail.send('mshipp08@gmail.com', "Forecast for " + location,
                 daily_memo, mimeSubtype='plain')


schedule.every().day.at("08:01").do(
    write_memo, target_location=location)
schedule.every().day.at("08:02").do(send_email)

while True:
    schedule.run_pending()
    time.sleep(1)
