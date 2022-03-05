def start_story():
    """
    Start a new story here
    """
    print("Do you want to start the story again? \n")
    answer = input("[Enter: yes or no] \n")

    if answer == "yes":
        path_1()

    else:
        start_story()


def path_1():
    """
    Tier 1
    """
    print("Story starts here. Choose your first path. Left or right? \n")
    answer = input("[Enter: left or right] \n")

    if answer == "left":
        path_2_a()

    elif answer == "right":
        path_2_b()

    else:
        path_1()


def path_2_a():
    """
    Tier 2
    """
    print("You chose the left path. Choose your the next path. Left or right? \n")
    answer = input("[Enter: left or right] \n")

    if answer == "left":
        start_story()

    elif answer == "right":
        start_story()

    else:
        path_2_a()

def path_2_b():
    """
    Tier 2
    """
    print("You chose the right path. Choose your next path. Left or right? \n")
    answer = input("[Enter: left or right] \n")

    if answer == "left":
        start_story()

    elif answer == "right":
        start_story()

    else:
        path_2_b()



path_1()
path_2_a()
path_2_b()
