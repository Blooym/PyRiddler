"""
Menu handling
"""

# PyRiddlers Entry Process
import sys
from pyriddler.leaderboard import list_scores
from pyriddler.game import play_game, show_logo


def show_leaderboard():
    """
    Pulls the leaderboard from leaderboard.py and displays it
    """
    try:
        score_limit = int(input("Show How Many Scores? > "))
        print(f"\n{list_scores(score_limit)}\n")
    except ValueError:
        show_leaderboard()

    go_back = input("Go Back? [Y/n] > ")
    if go_back == "n".lower():
        sys.exit()
    else:
        main_menu()


def options():
    """
    Show the user options to choose from, repeat until they pick a valid choice
    """
    try:
        choice = int(input('Choice > '))
        if choice == 1:
            play_game(0)
        elif choice == 2:
            show_leaderboard()
        elif choice == 3:
            sys.exit()
        else:
            options()
    except ValueError:
        options()


def main_menu():
    """
    Show the games main menu, essentially the entry function.
    """

    print(
        f"""
    {show_logo()}
    Welcome to PyRiddler!
    The fun and easy to play Riddle guessing game.

    [1] - Start new game
    [2] - See leaderboard
    [3] - Quit
    """)

    options()


main_menu()
