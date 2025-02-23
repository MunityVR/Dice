import random as r

# Setting random integer as dice (Number Cube).
dice = r.randint

# Whileloops dice (r.randint), and ask "Do you wanna exit", y = yes, n = no.
while True:
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


