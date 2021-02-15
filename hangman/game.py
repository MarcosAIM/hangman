from hangman.word import Word
from hangman.word_generator import WordGenerator
from hangman.hgman_graphics import hgman_graphics as hgg


#function for clearing command line
def clear():
    from os import system, name
    # windows
    if name == 'nt':
        _ = system('cls')
    # linux mac
    else:
        _ = system('clear')
'''
class Game:
    attributes:
        none

    functions:
        game:
            params:none

            function game implements the game hangman, main loop.
            Press enter to play
            initializes vars, lives,game_state,word,word_gen
            game_state: 0 = in_progress
                        1 = player win
                        -1 = player losses
            while game_state in progress
            ask player for char
            compares char to word
            if char fills word continue
            if char doesnt fill word subtract from lives
            call check_game_state to see wether player wins, loses or continues game

            returns:none
        check_game_state:
            params:none

            function checks wether player lives are zero, or player guessed all chars
            in word, or if none game continues.

            returns: 0 if game continues
                     1 if player wins
                    -1 if player loses.
        print_end_message:
            params:game_state,word

            function prints end game message of winner or loser. if game_state is
            1 it prints winner message, if -1 it prints loser message. It prints
            the actual word in both messages.

            returns:none
'''
class Game:
    def game(self):
        input("Welcome to Tic-Tac-Toe. Press Enter to play")

        #generate word
        lives = 8
        game_state = 0
        word_gen = WordGenerator()
        word = Word(word_gen.pick_word())
        clear() # clear command-line
        while game_state == 0:
            print(f'lives: {lives}') # number of lives left
            print(hgg[-(lives+1)]) # prints hangman graphic
            print(*word.display_word) #prints display_word
            char = input("Guess:") # get one char input

            if word.fill_display_word(char) is False: # check if guess is right
                lives -=1 # lose one life if guess is wrong

            game_state = self.check_game_state(word,lives) # check win,lose,continue
            clear() # clear command-line

        self.print_end_message(game_state,word.word) #print end game message

    def check_game_state(self,word,lives):
        if not word.word_dict: # if dict is empty it means player won
            return 1
        elif lives == 0: # if lives are zero it means player lost
            return -1
        else:
            return 0 # if none of above are true game continues

    def print_end_message(self,game_state,word):
        if game_state == 1:
            print(f"congrats the word is: {word}") # player wins
        elif game_state == -1:
            print(hgg[8])
            print(f"Hanged!! the word is: {word}") # player losses
