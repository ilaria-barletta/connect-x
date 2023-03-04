# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

def welcome_to_hangman():
    '''This is the main function that is called first when the game starts'''
    print("Welcome to Hangman")
    options = {
        "Rules": rules,
        "Start": start,
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


def exit_hangman():
    print("Exit")


def rules():
    print("Rules")


def start():
    print("Start")


welcome_to_hangman()

