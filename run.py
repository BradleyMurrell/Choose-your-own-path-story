def start_story():
    """
    Start a new story here
    """
    print("Do you want to start the story again? \n")
    answer = input("[Enter: yes or no] \n")

    if answer == "yes":
        path_1()

    elif answer == "no":
        print("Thank you for playing")


def path_1():
    """
    First path in the story
    """
    print("Story starts here. Choose your first path. Left or right?")
    answer = input("[Enter: left or right] \n")

    if answer == "left":
        start_story()

    elif answer == "right":
        start_story()

path_1()
