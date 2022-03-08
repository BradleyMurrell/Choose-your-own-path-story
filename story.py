from paths import path_1


def start_story():
    """
    Start a new story here
    """
    print("-" * 50)
    print("\n Do you want to start the story again? \n")
    print("-" * 50)
    answer = input("\n [Enter: yes or no] \n")
    print("-" * 50)

    if answer == "yes":
        path_1()

    else:
        start_story()


def finish_story():
    """
    Story finishes here
    """
    print("\n Story ends \n")
    start_story()


def game_over():
    """
    When the story ends before making it to the end
    """
    print("\n Game over \n")
    start_story()
