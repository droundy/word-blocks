#!/usr/bin/python3

import sys
from collections import defaultdict

with open('words.four') as f:
    words = list(filter(lambda x: len(x) == 4, map(lambda x: x.strip(), f.readlines())))
with open('basic.four') as f:
    basic = sorted(list(filter(lambda x: len(x) == 4, map(lambda x: x.strip(), f.readlines()))))

print len(words)
wordset = set(words)
first2 = set(map(lambda x: x[:2], words))
first3 = set(map(lambda x: x[:3], words))

maps = []
for i in range(4):
    maps.append(defaultdict(list))
for w in words:
    for i in range(4):
        maps[i][w[i]].append(w)

def two_okay(h0,h1):
    return all(map(lambda i: h0[i]+h1[i] in first2,range(4)))
def three_okay(h0,h1,h2):
    return all(map(lambda i: h0[i]+h1[i]+h2[i] in first3,range(4)))
def four_okay(h0,h1,h2,h3):
    return all(map(lambda i: h0[i]+h1[i]+h2[i]+h3[i] in wordset,range(4)))

def tuples_with_word(i, v0):
    tuples = []
    for h0 in maps[i][v0[0]]:
        for h1 in filter(lambda h1: two_okay(h0,h1), maps[i][v0[1]]):
            for h2 in filter(lambda h2: three_okay(h0,h1,h2), maps[i][v0[2]]):
                for h3 in filter(lambda h3: four_okay(h0,h1,h2,h3), maps[i][v0[3]]):
                    tuples.append((h0[0]+h1[0]+h2[0]+h3[0],
                                   h0[1]+h1[1]+h2[1]+h3[1],
                                   h0[2]+h1[2]+h2[2]+h3[2],
                                   h0[3]+h1[3]+h2[3]+h3[3]))
    return tuples

basicmaps = []
for i in range(4):
    basicmaps.append(defaultdict(list))
for w in basic:
    for i in range(4):
        basicmaps[i][w[i]].append(w)
def tuples_with_basic(i, v0):
    tuples = []
    for h0 in maps[i][v0[0]]:
        for h1 in filter(lambda h1: two_okay(h0,h1), basicmaps[i][v0[1]]):
            for h2 in filter(lambda h2: three_okay(h0,h1,h2), basicmaps[i][v0[2]]):
                for h3 in filter(lambda h3: four_okay(h0,h1,h2,h3), basicmaps[i][v0[3]]):
                    tuples.append((h0,h1,h2,h3))
    return tuples

tuples = []
for v0 in basic:
    for i in range(4):
        tuples += tuples_with_word(i,v0)
    print v0,len(tuples)
tuples = sorted(list(set(tuples)))
# tuples = tuples_with_word(1,'food')

print 'found', len(tuples)

def tuple_words(t):
    return [t[0], t[1], t[2], t[3],
            t[0][0]+t[1][0]+t[2][0]+t[3][0],
            t[0][1]+t[1][1]+t[2][1]+t[3][1],
            t[0][2]+t[1][2]+t[2][2]+t[3][2],
            t[0][3]+t[1][3]+t[2][3]+t[3][3]]

def has_word(triple, w):
    return w in tuple_words(triple)

def tuples_with(w, tuples):
    return list(filter(lambda t: has_word(t,w), tuples))

def has_letter(l, triple):
    return l in t[0]+t[1]+t[2]+t[3]
def count_letters(letters, triple):
    return len(list(filter(lambda x: has_letter(x,triple), letters)))

def tuples_with_both(w1,w2):
    return list(filter(lambda t: has_word(t,w1) and has_word(t,w2), triples))

def tuples_with_at_least(n, words, triples):
    return list(filter(lambda t: len(list(filter(lambda w: has_word(t,w), words))) >= n,
                       triples))

def alphabetical(l, triples):
    return list(filter(lambda t: l[0] in t[0] and l[1] in t[1]
                             and l[2] in t[2] and l[3] in t[3], triples))

def chunks(l, n):
    """Yield successive n-sized chunks from l."""
    for i in range(0, len(l), n):
        yield l[i:i + n]

def one_word(n, word, triples):
    return list(filter(lambda t: t[n] == word, triples))

def pretty_tuples(tuples):
    for line in chunks(tuples, 17):
        for i in range(4):
            for t in line:
                sys.stdout.write(t[i])
                sys.stdout.write(' ')
            print
        print

best_list = set(['mama','dada','papa'])
common_list = set(['food'])

# for three in ['abc', 'def', 'ghi', 'jkl', 'mno', 'pqr', 'stu', 'vwx', 'yza', 'zoo']:
#     print(three)
#     pretty_triples(alphabetical(three, triples))

print '6 common'
pretty_tuples(tuples_with_at_least(6, basic, tuples))

# print('1 best and 4 only common')
# pretty_triples(triples_with_at_least(1, best_list,
#                                      triples_with_at_least(5, common_list,triples)))
# print('2 best and 2 only common')
# pretty_triples(triples_with_at_least(2, best_list,
#                                      triples_with_at_least(4, common_list,triples)))

# print('2 best and 1 only common')
# pretty_triples(triples_with_at_least(2, best_list,
#                                      triples_with_at_least(3, common_list,triples)))

nicest = [#('zood','owld','oldd','food'),
]
pretty_tuples(nicest)

letters_left = set('abcdefghijklmnopqrstuvwxyz')

for t in nicest:
    print('... contains',count_letters(letters_left, t),'new letters:')
    pretty_tuples([t])
    for w in t:
        for l in w:
            if l in letters_left:
                #print('removing', l)
                letters_left.remove(l)
pretty_tuples(nicest)
print('remaining:', len(letters_left), letters_left)
need_list = set([])
for l in letters_left:
    need_list.update(filter(lambda x: l in x, common_list))
print(need_list)

new_list = set([])
for l in letters_left:
    new_list.update(filter(lambda x: l in x, words))
#print(new_list)

good_stuff = []
for t in tuples_with_at_least(6, basic, tuples): # one_word(2, 'fox', tuples): # tuples:
    if count_letters(letters_left, t) >= 3: # and has_letter('q', t):
        good_stuff.append(t)
pretty_tuples(good_stuff)

pretty_tuples(one_word(1,'miri',tuples))
# print('bot dad')
# pretty_tuples(one_word(1,'apes',one_word(0, 'dada', tuples)))
