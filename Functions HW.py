def main():
    hours = int(input("Enter the hours, less than 24. "))
    validatedhours = hoursvalid(hours)
    
    minutes = int(input("Enter the minutes, less than 60. "))
    validatedminutes = minutesvalid(minutes)

    print(validatedhours, validatedminutes)

def hoursvalid(hours):
    while hours > 23:
        hours = int(input("Enter the hours, less than 24: "))
    return hours

def minutesvalid(minutes):
    while minutes > 59:
        minutes = int(input("Enter the minutes, less that 60: "))
    return minutes

main()
