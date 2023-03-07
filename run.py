import random  # this is needed to pick a random word
import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('hangman_words')


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
    game = Game(level, words)
    game.play()


def exit_hangman():
    '''This function prints a message to the user when they exit the game'''
    print("Exit")


class Words:
    '''This class gets a random word as per selected level from
    the google sheet'''
    def __init__(self):
        worksheet = SHEET.worksheet('words')
        data = worksheet.get_all_values()
        self.easy_words = []
        self.intermediate_words = []
        self.hard_words = []
        for i, row in enumerate(data):
            #  this is to skip the first row in the
            #  sheet.that row defines the levels.
            if i == 0:  
                continue
            self.easy_words.append(row[0])
            self.intermediate_words.append(row[1])
            self.hard_words.append(row[2])

    def get_random_word(self, level):
        '''This function returns a random word from the words sheet'''
        if level == "easy":
            return random.choice(self.easy_words)
        if level == "intermediate":
            return random.choice(self.intermediate_words)
        if level == "hard":
            return random.choice(self.hard_words)



class Game:
    '''This class handles running the game'''
    def __init__(self, level, words):
        # this will convert upper cases to lower cases
        self.word = words.get_random_word(level).lower() 
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

    def get_letter(self):
        '''This function asks the user for a letter and returns
        it if it is valid and it hasn't been guessed before.
        If user enters an uppercase letter, it will be accepted and converted'''
        letter = input("Please write a letter: ").lower()
        if letter in self.correct_guesses:  # letter already entered
            print(f"You have already guessed {letter}, try again")
            return self.get_letter()
        elif letter == "":  # user enters nothing
            print("You need to enter a letter, try again")
            return self.get_letter()
        elif len(letter) > 1:  # user enters more than 1 letter
            print("You need to enter only one letter, try again")
            return self.get_letter()
        elif not letter.isalpha():  # check if character is an alphabet letter
            print("You need to enter a letter [a-z], try again")
            return self.get_letter()
    
        return letter 
          
    def play(self):
        '''This is the main function of the game. It keeps asking
        the user to guess and update the game until it's over'''
        while not self.game_over():
            self.print_lives()
            self.print_word()
            letter = self.get_letter()
            self.update_game(letter)


# load words when the program starts 
words = Words()
welcome_to_hangman()


