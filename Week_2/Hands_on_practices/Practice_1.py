# Create a program that gives different messages based on time of day


import datetime

def time_of_day_message():
    current_time = datetime.datetime.now().hour

    if 5 <= current_time < 12:
        print("Good Morning!")
    elif 12 <= current_time < 17:
        print("Good Afternoon!")
    elif 17 <= current_time < 21:
        print("Good Evening!")
    else:
        print("Good Night!")

time_of_day_message()
