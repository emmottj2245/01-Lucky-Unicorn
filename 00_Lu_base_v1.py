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


def num_check(question, low, high):
    error = "please enter an whole number between 1 and 10\n"

    valid = False
    while not valid:
        try:
            # ask the question
            response = int(input(question))
            # if the amount is too low / too high give
            if low < response <= high:
                return response

            # output an error
            else:
                print(error)

        except ValueError:
            print(error)

    # Main routine goes here


# main routine goes here...
played_before = yes_no("have you played this game"
                       "before? ")

if played_before == "no":
    instructions()

# Ask user how much they want to play with...
how_much = num_check("how much would you"
                     " like to play with? ", 0, 10)

print("You will be spending ${}".format(how_much))
