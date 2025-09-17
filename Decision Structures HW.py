speedlimit = float(input("What is the speed limit? "))
speed = float(input("What is your average speed? "))
distance = float(input("What is the distance you are traveling in miles? "))

speedtime = distance/speed #hours
speedlimittime = distance/speedlimit #hours

minutes_per_hour = 60

timesaved = (speedlimittime - speedtime)*minutes_per_hour

if timesaved > 0:
    print(f'You saved {timesaved:.2f} minutes.')
elif timesaved == 0:
    print("No time saved, good job driving at the speed limit.")
else:
    print("You are going slower than the speed limit, people might get mad.")
