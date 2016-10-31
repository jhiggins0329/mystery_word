#Beggining of the python file
import random
import re

def dictionayr(master):
    with open("/usr/share/dict/words", "r") as f:
        for line in f:
            print(line, end="")
    dictionay = master.read()
    dictionary = dictionary.lower().split()

# Let the user choose a level of difficulty at the beginning of the program. Easy mode only has words of 4-6 characters; normal mode only has words of 6-8 characters; hard mode only has words of 8+ characters.
def easy_mode(word_list):
    easy_mode_list = []
    for word in word_list:
        if len(word) >= 4 and len(word) <= 6:
            easy_mode_list.append(word)
    return easy_mode_list

def medium_mode(word_list):
    medium_mode_list = []
    for word in word_list:
        if len(word) >= 4 and len(word) <= 6:
            medium_mode_list.append(word)
    return medium_mode_list

def hard_mode(word_list):
    hard_mode_list = []
    for word in word_list:
        if len(word) >= 4 and len(word) <= 6:
            hard_mode_list.append(word)
    return hard_mode_list

def random(word_list):
    correct_letter = random.choice(word_list)
    return correct_letter

# At the start of the game, let the user know how many letters the computer's word contains.
def display_word(word, gueseses):
    progress_display = []
    for letter in word:
        if letter in guesses:
            progress_display.append(letter)
        else:
            progress_display.appent("_")
    progress_display = " ".join(progress_display)
    progress_display = progress_display.upper()
    return progress_display

def complete_word(word, guesses):
    progress = display_word(word, guesses)
    if "_" in progress:
        return False
    else:
        return True

def what_level():
    level = input("What challenge do you want, easy, medium or hard?.\n")
    level = level.lower()
    if level == "easy":
        answer = random(easy_mode(dictionay))
    elif level == "medium":
        answer = random(medium_mode(dictionsy))
    else:
        answer = random(hard_mode(dictionaru))
    return answer

# Ask the user to supply one guess (i.e. letter) per round. This letter can be upper or lower case and it does not matter. If a user enters more than one letter, tell them the input is invalid and let them try again.

# Let the user know if their guess appears in the computer's word.

# Display the partially guessed word, as well as letters that have not been guessed. For example, if the word is BOMBARD and the letters guessed are a, b, and d, the screen would display:

# A user is allowed 8 guesses. Remind the user of how many guesses they have left after each round.

# A user loses a guess only when they guess incorrectly. If they guess a letter that is in the computer's word, they do not lose a guess.

# If the user guesses the same letter twice, do not take away a guess. Instead, print a message letting them know they've already guessed that letter and ask them to try again.

# The game will end when the user constructs the full word or runs out of guesses. If the player runs out of guesses, reveal the word to the user when the game ends.

# When a game ends, ask the user if they want to play again. The game begins again if they reply positively.

# Write functions to select a subset of the complete word list.

# Write a function to select a word at random from the word list.

# Write a function to display a word with blanks/letters filled in the appropriate spots.

# Write a function to check if a word has been completely guessed.


# Write other helper functions as necessary to help with the flow of the game.

# Run mystery_word_test.py and ensure you pass all the unit tests.
def main():
    answer = what_level()
    return gameplay_loop(answer)

if __name__ == "__main__":
    main()
