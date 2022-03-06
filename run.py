import random

# STORY TITLE


print("-" * 50)
print("A messengers journey")
print("-" * 50)
print("Instructions")
print("-" * 50)
character_name = input("Please enter your character's name: ")
print("-" * 50)


# START STORY

def start_story():
    """
    Start a new story here
    """
    print("-" * 50)
    print("\n Do you want to start the story again? \n")
    print("-" * 50)
    answer = input("[Enter: yes or no] ")
    print("-" * 50)

    if answer == "yes":
        path_1()

    else:
        start_story()

# PATH 1


def path_1():
    """
    Path 1
    """
    print("-" * 50)
    print(f"\nA messenger named {character_name} has been tasked to deliver \
an important message to the castle. Along the way, {character_name} came to \
a crossroad. To the left, the path led through mountains. To the right, the \
path led through a dark and scary forest. The mountains look safer, but will \
take a few extra days. The forest would be quicker, but it looks dangerous. \
Does {character_name} take the left path or the right?\n")
    print("-" * 50)

    answer = input("[Enter: left or right] ")
    print("-" * 50)

    if answer == "left":
        path_2_a()

    elif answer == "right":
        path_2_b()

    else:
        print("Invalid input")
        print("-" * 50)
        answer = input("[Enter: left or right] ")

# PATH 2


def path_2_a():
    """
    Path 2
    """
    print("-" * 50)
    print(f"\n{character_name} decided that it would be safer to take the \
left path through the mountains. \n Before the ascent, {character_name} \
passed a merchant who was selling supplies. Does {character_name} stop to \
buy supplies before moving on?\n")
    print("-" * 50)
    answer = input("[Enter: buy supplies or keep moving] ")
    print("-" * 50)

    if answer == "buy supplies":
        path_3_a()

    elif answer == "keep moving":
        path_3_b()

    else:
        print("Invalid input")
        print("-" * 50)
        answer = input("[Enter: buy supplies or keep moving] ")


def path_2_b():
    """
    Path 2
    """
    print("-" * 50)
    print("\n You chose the right path. Choose your next path. Left \
    or right? \n")
    print("-" * 50)
    answer = input("[Enter: left or right] ")
    print("-" * 50)

    if answer == "left":
        path_3_c()

    elif answer == "right":
        path_3_d()

    else:
        print("Invalid input")
        print("-" * 50)
        answer = input("[Enter: left or right] ")

# PATH 3


def path_3_a():
    """
    Path 3
    """
    print("-" * 50)
    print(f"\nAs {character_name} was busy looking at the supplies, the \
merchant, who was actually an assasin, snuck up behind {character_name} \
and attempted to attack.\n")
    print("-" * 50)
    print("Attempt to fight back? [Roll dice. Roll a 3, 4, 5 or 6 to win]")
    answer = input("[Enter: fight or don't fight] ")
    print("-" * 50)
    if answer == "fight":
        dice_roll = random.randrange(1, 6)
        print(f"You rolled a {dice_roll}")

        if dice_roll >= 3:
            print(f"{character_name} successfully countered the assasin and \
defeated him.")
            path_3_b()

        else:
            print(f"{character_name} failed to counter the assasins attacked \
and died.")
            start_story()

    elif answer == "don't fight":
        print(f"{character_name} died")
        start_story()

    else:
        print("Invalid input")
        print("-" * 50)
        answer = input("[Enter: fight or don't fight] ")


def path_3_b():
    """
    Path 3
    """
    print("-" * 50)
    print(f"\n{character_name} continues the journey through the mountains. \n\
Three days have past and {character_name} can finally see the castle in the \
distance. \n")
    print("-" * 50)
    answer = input("[Enter: left or right] ")
    print("-" * 50)

    if answer == "left":
        start_story()

    elif answer == "right":
        start_story()

    else:
        print("Invalid input")
        print("-" * 50)
        answer = input("[Enter: left or right] ")


def path_3_c():
    """
    Path 3
    """
    print("-" * 50)
    print("\n You chose the left path. Choose your the next path. Left \
    or right? \n")
    print("-" * 50)
    answer = input("[Enter: left or right] ")
    print("-" * 50)

    if answer == "left":
        start_story()

    elif answer == "right":
        start_story()

    else:
        print("Invalid input")
        print("-" * 50)
        answer = input("[Enter: left or right] ")


def path_3_d():
    """
    Path 3
    """
    print("-" * 50)
    print("\n You chose the right path. Choose your next path. Left \
    or right? \n")
    print("-" * 50)
    answer = input("[Enter: left or right] ")
    print("-" * 50)

    if answer == "left":
        start_story()

    elif answer == "right":
        start_story()

    else:
        print("Invalid input")
        print("-" * 50)
        answer = input("[Enter: left or right] ")

# PATH 4


def path_4_a():
    """
    Path 4
    """
    print("-" * 50)
    print("\n You chose the right path. Choose your next path. Left \
    or right? \n")
    print("-" * 50)
    answer = input("[Enter: left or right] ")
    print("-" * 50)

    if answer == "left":
        start_story()

    elif answer == "right":
        start_story()

    else:
        print("Invalid input")
        print("-" * 50)
        answer = input("[Enter: left or right] ")


def path_4_b():
    """
    Path 4
    """
    print("-" * 50)
    print("\n You chose the right path. Choose your next path. Left \
    or right? \n")
    print("-" * 50)
    answer = input("[Enter: left or right] ")
    print("-" * 50)

    if answer == "left":
        start_story()

    elif answer == "right":
        start_story()

    else:
        print("Invalid input")
        print("-" * 50)
        answer = input("[Enter: left or right] ")


def finish_story():
    """
    Story finishes here
    """


def game_over():
    """
    When the story ends before making it to the end
    """


# RETURNED FUNCTIONS


path_1()
path_2_a()
path_2_b()
path_3_a()
path_3_b()
path_3_c()
path_3_d()
path_4_a()
path_4_b()
start_story()
finish_story()
