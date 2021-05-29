import ezgmail
# import schedule
import time
from weather_getter import write_memo

print("Logged into email: ", ezgmail.LOGGED_IN)
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


write_memo(location)
send_email()
# schedule.every().day.at("08:01").do(
#     write_memo, target_location=location)
# schedule.every().day.at("08:04").do(send_email)

# while True:
#     schedule.run_pending()
#     time.sleep(1)
