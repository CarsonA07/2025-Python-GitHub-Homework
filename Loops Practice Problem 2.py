password = 'calhoun'
attempts = 3

for i in range(attempts):
    guess = input("Enter the password: ")
    if guess == password:
        print("Access granted.")
    else:
        print("Incorrect password, try again.")
else:
    print("Account locked.")
