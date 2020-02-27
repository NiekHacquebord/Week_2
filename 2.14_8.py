current_time = int(input("What is the current time (0-23)?"))
alarm_in_hours = int(input("In how many hours do you want to wake up?"))
alarm_time_absolute = alarm_in_hours+current_time
alarm_time_correct = alarm_time_absolute%24
print("Your alarm will ring at",(alarm_time_correct),"o'clock")2