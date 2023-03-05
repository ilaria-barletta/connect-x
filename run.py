# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

def welcome_to_hangman():
    '''This is the main function that is called first when the game starts'''
    print("Welcome to Hangman")
    options = {
        "Rules": rules,
        "Start": pick_level,
        "Exit": exit_hangman
    }
    choose_option(options)

    
def choose_option(options):
    '''This function takes a dictionary of options, lets the user choose one
    and validates it'''
    for index, key in enumerate(options):
        print(f'{index}) {key}')

    max_option = len(options.keys())
    option = input("Please choose an option: ")
    try:
        option = int(option)
        if option >= 0 and option < max_option: 
            key = list(options.keys())[option]
            value = options[key]
            value()
        else:
            # The -1 fixes the issue caused by the options starting from 0
            print(f"Invalid,select a value between 0 and {max_option - 1}")
            choose_option(options)
    except ValueError:
        # The -1 fixes the issue caused by the options starting from 0
        print(f"Invalid,select a value between 0 and {max_option - 1}")
        choose_option(options)


def rules():
    '''This function handles the rules of the game and provides the user with 
    2 options: start the game or exit the game'''
    print("Rules")
    options = {
        "Start": pick_level,
        "Exit": exit_hangman
    }
    choose_option(options)
    

def pick_level():
    '''This function is so that the user can pick a difficulty-level for the 
    game. It contains in-line lambda fuctions for each one of the 
    levels available'''
    print("Start")
    options = {
        # lambda here is to avoid repetitions in defining functions
        # this same result could be obtained with: 
        # def easy_game():
        #   game_with_level("easy")
        # but we would need a function for each level
        "Easy": lambda: confirm_game_with_level("easy"),
        "Intermediate": lambda: confirm_game_with_level("intermediate"),
        "Hard": lambda: confirm_game_with_level("hard"),
        "Rules": rules,
        "Exit": exit_hangman
    }
    choose_option(options)


def confirm_game_with_level(level):
    '''This function confirms the level selected by the user and lets
    them decide if they want to continue or go back and make a 
    different choice'''
    print(f"You have selected {level} game, happy to proceed?")
    options = {
        "Yes": lambda: start_game_with_level(level), 
        "No": pick_level, 
    }
    choose_option(options)


def start_game_with_level(level):
    '''This function starts the actual game according to the level selected'''
    print(f"Starting {level} game")


def exit_hangman():
    '''This function prints a message to the user when they exit the game'''
    print("Exit")


welcome_to_hangman()


class Game:
    '''This class handles running the game'''
    def __init__(self, level):
        self.word = "bazinga"
        self.lives = 6
        self.correct_guesses = []
   
    def print_lives(self):
        '''This function prints the remaining lives'''
        print(f"Remaining lives: {self.lives}")

    def print_word(self):
        '''This function prints the word, if the guessed letter is
        present in the word, it shows the letter, if not, it shows an
        empty space'''
        for letter in self.word:
            if letter in self.correct_guesses:
                print(letter, end=" ")
            else:
                print("-", end=" ")
        print("\n")

    def update_game(self, letter):
        '''This function updates the game after a guess.'''
        if letter in self.word:
            self.correct_guesses.append(letter)
        else:
            self.lives = self.lives - 1

    def has_guessed_all_letters(self):
        '''This function returns true if the user has guessed 
        all the letters'''
        unique_letters = set(self.word)
        if len(unique_letters) == len(self.correct_guesses):
            return True
        else:
            return False

    def game_over(self):
        '''This function returns true if there are no more
        lives or if the user has guessed all the right letters'''
        if self.lives == 0 or self.has_guessed_all_letters():
            return True
        else:
            return False

    def did_win(self):
        '''This function returns true if the user won the game'''
        if self.lives > 0 and self.has_guessed_all_letters():
            return True
        else:
            return False

    