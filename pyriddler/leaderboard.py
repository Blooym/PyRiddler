"""
Leaderboard data & creating handler
"""

import csv
import pandas
field_names = ["Username", "Score"]


def leaderboard_check():
    """
    Checks if the leaderboard exists or not.
    Returns:
        True<boolean>: Leaderboard already exists.
        False<boolean>: Leaderboard was created (Did not exist).
    Example:
        if leaderboardCheck():
            print("Leaderboard already exists!")
        else:
            print("Created leaderboard!")
    """
    try:
        with open("leaderboard.csv", "r", encoding="utf-8") as leaderboard_file:
            leaderboard_file.close()
            return True
    except FileNotFoundError:
        with open("leaderboard.csv", "w", encoding="utf-8") as leaderboard_file:
            writer = csv.DictWriter(leaderboard_file, fieldnames=field_names)
            writer.writeheader()
            leaderboard_file.close()
            return False


def create_entry(username, score):
    """
    Creates a new entry in the leaderboard
    Arguments:
        username<string>: The username for the leaderboard entry
        score<int>: The score for the leaderboard entry
    Returns:
        True<bool>: Creating entry success.
        False<bool>: Creating entry failed.
    Example
        createEntry("John", 50)
    """
    leaderboard_check()
    if len(username) <= 1:
        print("Username not given, saving as generic name...")
        username = "Player"

    with open("leaderboard.csv", mode="a", encoding="utf-8") as leaderboard_file:
        writer = csv.DictWriter(leaderboard_file, fieldnames=field_names)
        writer.writerow({'Username': username, 'Score': score})
        leaderboard_file.close()


def list_scores(amount):
    """
    List scores from the leaderboard file (highest -> lowest)
    Arguments:
        amount<int>: The amount of entries to list
    Returns
        Leaderboard<string>: The leaderboard rows requested
    Example
        amount = 50
        print(f"Here are the top {amount} scores! {listScores(amount)}")
    """
    if leaderboard_check():
        try:
            leaderboard_file = pandas.read_csv('leaderboard.csv')
            return leaderboard_file.nlargest(amount, 'Score')
        except FileNotFoundError:
            return "No scores to show right now, get out there and set some!"
    else:
        return "No scores to show right now, get out there and set some!"
