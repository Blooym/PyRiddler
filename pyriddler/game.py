"""
Game and score handler
"""

# Imports
import sys
from pyriddler.leaderboard import create_entry
from pyriddler.riddles import random_riddle, get_value, total_riddles


def show_logo():
    """
    Shows the game logo
    """
    spacer = "\n" * 30

    return f"""
    {spacer}
          .=>r?(||||(?*~:`
         :i?,_>||||||||||(=
         ~ir_'~|||||||||((?
         =rrrrrrrr(||||(((r
  `_=!!!!!!!!!!!!!?||(((((r xllY(=
 "|iii||1AznXV||s@x(((((((r Kdddbby'     `,,,,_          ,,,,_   !*      ~i      ;i  )^
"ii|||||zRsyN@Sk8@]((((())^ qdbbbbbs     _bi>^hV`-`   -``bY>>VU` =>   _,-iA   _,-xA  Xl   -,_`  -``-
?||||||||||||tdRbn(((())?!`rbbbbbbbb_    _b^'-zS`wV  *A,`b(_,Yp. Tm `kt^*tA `wV^*yA  Xl ,U(>?S_ bzx|
|||||||||?!,"~>>>>>>>>;!!rybbbbbbbbb=    _bn||r- _A*-A* `bnrXP-  Tm ,b>  |A ,b>  iA  Xl |b???V= b?
?|||||||^`?mEMM666$####Rbbbbbbbbbbbb_    _b!      ^Aeu  `b* .sV` Tm `XV^*VA `aV^*VA  Xl ,mi^>^` b?
=|||||||-rEM6666dd@@$$#@#R#Bbbbbbbbz     `-`       1U`   -`  `-` .-  `,,'`-  `,,'`-  '.   _,,'  -`
 ~||||((.x6666dddd##bbON$d8$bbbbbb1`             =|i-
  ."~~~~`i66ddddddx|||||||(((((?;'
         iddddddbbwsessooon
         iddddbbbbbbbo=,Lbm
         "qbbbbbbbbbb4~!1bn
          `~izXSAbbAAPeu)=
    """


def submit_score(score):
    """
    Submits a score to the leaderboard
    Arguments:
        score<int>: The players total score at the end of the game
    Returns
        void
    """
    username = input("Username for Leaderboard > ")
    create_entry(username, score)
    print("Your score is now on the leaderboard! Press any key to exit PyRiddler.")
    sys.exit()


# The keys of riddles already used.
used_riddle_keys = []


def play_game(score):
    """
    Start the riddle game
    Arguments:
        score<int>: The amount of times the player has already won a game this session
    """

    # Generate riddle, if it's already been used, generate another
    riddle_chosen = False
    while not riddle_chosen:
        riddle_answer = random_riddle()
        # Riddle already used
        if riddle_answer not in used_riddle_keys:
            riddle_chosen = True
            riddle_hint = get_value(riddle_answer)
        if len(used_riddle_keys) == total_riddles():
            print(
                f'{show_logo()}Congratulations, you have solved all the riddles we have!')
            submit_score(score)

    print(show_logo())
    print(f"Your riddle is as follows!\n\"{riddle_hint}\"\n")
    game_over = False
    incorrect_guesses = 1

    # Game In-Progress
    while not game_over:
        guess = input('One Word Answer > ').lower()

        # If player got the answer wrong, increment counter.
        if riddle_answer != guess:
            print(
                f"""
                {show_logo()}
                Incorrect! You have used {incorrect_guesses} out of 6 guesses.
                \n\"{riddle_hint}\"\n""")
            incorrect_guesses = incorrect_guesses + 1

        # If player has used all their guesses, end the game loop
        if incorrect_guesses == 7:
            game_over = True
            print(
                f"Game Over! You ran out of guesses. Your total score was {score}")

        # If the user guesses correctly, end the game loop
        if guess == riddle_answer:
            game_over = True
            score = score + 1
            used_riddle_keys.append(riddle_answer)
            print(
                f"""\nCongratulations, the answer was {riddle_answer}! Your score is now {score}!
                Well done.\n""")

    # After the game has ended.
    while game_over:
        play_again = input('Play Again? [Y/n] > ').lower()
        if play_again == 'n':
            if score > 0:
                print(f"Game Ended! Your total score was {score}.")
                submit_score(score)
            else:
                sys.exit()
        else:
            play_game(score)
