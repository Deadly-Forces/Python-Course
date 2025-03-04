# Hangman in Python
import random

words = ("apple", "banana", "orange", "pear", "watermelon")

hangman_art = {0: ("     ",
                   "     ",
                   "     "),
                1: ("  o  ",
                   "     ",
                   "     ",
                   "     "), 
                2: ("  o  ",
                    "  |  ",
                    "     ",
                    "     "),
                3: ("  o  ",
                    " /|  ",
                    "     ",
                    "     "),
                4: ("  o  ",
                       " /|\\ ",
                    "     ",
                    "     "),
                5: ("  o  ",
                       " /|\\ ",
                       " /   ",
                       "     "),
                6: ("  o  ",
                           " /|\\ ",
                           " / \\ ",
                           "     ")
                }

def display_man(wrong_guesses):
    for line in hangman_art[wrong_guesses]:
        print(line)
    print(hangman_art[wrong_guesses])

def display_hint(hint):
    pass


def display_answer(answer):
    pass

def main():    
    answer = random.choice(words)
    hint = ["_"] * len(answer)
    wrong_guesses = 0
    guessed_letters = set()
    is_running = False
    while is_running:
        display_man(wrong_guesses)
        display_hint(hint)
        display_answer(answer)
        guess = input("Guess a letter: ").lower()
        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue
if __name__ == "__main__":
    main()