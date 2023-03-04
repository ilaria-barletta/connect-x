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
            print(f"Invalid, please select a value between 0 and {max_option - 1}")
            choose_option(options)
    except ValueError:
        # The -1 fixes the issue caused by the options starting from 0
        print(f"Invalid, please select a value between 0 and {max_option - 1}")
        choose_option(options)


def rules():
    print("Rules")
    options = {
        "Start": pick_level,
        "Exit": exit_hangman
    }
    choose_option(options)
    

def pick_level():
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
    print(f"You have selected {level} game, happy to proceed?")
    options = {
        "Yes": lambda: start_game_with_level(level), 
        "No": pick_level, 
    }
    choose_option(options)


def start_game_with_level(level):
    print(f"Starting {level} game")


def exit_hangman():
    print("Exit")


welcome_to_hangman()

