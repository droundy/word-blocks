#!/usr/bin/python3

import sys
from collections import defaultdict

with open('words') as f:
    words = list(filter(lambda x: len(x) == 3, map(lambda x: x.strip(), f.readlines())))

for x in ['hie','sis','wen', 'rev', 'zit','zed', 'adz',
          'fer','rep','ugh','erg','fag','ups','ads','mes','née','poi',
          'sos','brr','bra','err','sex','ism',
]:
    if x in words:
        words.remove(x)
words.append('quo')
print(len(words))
wordset = set(words)
first_two_set = set(map(lambda x: x[:2], words))

map0 = defaultdict(list)
map1 = defaultdict(list)
map2 = defaultdict(list)
for w in words:
    map0[w[0]].append(w)
    map1[w[1]].append(w)
    map2[w[2]].append(w)

count=0

triples = []

for v0 in words:
    for h0 in map0[v0[0]]:
        for h1 in map0[v0[1]]:
            if h0[1]+h1[1] in first_two_set and h0[2]+h1[2] in first_two_set:
                for h2 in map0[v0[2]]:
                    if h0[1]+h1[1]+h2[1] in wordset and h0[2]+h1[2]+h2[2] in wordset:
                        triples.append((h0,h1,h2))
                        count += 1

def triple_words(t):
    return [t[0], t[1], t[2],
            t[0][0]+t[1][0]+t[2][0],t[0][1]+t[1][1]+t[2][1],t[0][2]+t[1][2]+t[2][2]]

def has_word(triple, w):
    return w in triple_words(triple)

def triples_with(w):
    return list(filter(lambda t: has_word(t,w), triples))

def has_letter(l, triple):
    return l in t[0]+t[1]+t[2]
def count_letters(letters, triple):
    return len(list(filter(lambda x: has_letter(x,triple), letters)))

def triples_n_letters(n, letters, triples):
    return list(filter(lambda t: count_letters(letters, t) >= n, triples))

def triples_with_both(w1,w2):
    return list(filter(lambda t: has_word(t,w1) and has_word(t,w2), triples))

def triples_with_at_least(n, words, triples):
    return list(filter(lambda t: len(list(filter(lambda w: has_word(t,w), words))) >= n,
                       triples))

def alphabetical(l, triples):
    return list(filter(lambda t: l[0] in t[0] and l[1] in t[1] and l[2] in t[2], triples))

def chunks(l, n):
    """Yield successive n-sized chunks from l."""
    for i in range(0, len(l), n):
        yield l[i:i + n]

def one_word(n, word, triples):
    return list(filter(lambda t: t[n] == word, triples))

def pretty_triples(triples):
    for line in chunks(triples, 20):
        for t in line:
            sys.stdout.write(t[0])
            sys.stdout.write(' ')
        print()
        for t in line:
            sys.stdout.write(t[1])
            sys.stdout.write(' ')
        print()
        for t in line:
            sys.stdout.write(t[2])
            sys.stdout.write(' ')
        print()
        print()

best_list = set(['mom','dad','you',
                 'hug','pet','her',
                 'wag','dog','cat','mew','ruf',
                 ])
common_list = set(['mom','dad','you',
                   'and','for','run','see','red','not',
                   'all','any','are','bed','box','boy',
                   'bad','bye','can','cup',
                   'big','can','the','car','our','eat',
                   'fly','for','get','had','has','her',
                   'him','his','hot','how','huh','new',
                   'man','may',
                   'all', 'and', 'any', 'are', 'bad', 'bet', 'big', 'box', 'boy', 'bye',
                   'can', 'car', 'cat', 'cup', 'cut', 'day', 'did', 'dog', 'dry', 'eat',
                   'eve', 'fly', 'for', 'get', 'had', 'has', 'her', 'him', 'his', 'hot',
                   'how', 'huh', 'hum', 'let', 'lot', 'man', 'may', 'mom', 'new', 'not',
                   'off', 'old', 'one', 'our', 'out', 'pet', 'put', 'red', 'run', 'saw',
                   'say', 'see', 'she', 'sit', 'the', 'too', 'top', 'try', 'two', 'use',
                   'was', 'way', 'who', 'why', 'yes', 'yet', 'you','zoo',
                   'cat','dog','hat', 'cow', 'wag',
                   'bat','hat','mat','pat','rat','sat',
                   'dog','fog','log','hog','big','dig','pig','fit','dot','pot','tag',
                   'zig','zag',
                   'cut','nut','bug','hug','tug','jam',
                   'one', 'two',
])

