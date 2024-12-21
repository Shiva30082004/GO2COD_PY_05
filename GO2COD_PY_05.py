'''
GO2COD PYTHON PROGRAMMING INTERNSHIP
TASK 05 : A HANGMAN GAME
NAME: SHIV BHAVSAR

This program will start with the random word with some unknown letters in it and it will
ask the user to guess those unknown letters to reveal the word with limited no. of attempts.
'''

import random

# a function that play a Hangman game and has two input parameters for list of words and max no. of attempts  
def hangman_game(word_list, max_attempts):
    
    # select a random word from the list
    chosen_word = random.choice(word_list).lower()
    guessed_letters = set()
    attempts_left = max_attempts

    # reveal some letters of the chosen word initially
    num_to_reveal = max(1, len(chosen_word) // 2)
    revealed_indices = random.sample(range(len(chosen_word)), k=num_to_reveal)
    word_state = []

    for i in range(len(chosen_word)):
        if i in revealed_indices:
            word_state.append(chosen_word[i])
        else:
            word_state.append('_')

    # prompt the user
    print("Welcome to the Hangman Game!")
    print("Guess the word:", ' '.join(word_state))

    
    while attempts_left > 0:
        # get the player's guess
        guess = input("Enter a letter: ").lower()

        # validate input
        if (len(guess) != 1) or (not guess.isalpha()):
            print("Please enter a single valid letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter. Try again.")
            continue

        # add guess to the set of guessed letters
        guessed_letters.add(guess)

        if guess in chosen_word:
            print("Good job! ",guess," is in the word.")

            # update the word state
            for i, letter in enumerate(chosen_word):
                if letter == guess:
                    word_state[i] = guess
            # deaccumulate the no. of attempts
            attempts_left -= 1

        else:
            print("Sorry, ",guess," is not in the word.")
            # deaccumulate the no. of attempts
            attempts_left -= 1

        # display the current state of the word
        print("Word:", ' '.join(word_state))
        print("Attempts left: ",attempts_left)
        print(" ")


        # check if the player has guessed the word
        if '_' not in word_state:
            print("Congratulations! You guessed the word:", chosen_word)
            return

    print("Game over! The word was:", chosen_word)

# a main function
def main():
    # a word list
    words = ["animal","basket","castle","desert","farmer","garden","hammer","island","jungle","kitten",
             "ladder","market","nature","orange","planet","rocket","school","tunnel","velvet","window"]

    # call the function and start the game with a word list and a maximum of 6 attempts
    hangman_game(words, max_attempts=6)

main()
