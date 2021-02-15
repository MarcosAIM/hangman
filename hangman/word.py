'''
class Word:
    attributes:
        word:
            word is a string that contains a word used for constructing the word_dict
            dictionary for fast access to each character in the word and its position
        display_word:
            display_word is a list that contains '_' that means an empty unguessed position
            in the word, it is meant to be displayed to the player as he guesses the word
        word_dict:
            word_dict is a dictionary that contains character:[positions in the word]. each character in the
            word is mapped into the dict and each character is mapped to a list of positions of
            the character.
    functions:
        init_dict:
            init_dict is a function that initializes the word_dict using the word attribute.
            init_dict loops through word and for each character it maps its position.
        fill_display_word:
            fill_display_word is a function that takes as a parameter a char and tries to find it
            in the word_dict,
            if is there it fills display_word using the positions list and the char, then it removes
            the char from the dictionary, and then it returns True signaling it found it.
            if is not there it returns False signaling it did not find the character.

'''
class Word:
    def __init__(self,word:str=''):
        self.word = word # full word
        self.display_word = list('_' for i in range(len(self.word))) # empty word
        self.word_dict = self.init_dict() # dictionary with chars:[positions of char]

    #params: none
    #function maps chars to its position in the word
    #ex cat -> {'c':[0],'a':[1],'t'[2]}
    #returns:dictionary of chars:list of positions of chars
    def init_dict(self):
        if len(self.word) > 0: #non-empty word
            w_d = {}
            for pos,char in enumerate(self.word):
                if char in w_d:
                    w_d[char].append(pos)
                else:
                    w_d[char] = [pos]

            return w_d #mapped chars:list of positions
        else:
            return {} #empty word

    #params:char(a character)
    #function looks for char in word_dict to fill display_word according to
    # the positions of those chars.
    # example dict={'c':[0],'a':[1],'t'[2]}
    #         char='c'
    #         display_word=['c','_','_']
    #returns: True if char found in word_dict
   #          False if char not found in word_dict
    def fill_display_word(self,char):
        if char in self.word_dict: # if found
            for pos in self.word_dict[char]: #loop through list of positions
                self.display_word[pos] = char #replace '_' with char in position
            del self.word_dict[char] # remove char from word_dict
            return True # found
        else:
            return False # not found
