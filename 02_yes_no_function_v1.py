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


# main routine goes here...
show_instructions = yes_no("have you played this game"
                           "before? ")
print("you chose {}".format(show_instructions))
print()
having_fun = yes_no("are you having fun?")
print("you said {} to having fun".format(having_fun))