import random
from typing import List
from utils.word import word_list
from utils.hangman_art import logo, stages

class Hangman:
    def __init__(self):
        # Initialize the game attributes
        self.possible_words: List[str] = word_list
        self.word_to_find: List[str] = list(random.choice(self.possible_words))
        self.lives: int = 6
        self.correctly_guessed_letters: List[str] = ['_'] * len(self.word_to_find)
        self.wrongly_guessed_letters: List[str] = []
        self.turn_count: int = 0
        self.error_count: int = 0
        self.logo: str = logo
        self.stage: str = stages


    def play(self):
        """
        Prompts the player to guess a letter and updates the game
        """
        print(self.logo)
        while '_' in self.correctly_guessed_letters and self.lives > 0:
            guess = input("Guess a letter: ").lower()

            # Verify the input
            if len(guess) != 1 or not guess.isalpha():
                print("Invalid input. Please enter a single alphabetic character.")
                continue
            
            # Check if the letter has been guessed before
            if guess in self.correctly_guessed_letters or guess in self.wrongly_guessed_letters:
                print(f"You've already guessed {guess}. Try a different letter.")
                continue

            # Update the game based on the guess
            if guess in self.word_to_find:
                for index, letter in enumerate(self.word_to_find):
                    if letter == guess:
                        self.correctly_guessed_letters[index] = guess
                print(f"Good guess! The letter {guess} is in the word.")
            else:
                self.wrongly_guessed_letters.append(guess)
                self.lives -= 1
                self.error_count += 1
                print(f"Wrong guess! The letter {guess} is not in the word. Lives left: {self.lives}")

            # Increment the turn count by 1
            self.turn_count += 1

            # Print the current state of the game
            self.print_game_state()

            # Check if the game is over
            if self.lives == 0:
                self.game_over()
                return
            elif '_' not in self.correctly_guessed_letters:
                self.well_played()
                return

    def start_game(self):
        """
        Starts the game and keeps it running until it's over.
        """
        self.play()

    def game_over(self):
        """
        Prints a game over message and stops the game.
        """
        print("Game over...")
    
    def well_played(self):
        """
        Prints a message if the player successfully guesses the word.
        """
        guessed_word = ''.join(self.word_to_find)
        print(f"You found the word: {guessed_word} in {self.turn_count} turns with {self.error_count} errors!")

    def print_game_state(self):
        """
        Prints the current state of the game including the guessed letters, lives left,
        errors made, and turns played.
        """
        print(f"Correctly guessed letters: {' '.join(self.correctly_guessed_letters)}")
        print(f"Wrongly guessed letters: {' '.join(self.wrongly_guessed_letters)}")
        print(f"Lives left: {self.lives}")
        print(f"Errors made: {self.error_count}")
        print(f"Turns played: {self.turn_count}")
        print(self.stage[self.lives])

