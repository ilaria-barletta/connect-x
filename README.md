# Hangman 

This is a Python terminal game addressed to word games lovers. The main goal is to guess the mistery word before loosing all the given lives. The user can input their choices in the terminal, a number, a single letter or the word 'hint' depending on the stage of the game they are in and they will receive a response according to their pick. The game ends with a win or if they use all their lives without completing the word. Some art  has been added so that the hangman results more appealing and user friendly. 

Here is the live version of my project (!!!!!!add link once deployed)

___
## How to play

The game starts with a welcome screen where the user finds the title of the game and 3 options. They can go to the rules, start the game, or exit the game. To start the game the user needs to select the number matching the "start" option. At this point they are provided with new options with different levels as the game consists of 3 difficulty levels. There is an easy level where the word that they need to guess is short (4/5 letters), there is an intermediate level for medium lenght words (7/8 letters) and an hard level for long words (from 10 letters). Once the user selects the preferred level, they are asked once againto confirm their choice before proceeding. When they are happy with their choice, the game can start. The user starts guessing letters and if they haven't used one already they can also ask for a hint so that a random letter from the mistery word is added to the screen for them. The user has only 1 hint per game and 6 lives, one life will be taken from them every time they pick the wrong letter. The game ends either when the user successfully guesses the word while still alive or if they use all their lives and they die. A new set of options with the opportunity to start a new game or exit appears to them after every win/defeat. 

___
## Features

### Existing Features
1. <u>Welcome page :</u><br>
This is the first sceen the user faces when they start the game. They have 3 options: go to the rules, start the game or exit the game. The imput they can provide and will be accepted by the game is stricly one of the number given with the option. If they type in an invalid character an error message will be shown asking them to select a valid option.

![The welcome page consists of the name of the game and 3 options for the user: rules, start or exit the game](images/hangman_start_screen.png)

2. <u>Rules:</u><br>
The rules of the game is a set of instruction that the user can access by selecting the number responding to that option. Here they are informed about the lives they have available and the hint they can use. From the rules screen they then have the option to start the game or exit.
![The rules page is the explanation of the game](images/hangman_rules.png)

3. <u>Exit:</u><br>
This is just a quick message shown to the user when they want to exit the game and leave the terminal. 
![The exit page is a goodbye message to the user when they decide to leave the game](images/hangman_exit_screen.png)

4. <u>Play game:</u><br>
If the user follows the instructions and decides to proceed in order to play a game they will be given the option to select their preferred difficulty level. The game has 3 levels: easy, intermediate and hard. The difference in levels depends on the lenght of the words they need to guess in order to win. Easy has short words (4/5 letters), intermediate has medium lenght words and hard has particularly long/hard words. 
![The game is made of three levels](images/hangman_levels.png)

When they pick their preferred level they are then asked if they are happy with their choice and if they are,the game begins. 

![The user is asked to confirm their level choice](images/hangman_level_confirmation.png)

Once they confirm their choice, the actual game starts. The user sees an hagman structure, with empty spaces where they are asked to put letters. They are asked to give a letter or type `hint` in order to get a little help.The user is allowed to ask for one hint each time they play the game. The hint can be invoked up until the second to last guess hence they can't use it to win the game. As soon as they are no longer allowed to ask for a hint they will be given only the option to enter a letter.

![The game shows an hangman, spaces where to put letters and a request to type a guess or hint ](images/hangman_start_game.png)
![The possiility to request a hint will disappear if the user is just one letter away from completing the word](images/hangman_hint.png)

6. <u>End of game:</u><br>
The game can either end when the user has guessed all the letters not using all the lives hence staying alive or when they haven't completed the word but they have finished their lives. In the first scenario they won the game and a winning message will be displayes, in the second scenario they have lost and will be informed of the same via a "Game over" message. In both cases they will be asked if they want to play again and offered options (start or exit). 
![The game can end either when the user wins or when they used all their lives](images/hangman_win_loose.png)

7. <u>Word sheet:</u>
The words for the game are loaded from https://docs.google.com/spreadsheets/d/1aRm2vaK6hhwBCVrdoNGkP30kM_ICPRoBVCcb7OAEG1s/edit?usp=sharing 

### Future Features
1. Add the option to select a word category to pick from (movies, books, songs)
2. Allow the user to guess the full mistery word at any point during the game. 

