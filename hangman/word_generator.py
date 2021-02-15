from random import choice

'''
class Word:
    attributes:
        word_bank:
            list of words for use in hangman game.

    functions:
        pick_word:
            params:none
            returns:random word chosen from word_bank
'''
class WordGenerator:
    def __init__(self):
        self.word_bank = ['resolution',
                          'posture',
                           'time',
                           'tail',
                           'do',
                           'difficult',
                           'craft',
                           'sanctuary',
                           'table',
                           'barrel',
                           'recommendation',
                           'chance',
                           'hospital',
                           'west',
                           'hypnothize',
                           'translate',
                           'queen',
                           'riot',
                           'crosswalk',
                           'industry', ]

    def pick_word(self):
        return choice(self.word_bank) #random word
