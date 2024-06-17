def get_word() -> str:
    word = input("Enter your word: ")
    print(f"Your word is {word}.")
    return word

def get_lives() -> int:
    live_numbers = int(input("How many lives do you want? "))
    print(f"You have {live_numbers} lives")
    return live_numbers

def get_guess(suggested_letters):
    letter_guess.append(suggested_letters)
    return suggested_letters





######################################""""


# test of the functions
get_word()
get_lives()
letter_guess = input(f"Can you suggested a letter? ")
get_guess(letter_guess)


