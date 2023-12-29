import random

# function which random chooses words 
def choose_word():
    words = ["python", "hangman", "programming", "computer", "science","game", "coding"]
    return random.choice(words)

# function that displays words
def display_board(chosen_word, guessed):
    display = " "
    for letter in chosen_word:
        if letter in guessed:
            display += f"{letter} "
        else:
            display += "_ "
    return display

# main game loop
def hangman():
    word = choose_word()
    guessed_letters = []
    attempts_left = 6

    print("Welcome to Hangman!")

    print(display_board(word, guessed_letters))

    while attempts_left > 0 :

        guess = input("\n Guess a letter: ").lower()
        print(" The Number of attempts left are: ",attempts_left)

        if guess.isalpha() and len(guess) == 1: # keep looping until the user wins or loses
           
            if guess in guessed_letters:
                print("Already Gussed")

            elif guess in word:
                    guessed_letters.append(guess)
                    print(f"\nGood job, {guess} is in the word.")
            
            else:
                attempts_left -= 1
                print(f"\nWrong choice. You have {attempts_left} attempts left.")
        
        else:
            print("Invalid Input")

        

        print(display_board(word, guessed_letters))

        if word==guessed_letters:
            break

    if "-" in display_board(word, guessed_letters):
        print("you guessed it")
    
    if "-" not in display_board(word, guessed_letters):
        print("you have not  guessed it")
     
if __name__ == "__main__":
    hangman()