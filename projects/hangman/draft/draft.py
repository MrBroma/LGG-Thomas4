from typing import List

def get_word() -> str:
    """
    Prompts the user to enter a word to be guessed. Converts the word to lowercase.
    
    Returns:
        str: The word provided by the user in lowercase.
    """
    word = input("Enter your word to be guessed: ").lower()
    print(f"Your word is {word}.")
    return word


def get_lives() -> int:
    """
    Prompts the user to enter the number of lives they want for the game.
    Ensures that the number of lives is a positive integer.
    
    Returns:
        int: The number of lives provided by the user.
    """
    while True:
        try:
            live_numbers = int(input("How many lives do you want? "))
            if live_numbers <= 0:
                print("Please enter a positive number.")
            else:
                print(f"You have {live_numbers} lives")
                return live_numbers
        except ValueError:
            print("Invalid input. Please enter a valid number.")


def get_guess(suggested_letters: List[str]) -> str:
    """
    Prompts the user to guess a letter. Ensures the letter is a single alphabetic character
    and has not been guessed before.
    
    Args:
        suggested_letters (List[str]): A list of letters that have already been guessed.
        
    Returns:
        str: The letter guessed by the user.
    """
    guessed_letter = input("Guess a letter: ").lower()
    while guessed_letter in suggested_letters or len(guessed_letter) != 1 or not guessed_letter.isalpha():
        if guessed_letter in suggested_letters:
            guessed_letter = input(f"You've already guessed {guessed_letter}.\nPlease enter a new letter to guess: ").lower()
        elif len(guessed_letter) != 1 or not guessed_letter.isalpha():
            guessed_letter = input("This is not a valid letter. Enter a single alphabetic character: ").lower()
    return guessed_letter


def asses_guess(secret_word: str, guessed_letter: str, lives_left: int) -> int:
    """
    Assesses the guessed letter against the secret word. If the letter is not in the word,
    it decreases the number of lives left.
    
    Args:
        secret_word (str): The word to be guessed.
        guessed_letter (str): The letter guessed by the user.
        lives_left (int): The current number of lives left.
        
    Returns:
        int: The updated number of lives left.
    """
    if guessed_letter not in secret_word:
        print("The guessed letter is not in the secret word.")
        lives_left -= 1
        print(f"You lose a life, you have {lives_left} lives left.")
    return lives_left


def display_word(secret_word: str, suggested_letters: List[str]) -> bool:
    """
    Displays the current state of the secret word, with guessed letters revealed
    and unguessed letters as underscores. Checks if the word has been fully guessed.
    
    Args:
        secret_word (str): The word to be guessed.
        suggested_letters (List[str]): A list of letters that have been guessed.
        
    Returns:
        bool: True if the word has been fully guessed, False otherwise.
    """
    display = ['_'] * len(secret_word)
    for position in range(len(secret_word)):
        letter = secret_word[position]
        if letter in suggested_letters:
            display[position] = letter
    print(f"{' '.join(display)}")
    return '_' not in display


# Start of the program
if __name__ == "__main__":
    end_of_game = False
    secret_word = get_word()            # Word to guess
    word_length = len(secret_word)      # length of the word to guess
    live_numbers = get_lives()          # get the number of lives
    suggested_letters: List[str] = []   # list of the suggested letters
    lives_left = live_numbers           # Initialize the lives that are left

    # Game launch
    while not end_of_game:
        # ask for a letter to guess
        guess = get_guess(suggested_letters)
        suggested_letters.append(guess)

        # Update of left lives
        lives_left = asses_guess(secret_word, guess, lives_left)

        # Display the word and verify the end of the game
        end_of_game = display_word(secret_word, suggested_letters)

        # Check if the player won or lost
        if end_of_game:
            print("Congratulations! You've guessed the word!")
        elif lives_left == 0:
            end_of_game = True
            print("You've run out of lives. Game over.")
