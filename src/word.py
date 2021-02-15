class Word:
    def __init__(self,word:str=''):
        self.word = word
        self.display_word = list('_' for i in range(len(self.word)))
        self.word_dict = self.init_dict()



    def init_dict(self):
        if len(self.word) > 0:
            w_d = {}
            for pos,char in enumerate(self.word):
                if char in w_d:
                    w_d[char].append(pos)
                else:
                    w_d[char] = [pos]

            return w_d
        else:
            return {}

    def fill_display_word(self,char):
        if char in self.word_dict:
            for pos in self.word_dict[char]:
                self.display_word[pos] = char
            del self.word_dict[char]
            return True
        else:
            return False
