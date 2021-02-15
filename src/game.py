from word import Word
from word_generator import WordGenerator
from hgman_graphics import hgman_graphics as hgg
#function for clearing command line
def clear():
    from os import system, name
    # windows
    if name == 'nt':
        _ = system('cls')
    # linux mac
    else:
        _ = system('clear')

class Game:
    def game(self):
        input("Welcome to Tic-Tac-Toe. Press Enter to play")

        #generate word
        lives = 8
        game_state = 0
        word_gen = WordGenerator()
        word = Word(word_gen.pick_word())
        clear()
        while game_state == 0:
            print("Current Word")
            print(f'lives: {lives}')
            print(hgg[-(lives+1)])
            print(*word.display_word)
            char = input("Guess:")

            if word.fill_display_word(char) is False:
                lives -=1

            game_state = self.check_game_state(word,lives)
            clear()
        self.print_end_message(game_state,word.word)

    def check_game_state(self,word,lives):
        if not word.word_dict:
            return 1
        elif lives == 0:
            return -1
        else:
            return 0

    def print_end_message(self,game_state,word):
        if game_state == 1:
            print(f"congrats the word is{word}")
        elif game_state == -1:
            print(hgg[8])
            print(f"Hanged!! the word is {word}")



def main():
    g = Game()
    g.game()




if __name__ == '__main__':
    main()
