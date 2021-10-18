"""
Riddle handling for pyriddler
"""

import random
import json


def create_riddle_dictionary():
    """
    Creates a riddle file with default riddles in a JSON format.
    Returns:
        void
    """

    default_riddles = {
        "dozens": "A word I know, Six letters it contains, Subtract just one, And twelve is what remains.",  # pylint: disable=C0301
        "shorter": "What common English word becomes shorter when you add two letters?",
        "footsteps": "The more you take, the more you leave behind. What am I?",
        "incorrectly": "What common 11-letter word is always spelled incorrectly",
        "noon": "What word with 4 letters can be written forward, backward or upside down, and can still be read from left to right?"}  # pylint: disable=C0301

    json_dict = json.dumps(default_riddles, indent=4)
    with open('riddles.json', 'w', encoding="utf-8") as riddles_file:
        riddles_file.write(json_dict)
        riddles_file.close()


def get_value(key):
    """
    Get the value for key from the riddles file
    Arguments:
        key<string>: The key to search in the dictionary
    Returns:
        value<string>: The value for the given key
    """

    try:
        with open('riddles.json', 'r', encoding="utf-8") as riddles_file:
            riddles_file = json.load(riddles_file)
            return riddles_file[key]
    except KeyError:
        return f'Could not find value for key: {key}'


def random_riddle():
    """
    Generate a random riddle key from the riddles file
    Returns:
        key<string>: A randomised key
    """
    try:
        with open('riddles.json', 'r', encoding="utf-8") as riddles_file:
            riddles_file = json.load(riddles_file)
            return random.choice(list(riddles_file.keys()))
    except FileNotFoundError:
        create_riddle_dictionary()
        with open('riddles.json', 'r', encoding="utf-8") as riddles_file:
            riddles_file = json.load(riddles_file)
            return random.choice(list(riddles_file.keys()))
    except BaseException:  # pylint: disable=W0703
        return print(
            "Failed to generate a random value from dictionary, exiting.")


def total_riddles():
    """
    Get the total amount of riddles in the riddles file
    Returns:
        amount<int>: The total amount of riddles
    """
    with open('riddles.json', 'r', encoding="utf-8") as riddles_file:
        riddles_file = riddles_file.read()
        riddles_file = json.loads(riddles_file)
        return len(riddles_file)
