#password

attempts = 3
password = "apple"

while attempts > 0:
    guess = input("Please enter your password")
    if guess == password:
        print("login sucessfull")
        break
    attempts -= 1
else:
    print("No attempts left")