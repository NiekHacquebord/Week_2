current_time = 14
alarm_in_hours = int(input("In how many hours do you want to wake up?"))
alarm_time = alarm_in_hours+current_time
hours_left = alarm_time%24
print("Your alarm will ring at",(hours_left),"hours")

# -------------------------------------------------------------------------------
# current_time = 14
# alarm_in_hours = int(input("In how many hours do you want to wake up?"))
# alarm_time = alarm_in_hours
# alarm_days = alarm_time//24
# hours_left = alarm_time%24
# print("Your alarm will ring in",(alarm_days),"days and",(hours_left),"hours")
# -------------------------------------------------------------------------------