#!/usr/bin/env python3

import random,sys, string

# from https://github.com/dwyl/english-words
# cat words.all.txt|grep -xE '.{5}' |sort -u >words.all.len5.txt
# WORDS   = 'words.all.len5.txt'
WORDS   = 'wordle.wordlist.txt'
vowels  = {'a','e','i','o','u'}
allchr  = set(string.ascii_lowercase)

# Guess is first and only parameter in the form:
# __x_y?abc!defgh, interpreted as x in 3rd position, y in 5th position, contains abc and does not contain defgh
guess   = None if len(sys.argv) == 1 else sys.argv[1]

def getExact(guess: str) -> tuple(str, str, str):
    exact = doesHave = notHave = None
    if      '?' in guess:
        exact, rest = guess.split('?')
        if '!' not in rest:
            rest += '!'
        doesHave, notHave = rest.split('!')
    elif    '!' in guess:
        exact, notHave = guess.split('!')
        doesHave    = ''
    else:
        exact       = guess
        doesHave    = ''
        notHave     = ''
    exact += '_____'
    return exact, doesHave, notHave

def filter(word: str, guess: str) -> bool:
    if not guess:
        return True
    # parse the guess values into exact, doesHave and notHave
    exact, doesHave, notHave = getExact(guess)
    # word matches if all exact characters in position, all doesHave belong, and none of notHave are there.
    conditionExact      = all([word[i] == exact[i] if exact[i] != '_' else True for i in range(len(word))])
    conditionDoesHave   = all([l in word for l in doesHave])
    contitionNotHave    = not any(l in word for l in notHave)
    if  conditionExact and conditionDoesHave and contitionNotHave:
        return True
    return False

def extra(word: str, guess: str) -> str:
    if not guess:
        return word
    # parse the guess values into exact, doesHave and notHave
    exact, doesHave, notHave = getExact(guess)
    return set(set(word) - set(exact) - set(doesHave))

with open(WORDS) as f:
    originalwords = [line.rstrip() for line in f]
# compute first and last letter probability
origdistro = {k: [0,0] for k in allchr}
for word in originalwords:
    origdistro[word[0]][0] += 1
    origdistro[word[-1]][1] += 1
for letter in list(origdistro.keys()):
    if origdistro[letter] == [0,0]:
        continue
    origdistro[letter] = [100*origdistro[letter][0]/len(originalwords),100*origdistro[letter][1]/len(originalwords)]

# for k,v in sorted(origdistro.items(), key=lambda item: item[0]):
#     print(f'first/last distro {k} {v[0]:.2f}% {v[-1]:.2f}%')
words = [word for word in originalwords if filter(word, guess)]

# print(f'{len(words)} words filtered')
# the best next guess will be the one that has the most frequent letter(s) of the filtered set.
letterDistro    = {letter: 0 for letter in allchr}
wordScore       = {w: 0 for w in words}
maxScore        = 0
for word in words:
    missing = extra(word, guess)
    # print(f'{word} has {missing}')
    for letter in missing:
        letterDistro[letter] += 1

# now look for the words with highest score
for word in words:
    missing = extra(word, guess)
    # print(f'{word} has {missing}')
    for letter in set(missing):
        wordScore[word] += letterDistro[letter]
    if wordScore[word] > maxScore:
        maxScore = wordScore[word]
# print('***** BEST GUESSES *****')
for word in words:
    if wordScore[word] == maxScore:
        score = {k: letterDistro[k] for k in word}
        only  = '!ONLY!' if len(words) == 1 else f'[1 of {len(words)}]'
        print(f'{guess} -> {word} {only} has {maxScore}')

# frequency of letters
sorted_tuples = sorted(letterDistro.items(), key=lambda item: item[1])
bestLetters = []
for k,v in sorted_tuples:
    if v > 0:
        # print(f'{k}: {v}')
        bestLetters.append((k,v))
# print(f'--- Best letters {bestLetters[::-1]}')