# for three in ['abc', 'def', 'ghi', 'jkl', 'mno', 'pqr', 'stu', 'vwx', 'yza', 'zoo']:
#     print(three)
#     pretty_triples(alphabetical(three, triples))

# print('5 common')
# pretty_triples(triples_with_at_least(5, common_list, triples))

# print('6 common')
# pretty_triples(triples_with_at_least(6, common_list, triples))

# print('1 best and 4 only common')
# pretty_triples(triples_with_at_least(1, best_list,
#                                      triples_with_at_least(5, common_list,triples)))
# print('2 best and 2 only common')
# pretty_triples(triples_with_at_least(2, best_list,
#                                      triples_with_at_least(4, common_list,triples)))

# print('2 best and 1 only common')
# pretty_triples(triples_with_at_least(2, best_list,
#                                      triples_with_at_least(3, common_list,triples)))

# print('3 best')
# pretty_triples(triples_with_at_least(3, best_list, triples))

# print('2 very best')
# pretty_triples(triples_with_at_least(2, ['mom','dad'], triples))

nicest = [('zoo','owl','old'),#('zoo','odd','ode'),
          ('sip','ice','tea'),
          ('ark','hue','any'),
          ('jog','aha','mob'),
          ('oaf','axe','key'),
          ('jig','ivy','gym'),
          #('dog','are','yet'),
          #('mom','aha','not'),
          #('cub','use','pet'),
          #('hat','ash','she'),
          #('mom','one','pet'),
          #('cat','use','the'),
          #('two','had','eye'),
]
nicest = [('sip','ice','tea'),
          ('zoo','owl','old'),
          ('qua','urn','any'),
          ('bag','axe','hem'),
          ('fed','eve','new'),
          ('jay','aha','yak'),
]
pretty_triples(nicest)
nicest = [('sip','ice','tea'),
          ('zoo','odd','ode'),
          ('qua','urn','any'),
          ('bag','axe','hem'),
          ('foe','owl','elk'),
          ('jig','ivy','gym'),
]
pretty_triples(nicest)
nicest = [('sip','ice','tea'),
          ('zoo','odd','ode'),
          ('bus','ark','any'),
          ('owl','aha','fox'),
          ('jig','ivy','gym'),
          ('qua','urn','ant'),
]

nicest = [('sip','ice','tea'),
          ('mom','one','pet'),
          ('and','coy','ewe'),
          ('dad','ape','mew'),
          #('baa','and','add'),
          #('wet','ego','dog'),
          #('bug','are','ant'),
          #('owl','aha','fox'),
]
pretty_triples(nicest)

letters_left = list('abcdefghijklmnopqrstuvwxyz')

for t in nicest:
    print('... contains',count_letters(letters_left, t),'new letters:')
    pretty_triples([t])
    for w in t:
        for l in w:
            if l in letters_left:
                #print('removing', l)
                letters_left.remove(l)
pretty_triples(nicest)
print('remaining:', len(letters_left), letters_left)
need_list = set([])
for l in letters_left:
    need_list.update(filter(lambda x: l in x, common_list))
print(need_list)

new_list = set([])
for l in letters_left:
    new_list.update(filter(lambda x: l in x, words))
#print(new_list)

# print('2 needed and 2 only common')
# pretty_triples(triples_n_letters(1, letters_left,
#                                  triples_with_at_least(2, common_list,triples)))

good_stuff = []
for t in one_word(1, 'the', triples): # triples:
    if count_letters(letters_left, t) >= 0: # and has_letter('q', t):
        good_stuff.append(t)
pretty_triples(good_stuff)

tops = []
mids = []
bots = []
for t in triples:
    if t[0] in ['dog','wag','mom','and','dad']:
        tops.append(t)
    if t[1] in ['dog','wag','mom','and','dad']:
        mids.append(t)
    if t[2] in ['dog','wag','mom','and','dad']:
        bots.append(t)

# print('top mom')
# pretty_triples(one_word(0, 'mom', triples))
# print('top and')
#pretty_triples(one_word(1, 'ate', triples))
print('top dad')
pretty_triples(one_word(1,'ape',one_word(0, 'dad', triples)))
# print('tops', len(tops))
# pretty_triples(tops)
# print('mids', len(mids))
# pretty_triples(mids)
# print('bots', len(bots))
# pretty_triples(bots)

print('found', count)
