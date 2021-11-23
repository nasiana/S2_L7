'''
Practicisng the coding problem from Corey Schafer's YouTube channel on creating your own iterators
'''

# creating an iterable with a class

class Sentence:

    # i originally used str as my second argument but this is bad practice as str is how you declare a string in python
    def __init__(self, sentence):
        self.sentence = sentence
        self.n = 0
        self.seperate = self.sentence.split()
        self.max_len = len(self.seperate)

    # you need the __iter__ and __next__ methods to create an object that is an iterable

    def __iter__(self):
        return self

    def __next__(self):
        if self.n >= self.max_len:
            raise StopIteration

        index = self.n
        result = self.seperate[index]
        self.n += 1
        return result

# creating an iterable with a generator function

def my_gen(sentence):
    n = 0
    seperate = sentence.split()
    max_len = len(seperate)
    while n < max_len:
        # yield is the keyword needed to make this a generator
        # use of the yield gives this __iter__ and __next__ methods without having to write out all that ugly notation
        yield seperate[n]
        n += 1

# iterable using the class method
my_sentence = Sentence('This is a test')

for word in my_sentence:
    print(word)

print('\n BREAK \n')

# iterable using the generator method
sentence_2 = my_gen('This is a test')

for word in sentence_2:
    print(word)