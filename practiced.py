# You are a pilot, cruising at an altitude of 33000 ft,
# you want to land your plane, to land your plane, you need
# to be under 5000ft take input from the pilot, what
# is your current altitude, and suggest
# the pilot to go around if the altitude is more than 10K feet,
# if its more than 5K suggest the pilot to land the plane
# by bringing it to 1000ft

altitude = int(input("What is your current altitude: "))
print(altitude)
if(altitude>10000):
    print("Go around the landing site")
elif(altitude>=5000&altitude<10000):
    print("Go down to 1000ft and land")
