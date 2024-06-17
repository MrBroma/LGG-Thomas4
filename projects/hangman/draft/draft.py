def get_word():
    word = input("Enter your word: ")
    print(f"Your word is {word}.")
    return word

def get_lives():
    live_numbers = int(input("How many lives do you want? "))
    print(f"You have {live_numbers} lives")
    return live_numbers

def get_guess(suggested_letters):
    suggested_letters  = suggested_letters.append(input("Enter a letter to guess: "))
    return suggested_letters


# test of the functions
get_word()
get_lives()
get_guess()



# def assess_guess(secret_word, guessed_letter, lives_left):


# def display_word(secret_word, suggested_letters):


