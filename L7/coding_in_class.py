
# generator function I created yesterday

def my_gen(sentence):
    n = 0
    seperate = sentence.split()
    max_len = len(seperate)
    while n < max_len:
        # yield is the keyword needed to make this a generator
        # use of the yield gives this __iter__ and __next__ methods without having to write out all that ugly notation
        yield seperate[n]
        n += 1

'''
When I use my generator function and run the next method on it, after it has exausted the iterable, it will 
throw an error and won't allow me to print it again.

It throws the error: StopIteration
'''

sentence_2 = my_gen('My name is Nasian')
print(next(sentence_2))
print(next(sentence_2))
print(next(sentence_2))
# after this one it will throw an error
print(next(sentence_2))
print(next(sentence_2))
print(next(sentence_2))

############################################
############################################
############################################

'''
I had to copy the function over, as it processed the next in the sentence_2 which was left as Nasian and it
kept cycling over Nasian.

Very interesting behaviour!
'''

def my_gen(sentence):
    n = 0
    seperate = sentence.split()
    max_len = len(seperate)
    while n < max_len:
        # yield is the keyword needed to make this a generator
        # use of the yield gives this __iter__ and __next__ methods without having to write out all that ugly notation
        yield seperate[n]
        n += 1

sentence_2 = my_gen('My name is Nasian')

import itertools

cycle_def = itertools.cycle(sentence_2)
print(next(cycle_def))
print(next(cycle_def))
print(next(cycle_def))
print(next(cycle_def))
print(next(cycle_def))
print(next(cycle_def))
print(next(cycle_def))
print(next(cycle_def))

from itertools import cycle
# remove the itertools as it throws an error, you have imported cycle - no need to reference the module
counter = cycle(['my', 'name', 'is', 'nasian'])

print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))

'''
By using the cycle itertools, we can overcome this issue as it allows us to cycle through the iterable and 
does not throw an error. Instead, it cycles through and keeps printing the iterable.

This is different as we able to use the cycle itertool on the generator function I have produced and keep using the
next method on the cycle itertool, and it won't throw a StopIteration error.
'''

# or if you want to just import all of itertools and call it like so

import itertools
# remove the itertools as it throws an error, you have imported cycle - no need to reference the module
counter = itertools.cycle(['my', 'name', 'is', 'nasian'])

print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))

'''
Simple example from class
'''

from itertools import cycle

counter = cycle(['my', 'name', 'is', 'nasian'])

print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))