# Exercise 1

greeting_txt = """You wander alone at night across the Brunel concourse.
Alone, drunk and without coin, you begin to lose hope of ever making it to Games programming.

"Why I am going to Games Programming? It's 4:30AM" you begin to blubber at no-one in particular, yet before your
sot tongue can cross the finish line of  single sentence, a large tentacle monster bearing a strong resemblance to
Chris Cox crosses your path. There is no more time for thought..."""

print(greeting_txt)

inventory = ["sword", "morningstar", "an obscene hexagon", "the number 42", 42, "tentacle sweeper"]

print(inventory)

weapon = input("Choose your weapon: ").lower()

if weapon not in inventory:
    print("That's not in your inventory, you die screaming in the arms of Chris Octocox")
else:
    print("You reach down and pull a %s from your bag" % weapon)
if weapon == "tentacle sweeper":
    print("Wielding the almighty sweeper you vanquish the beast back into the fiery depths from whence it came (MILL "
          "HALL)... And you awake in class")
else:
    print("It is not enough, despite a valiant effort, you succumb to a squelchy demise.")

    pyString = "Python"
    outputString = ""
    for letter in pyString:
        if letter != "t":
            outputString += letter

    print(outputString)

    # numbers list

    numbers = [2, 3, 5, 7, 66, 89, 134]
    playerNum = (input("tell me a number..."))

    if not playerNum.isdigit():
        print("that is not a number")
    ###
    playerNum = int(playerNum)
    outputList = []

    for i in numbers:
        if i < playerNum:
            outputList.append(i)

    print(outputList)