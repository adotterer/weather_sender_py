import ezgmail
from weather_getter import write_memo

print("Logged into email: ", ezgmail.LOGGED_IN)
location = "Diablo Lake, Whatcom County, Washington 98267"


def send_email():
    daily_memo = open("./memos/daily.txt", "r").read()

    print(daily_memo)

    ezgmail.send('adotterer@gmail.com', "Forecast for " + location,
                 daily_memo, mimeSubtype='plain')
    ezgmail.send('mshipp08@gmail.com', "Forecast for " + location,
                 daily_memo, mimeSubtype='plain')


write_memo(location)
send_email()
