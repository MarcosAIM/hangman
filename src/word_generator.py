from random import choice


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
        return choice(self.word_bank)



def main():
    w = WordGenerator()
    print(w.word_bank)



if __name__ == '__main__':
    main()
