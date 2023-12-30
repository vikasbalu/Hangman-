import random
import json

# This section is used to import the json file that contain several words 
f = open('words_dictionary.json')
data = json.load(f)
just_words = list(data.keys())

# This section is to choose a word at random from that json file
def choose_word():
    words = just_words
    return random.choice(words)

# This function block is to display the board in the terminal 
def display_word(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += "_"
    return display

# The main block where the actua game takes place
def hangman():
    print("Welcome to Hangman!")
    word_to_guess = choose_word()
    print(word_to_guess)
    guessed_letters = []
    max_attempts = 6
    attempts = 0

    while True:
        current_display = display_word(word_to_guess, guessed_letters)
        print("Current word:", current_display)
        print("Guessed letters:", guessed_letters)

        guess = input("Guess a letter: ").lower()

        if guess in guessed_letters:
            print("You already guessed that letter. Try again.")
            continue

        guessed_letters.append(guess)

        if guess not in word_to_guess:
            attempts += 1
            print("Incorrect guess. Attempts left:", max_attempts - attempts)
            if attempts == max_attempts:
                print("Sorry, you ran out of attempts. The word was:", word_to_guess)
                break
        else:
            print("Good guess!")

        if set(guessed_letters) >= set(word_to_guess):
            print("Congratulations! You guessed the word:", word_to_guess)
            break

if __name__ == "__main__":
    hangman()

 