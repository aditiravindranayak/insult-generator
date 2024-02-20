from random import randint

def get_random_word(words):
    return words[randint(0, len(words) - 1)]

opinion = ['stupid', 'weird', 'boring', 'witless']
size = ['huge', 'big', 'little', 'tiny']
quality = ['scabby', 'spotty', 'saggy', 'ugly']
age = ['old', 'immature', 'childish', 'decrepit']
shape = ['fat', 'skinny', 'clunking', 'lanky']
noun = ['idiot', 'halfwit', 'coward', 'crybaby']

sentence = 'You {}, {}, {}, {}, {} {}'.format(
    get_random_word(opinion),
    get_random_word(size),
    get_random_word(quality),
    get_random_word(age),
    get_random_word(shape),
    get_random_word(noun)
)

print(sentence)
