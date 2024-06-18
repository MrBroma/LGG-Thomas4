def get_word() -> str:
    word = input("Enter your word: ")
    print(f"Your word is {word}.")
    return word


def get_lives() -> int:
    live_numbers = int(input("How many lives do you want? "))
    print(f"You have {live_numbers} lives")
    return live_numbers


def get_guess(suggested_letters):
    guess = input("Enter a letter to guess: ")
    suggested_letters.append(guess)
    print(suggested_letters)
    return guess


# def asses_guess(secret_word, guessed_letter, lives_left):


# def display_word(secret_word, suggested_letters):


# Start of the program
if __name__ == "__main__":
    # variable for the program
    suggested_letters = []
    
    # call of the functions
    get_word()
    get_lives()
    get_guess(suggested_letters)







######################################""""


# test of the functions
# get_word()
# get_lives()


# user_letter = ['a', 'f', 'k', 'p']
# user_guess = get_guess(user_letter)

# print(user_letter)
