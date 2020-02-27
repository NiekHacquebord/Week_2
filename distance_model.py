distance_km = int(input("What is the distance of your journey? (in km)"))

trip_time_walk_mins=int(distance_km*(60/5))
trip_time_bike_mins=int(distance_km*(60/20))
trip_time_car_mins=int(distance_km*(60/45))

trip_time_walk_hours=int(trip_time_walk_mins/60)
trip_time_bike_hours=int(trip_time_bike_mins/60)
trip_time_car_hours=int(trip_time_car_mins/60)

trip_time_walk_remaining=int(trip_time_walk_mins%60)
trip_time_bike_remaining=int(trip_time_bike_mins%60)
trip_time_car_remaining=int(trip_time_car_mins%60)

additional_time_walk=5
additional_time_bike=10
additional_time_car=8

print("Your trip will take",
      (trip_time_walk_hours), "hours and",(trip_time_walk_remaining+additional_time_walk), "minutes if you walk,",
      (trip_time_bike_hours), "hours and",(trip_time_bike_remaining+additional_time_bike),"minutes if you go by bike, and",
      (trip_time_car_hours), "hours and",(trip_time_car_remaining+additional_time_car),"minutes if you take the car.")
