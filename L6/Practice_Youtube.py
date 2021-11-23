'''
Practicisng the coding problem from Corey Schafer's YouTube channel on creating your own iterators
'''

# create class sentence
class Sentence:

    # specified the type of data str is by :object
    def __init__(self, str: object):
        self.str = str

    def seperate_string(self):
        super().__init__(str)
        self.seperate = self.str.split()

    def

my_sentence = Sentence('This is a test')

# create a generator for this function
for word in my_sentence:
    print(word)