"""
Imports go here
"""
import random


print("-" * 50)
print("A messengers journey")
print("-" * 50)
print("Instructions")
print("-" * 50)
character_name = input("Please enter your character's name: \n")
print("-" * 50)


def start_story():
    """
    Start a new story here
    """
    dotted_line()
    print("Do you want to start the story again?")
    dotted_line()
    answer = input("[Enter: yes or no] ")
    dotted_line()

    if answer == "yes":
        path_1()

    else:
        start_story()


def path_1():
    """
    Path 1
    """
    dotted_line()
    print(f"A messenger named {character_name} has been tasked to deliver \
an important message to the castle. Along the way, {character_name} came to \
a crossroad. To the left, the path led through mountains. To the right, the \
path led through a dark and scary forest. The mountains look safer, but will \
take a few extra days. The forest would be quicker, but it looks dangerous. \
Does {character_name} take the left path or the right?")
    dotted_line()

    answer = input("[Enter: left or right] ")
    dotted_line()

    if answer == "left":
        path_2_a()

    elif answer == "right":
        path_2_b()

    else:
        print("Invalid input")
        dotted_line()
        answer = input("[Enter: left or right] ")


def path_2_a():
    """
    Path 2
    """
    dotted_line()
    print(f"{character_name} decided that it would be safer to take the \
left path through the mountains. Before the ascent, {character_name} passed \
a merchant who was selling supplies. Does {character_name} stop to buy \
supplies before moving on?")
    dotted_line()
    answer = input("[Enter: buy supplies or keep moving] ")
    dotted_line()

    if answer == "buy supplies":
        path_3_a()

    elif answer == "keep moving":
        path_3_b()

    else:
        print("Invalid input")
        dotted_line()
        answer = input("[Enter: buy supplies or keep moving] ")


def path_2_b():
    """
    Path 2
    """
    dotted_line()
    print(f"{character_name} decided that time was short and it would be \
quicker to take the right path through the scary forest. After some time, \
{character_name} comes to a river. There is a bridge to cross to the other \
side, but it looks like it is about to fall apart. Does {character_name} \
attempt to cross the bridge?")
    dotted_line()
    answer = input("[Enter: cross bridge or find another way] ")
    dotted_line()

    if answer == "find another way":
        path_3_c()

    elif answer == "cross bridge":
        path_3_d()

    else:
        print("Invalid input")
        dotted_line()
        answer = input("[Enter: cross bridge or find another way] ")


def path_3_a():
    """
    Path 3
    """
    dotted_line()
    print(f"As {character_name} was busy looking at the supplies, \
the merchant, who was actually an assasin, snuck up behind {character_name} \
and attempted to attack.")
    dotted_line()
    print("Attempt to fight back? [Roll dice. Roll a 3, 4, 5 or 6 to win]")
    answer = input("[Enter: fight or don't fight] ")
    dotted_line()
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
        dotted_line()
        answer = input("[Enter: fight or don't fight] ")


def path_3_b():
    """
    Path 3
    """
    dotted_line()
    print(f"{character_name} continues the journey through the mountains. \
Three days have passed and {character_name} can finally see the castle in the \
distance. Does {character_name} continue to the castle or make camp and rest \
for the night?")
    dotted_line()
    answer = input("[Enter: continue or rest] ")
    dotted_line()

    if answer == "continue":
        finish_story()

    elif answer == "rest":
        path_4_a()

    else:
        print("Invalid input")
        dotted_line()
        answer = input("[Enter: continue or rest] ")


def path_3_c():
    """
    Path 3
    """
    dotted_line()
    print(f"{character_name} continues the journey through the forest. \
A day has passed and {character_name} can finally see the castle in the \
distance. Does {character_name} continue to the castle or make camp and rest \
for the night?")
    dotted_line()
    answer = input("[Enter: continue or rest] ")
    dotted_line()

    if answer == "continue":
        finish_story()

    elif answer == "rest":
        path_4_b()

    else:
        print("Invalid input")
        dotted_line()
        answer = input("[Enter: left or right] ")


def path_3_d():
    """
    Path 3
    """
    dotted_line()
    print(f"{character_name} attempted to cross the bridge. When \
{character_name} got halfway, the bridge started to collapse.")
    dotted_line()
    print("Attempt to run to the otherside? [Roll dice. Roll a \
3, 4, 5 or 6 to make it to the otherside]")
    answer = input("[Enter: run or stand still] ")
    dotted_line()

    if answer == "run":
        dice_roll = random.randrange(1, 6)
        print(f"You rolled a {dice_roll}")

        if dice_roll >= 3:
            print(f"{character_name} successfully made it across to the \
otherside before the bridge collapsed.")
            path_3_c()

        else:
            print(f"{character_name} failed to make it across in time and \
fell to their death")
            start_story()

    elif answer == "stand still":
        print(f"{character_name} fell to their death.")
        start_story()

    else:
        print("Invalid input")
        dotted_line()
        answer = input("[Enter: run or stand still] ")


def path_4_a():
    """
    Path 4
    """
    dotted_line()
    print("You chose the right path. Choose your next path. Left \
or right?")
    dotted_line()
    answer = input("[Enter: left or right] ")
    dotted_line()

    if answer == "left":
        start_story()

    elif answer == "right":
        start_story()

    else:
        print("Invalid input")
        dotted_line()
        answer = input("[Enter: left or right] ")


def path_4_b():
    """
    Path 4
    """
    dotted_line()
    print("You chose the right path. Choose your next path. Left \
or right?")
    dotted_line()
    answer = input("[Enter: left or right] ")
    dotted_line()

    if answer == "left":
        start_story()

    elif answer == "right":
        start_story()

    else:
        print("Invalid input")
        dotted_line()
        answer = input("[Enter: left or right] ")


def finish_story():
    """
    Story finishes here
    """
    print("\n Story ends \n")
    start_story()


def dotted_line():
    """
    Prints a dotted line with a new line above and below
    """
    print("\n")
    print("-" * 60)
    print("\n")


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
dotted_line()
