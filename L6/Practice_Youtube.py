'''
Practicisng the coding problem from Corey Schafer's YouTube channel on creating your own iterators
'''

# create class sentence
class Sentence:

    # specified the type of data str is by :object
    def __init__(self, str):
        self.str = str
        self.n = 0
        self.seperate = self.str.split()
        print(self.seperate)
        self.max_len = len(self.seperate)
        print(self.max_len)

    # you need the __iter__ and __next__ methods for an iterable

    def __iter__(self):
        return self

    def __next__(self):
        if self.n >= self.max_len:
            raise StopIteration

        index = self.n
        result = self.seperate[index]
        self.n += 1
        return result


    # def seperate_string(self):
    #     super().__init__(str)
    #     self.seperate = self.str.split()
    #     return self.seperate
    #
    # def my_gen(self):
    #     n = len(self.seperate)
    #     print(self.str[n])
    #     yield n


my_sentence = Sentence('This is a test')

# my_sentence = Sentence.my_gen(my_sentence)
# create a generator for this function
for word in my_sentence:
    print(word)

