# Functions go here ...

# checks users enter yes or no to a question
def yes_no(question):
    valid = False
    while not valid:
        response = input(question).lower()

        if response == "yes" or response == "y":
            return "yes"

        elif response == "no" or response == "n":
            return "no"

        else:
            print("Please answer yes / no")


def instructions():
    print("***** How to play *****")
    print()
    print("The rules of the game go here")
    print()
    return ""


# main routine goes here...
played_before = yes_no("have you played this game"
                       "before? ")

if played_before == "no":
    instructions()

print("program continues")
