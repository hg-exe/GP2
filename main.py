
#Password guessing
attempts = 3
password = "ILoveAnime"

while attempts > 0:
    guess = input("please enter your password:")
    if guess == password:
        print("login successfull")
        break
    attempts -= 1
else:
    print("No Attempts left")