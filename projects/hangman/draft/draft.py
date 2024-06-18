from typing import List

def get_word() -> str:
    word = input("Enter your word to be guessed: ")
    print(f"Your word is {word}.")
    return word


def get_lives() -> int:
    live_numbers = int(input("How many lives do you want? "))
    print(f"You have {live_numbers} lives")
    return live_numbers


def get_guess(suggested_letters: List[str]) -> List[str]:
    guess_letter = input("Enter a letter to guess: ")
    while not guess_letter.isalpha() or len(guess_letter) != 1 or guess_letter in suggested_letters:
        if not guess_letter.isalpha():
            guess_letter = input("This is not a letter\n Enter a letter to guess: ")
        elif len(guess_letter) != 1:
            guess_letter = input("The char is too long\n Enter a letter to guess: ")
        elif guess_letter in suggested_letters:
            guess_letter = input("The char is already in the list\n Enter a letter to guess: ")
        else:
            print("Error")
    suggested_letters.append(guess_letter)
    return(suggested_letters)


def asses_guess(secret_word: str, guessed_letter: str, lives_left: int) -> int:
    if guessed_letter not in secret_word:
        lives_left -= 1
    return lives_left


def display_word(secret_word: str, suggested_letters: str): 
    hidden_word = list("_" * len(secret_word))
    for i, letter in enumerate(secret_word):
        if suggested_letters != "_" and suggested_letters == letter:
            hidden_word[i] = letter
    print(' '.join(hidden_word))
    

# Start of the program
if __name__ == "__main__":
    game = True
    # define the secret word with the function get_word()
    secret_word = get_word().upper()
    # choose the number of lives of the player
    number_lives = get_lives()
    
    while game:
        # asking the player to guess a letter assign to suggested letter
        guessed_letter = ''.join(get_guess([])).upper()

        # check if the guess is correct and return number of lives
        lives_left = asses_guess(secret_word, guessed_letter, number_lives)

        # display the secret word hidden with hiphen
        display_word(secret_word, guessed_letter)

