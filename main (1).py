import random as r

# This keeps it looping.
a = 0.1
b = 0.2

# Setting random integer as dice (Number Cube).
dice = r.randint

# Whileloops dice (r.randint), and ask "Do you wanna exit", y = yes, n = no.
while a != b:
    print("You rolled : " + str(dice(1,6)))
    ab = str(input("Do you wanna exit y/n : "))
    if ab == 'y' or ab == 'Y':
        exit()
    elif ab == 'n' or ab == 'N':
        # Space
        print("")
    else:
        print("Invalid Variable")
        exit()


