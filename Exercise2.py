# Exercise 2

the_string = "Hello World"
num_Ls = int(0)

for letter in the_string:
    if letter.lower() == "l":
        num_Ls += 1
print("The number of L's in the string is {}".format(num_Ls))
