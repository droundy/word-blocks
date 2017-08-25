#!/usr/bin/python2

import sys, random, genalg
from collections import defaultdict

with open('words.four') as f:
    words = list(filter(lambda x: len(x) == 4, map(lambda x: x.strip(), f.readlines())))
with open('basic.four') as f:
    basic = sorted(list(filter(lambda x: len(x) == 4, map(lambda x: x.strip(), f.readlines()))))

animals = list(set(['lion','bear','goat','seal','dogs','cats','hawk','worm','crow',
                    'puma','slug','star','fish','herd','mink','duck','bird','pigs',
                    'emus','ibex','gnat','duck','lion','bear','yeti','crab','hare',
                    'wolf','mole','toad','boar','buck','bull','calf','colt','coon',
                    'deer','fawn','foal','joey','lamb','lynx','mule','newt','orca',
                    'oxen',
]))

words = list(set(words+animals))
# words = basic

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

def has_letter(l, triple):
    return l in t[0]+t[1]+t[2]+t[3]

def count_letters(letters, triple):
    return len(list(filter(lambda x: has_letter(x,triple), letters)))

def has_word(triple, w):
    return w in tuple_words(triple)
def has_horizontal_word(triple, w):
    return w in triple

def tuples_with(w, tuples):
    return list(filter(lambda t: has_word(t,w), tuples))

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

nicest = [
    ('lamb','afar','mama','pray'),
    ('hold','oboe','love','deep'),
    ('camp','aria','miri','pain'),
    #('wish','idle','near','game'),
    #('show','papa','even','went'),
    #('quip','undo','idle','poem'), # or poet
    #('warm','aqua','sunk','page'),
    ('wild','idea','lead','dads'),
    ('kiss','into','stun','song'),
    #('chef','real','also','blew'),
    ('swap','tale','ages','best'),
    #('thee','real','arts','pose'),
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
    need_list.update(filter(lambda x: l in x, basic))
print(need_list)

new_list = set([])
for l in letters_left:
    new_list.update(filter(lambda x: l in x, words))
#print(new_list)

# good_stuff = []
# for t in sorted(tuples_with_word(3, 'best')): #one_word(1,'gave', tuples): # tuples_with_at_least(4, basic, tuples_with_at_least(2, best, tuples)): # one_word(2, 'fox', tuples): # tuples:
#     if count_letters(letters_left, t) >= 0: # and has_letter('q', t):
#         good_stuff.append(t)
# pretty_tuples(good_stuff)

# print 'hello world'
# pretty_tuples(tuples_with_at_least(2, best, tuples))

#pretty_tuples(one_word(1,'love',tuples))
# print('bot dad')
# pretty_tuples(one_word(1,'apes',one_word(0, 'dada', tuples)))

best = ['love','miri','mama','hugs','kiss','with','hold','doll','girl','boys',
        'quip','quiz','whiz','zero','zoom','taxi',]

already_found = nicest

unused_best = list(filter(lambda w: not any(map(lambda t: has_word(t, w), already_found)),
                          best+animals))
unused_basic = list(filter(lambda w: not any(map(lambda t: has_word(t, w), already_found)),
                           basic))
unused_words = list(filter(lambda w: not any(map(lambda t: has_word(t, w), already_found)),
                           words))

def score_alpha(tuples):
    s = 0.0
    missing = ''
    contains = ''
    for l in 'abcdefghijklmnopqrstuvwxyz':
        if l in [c for t in tuples for w in t for c in w]: # any(map(lambda t: has_letter(l, t), tuples)):
            s += 1.0
            contains += l
        else:
            missing += l
    return s, missing
def score_basic(tuples):
    s = 0.0
    for b in unused_basic:
        if any(map(lambda t: has_word(t, b), tuples)):
            s += 1
        if any(map(lambda t: has_horizontal_word(t, b), tuples)):
            s += 0.5
    return s
def score_best(tuples):
    s = 0.0
    for b in unused_best:
        if any(map(lambda t: has_word(t, b), tuples)):
            s += 0.5
        if any(map(lambda t: has_horizontal_word(t, b), tuples)):
            s += 1.0
    return s

def score(tuples):
    s = 0.0
    s += score_best(tuples)
    s += score_basic(tuples)
    for b in unused_words:
        if any(map(lambda t: has_word(t, b), tuples)):
            s += 0.01
    s += 10*score_alpha(tuples)[0]
    return s
def simple_score(t):
    s = 0.0
    for b in unused_best:
        if has_horizontal_word(t, b):
            s += 1.0
    for b in unused_basic:
        if has_word(t, b):
            s += 1
    for b in unused_basic:
        if has_horizontal_word(t, b):
            s += 0.5
    return s

print "previously had", len(tuples), 'tuples to work with'
#tuples = list(filter(lambda t: simple_score(t) > 5, tuples))
#print "reduced to", len(tuples), 'tuples to work with'

def extend_tuple(start, bestscore):
    if len(start) == 6:
        return score(start), start
    average_best = bestscore/6
    best_tuple = start
    if len(start) > 0 and score(start)/len(start) <= average_best:
        return None
    for t in tuples:
        nextscore = score(start + [t])
        if nextscore/(len(start)+1) > bestscore/6:
            xxx = extend_tuple(start + [t], bestscore)
            if xxx is not None and xxx[0] > bestscore:
                print 'score', xxx[0], '>', bestscore
                bestscore = xxx[0]
                best_tuple = xxx[1]
                pretty_tuples(best_tuple)
    return bestscore, best_tuple

bestscore = 0.0
for i in range(1000): #range(len(tuples)):
    attempt = random.sample(tuples, 6)
    s = score(attempt)
    if s > bestscore:
        print 'random', i, ':', s, '>', bestscore
        bestscore = s
        best_tuple = attempt
        pretty_tuples(best_tuple)

p = genalg.Population(
    popsize = 10000,
    nchrom = 6,
    chromset = tuples,
)
def print_report(name, ind):
    alphscore, missing = score_alpha(ind.chromosomes)
    for i in range(4):
        if i == 0:
            sys.stdout.write('   {0:5} {1:<6}'.format(name, ind.fitness))
        elif i == 1:
            sys.stdout.write('   {0:>5} {1:<6}'.format('a-z', alphscore))
        elif i == 2:
            if len(missing) <= 11:
                sys.stdout.write('   {0:>11} '.format(missing))
            else:
                sys.stdout.write('   {0:>8}... '.format(missing[:8]))
        elif i == 3:
            sys.stdout.write('   {0:>5} {1:<6}'.format('bas', score_basic(ind.chromosomes)))
        else:
            sys.stdout.write('   {0:5} {1:<6}'.format('',''))
        for t in ind.chromosomes:
            sys.stdout.write(t[i])
            sys.stdout.write(' ')
        print
    print

best = p.run(
    eval_fn = score,
    generations = 1000,            # maximum generations to run for
    verbose = True,
    minimize = False,
    mutations = ['mutate', 'shuffle-mate', 'sort'],
    print_report = print_report,
)

p.members.reverse()

for i in p.members:
    print_report(i)

pretty_tuples(best.chromosomes)
# print "Now being systematic..."

# print extend_tuple([], bestscore)