___
## Data Model

The game is mainly made of 2 classes: 

### Game class
The game class handles each time the user starts a new game. Every time a new game is started an instance of this class is created. The game class tracks the current word, correct guesses, number of lives, and updates each of these properties every time the user gives a letter. The game class has several functions. The main functions are `play` and `did_win`. The play function handles the main loop of the game. The did win function returns true or false and lets us show the correct screen after a game is over. 
### Words class
The Words class loads a list of words from a google sheet and then stores them in a list according to their difficulty. The Word class has a function to get a random word based on a difficulty, which is used by the game class when a new game starts. 
___
## Testing
The game has been tested both manually and using a validator to make sure no issues are present in the code itself or bugs while playing the game. 

### Validator
I have tested the code using the CI Python Linter and it showed no errors.
![Validator screenshot showing the outcome of python code testing](images/hangaman_code_validator.png)

### Manual testing
I have tested the project manually in each part by playing the game multiple times. I have made sure multiple scenarios were covered as in what kind of input the user can use and what will and won't be accepted. When it comes to the options only one of the options listed will be accepted. The options are indicated with numbers so only a number matching on of the options on screen will let the user process. In any other case an invalid message will be shown with the request to provide a valid option. 
![Input testing for options](images/hangman_%20options_input_validation.png)

When in the game the user needs to provide guesses. This scenario has been extensively tested as well adding validation for all the occurrencies that came to mind: a number, multiple characters, an empty space, a special character or a letter present in the word that had been already guessed before. All these cases will prompt a message asking the user to try again. If the guess is a single letter but capitalized, it will be accepted and automatically converted to lowercase using the lower method. 
![Input testing for guesses](images/hangman_guesses_input_validation.png)


### Fixed Bugs
`1`

**Expected** :
When selecting a level one random word must be shown from the list provided in the googlesheet for that level

**Testing** :
While playing the game for testing I noticed how, at times, the word 'easy' would be randomly selected from the file even if that was not meant to be an actual word but only the category.  

**Result** :
A word not meant to be shown was being instead shown. 

**Fix** :
To fix this I had to skip the first row of words from the sheet (that simply define the level) and are not meant to be part of the game

`2`

**Expected** :
When loosing the game the final complete hangmam needs to be shown to the user. 

**Testing** :
I played the game multiple times loosing on purpose to test it.  

**Result** :
When loosing the game I noticed how the "Game over" message was showing at the right time but the hangman displayed was still incomplete (it still had a missing leg). This was confusing and deceptive as the user, seeing the image, could have been under the impression of having another guess. 

**Fix** :
To solve this I have added `self.print_lives()` so that when they loose the game a full hangman shows too making clear that they have used all the lives. 

`3`

**Expected** :
When only one letter is missing from the word, the user can't ask for a hint as it would automatically result in a win.  

**Testing** :
I played the game multiple times guessing the right words and waiting to ask for a hint when just one letter was missing.  

**Result** :
I was able to ask for a hint when one letter was missing hence winning. This was not the wantend outcome

**Fix** :
To solve this I have modified the code originally created to `has_one_letter_remaining =len(unique_letters) == len(self.correct_guesses) + 1`. The +1 solved the issue. 


### Remaining Bugs 
No bugs remaining

___
## Deployment
The project has been deployed using Heroku. Here are the step to follow for the deployement:

1. Access your Heroku account and click on "create a new app", name the app and select the region before hitting the create app button.   
2. Navigate to the settings tab and create config vars according to the files that need to be made known to heroku for the app to be able to work
3. Add buildpacks in order to install the other dependencies needed. In particular add Python and NodeJS in this order and then hit on Add buildpack
4. Navigate to the deploy section and select Github as deployment method. After confirming that we want to connect to Github we can then search for the Github repository name. Once we find it we can click on connect. 
5. Scroll down and select enable automatic deploys



### Cloning & Forking

___
## Credits

1. The font for the name of the game comes from https://patorjk.com/software/taag/#p=display&f=Graffiti&t=Type%20Something%20

2. The Hangman art (hangmampics) comes from https://gist.github.com/chrishorton/8510732aa9a80a03c829b09f12e20d9c . 
I have then adapted it to my own taste and changed some of the character to completely remove syntax errors highlighted by the validator

3. The structure of the read me has been taken from code institute ultimate battleship walktrough project.