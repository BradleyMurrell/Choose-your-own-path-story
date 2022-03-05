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

#PATH 1

def path_1():
    """
    Path 1
    """
    print("Story starts here. Choose your first path. Left or right? \n")
    answer = input("[Enter: left or right] \n")

    if answer == "left":
        path_2_a()

    elif answer == "right":
        path_2_b()

    else:
        path_1()

#PATH 2

def path_2_a():
    """
    Path 2
    """
    print("You chose the left path. Choose your the next path. Left or right? \n")
    answer = input("[Enter: left or right] \n")

    if answer == "left":
        path_3_a()

    elif answer == "right":
        path_3_b()

    else:
        path_2_a()

def path_2_b():
    """
    Path 2
    """
    print("You chose the right path. Choose your next path. Left or right? \n")
    answer = input("[Enter: left or right] \n")

    if answer == "left":
        path_3_c()

    elif answer == "right":
        path_3_d()

    else:
        path_2_b()

#PATH 3

def path_3_a():
    """
    Path 3
    """
    print("You chose the left path. Choose your the next path. Left or right? \n")
    answer = input("[Enter: left or right] \n")

    if answer == "left":
        start_story()

    elif answer == "right":
        start_story()

    else:
        path_3_a()

def path_3_b():
    """
    Path 3
    """
    print("You chose the right path. Choose your next path. Left or right? \n")
    answer = input("[Enter: left or right] \n")

    if answer == "left":
        start_story()

    elif answer == "right":
        start_story()

    else:
        path_3_b()

def path_3_c():
    """
    Path 3
    """
    print("You chose the left path. Choose your the next path. Left or right? \n")
    answer = input("[Enter: left or right] \n")

    if answer == "left":
        start_story()

    elif answer == "right":
        start_story()

    else:
        path_3_c()

def path_3_d():
    """
    Path 3
    """
    print("You chose the right path. Choose your next path. Left or right? \n")
    answer = input("[Enter: left or right] \n")

    if answer == "left":
        start_story()

    elif answer == "right":
        start_story()

    else:
        path_3_d()



path_1()
path_2_a()
path_2_b()
path_3_a()
path_3_b()
path_3_c()
path_3_d()
