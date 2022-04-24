#!/usr/bin/env python3

import sys, string, multiprocessing
from multiprocessing import Pool

from numpy import full

# from https://github.com/dwyl/english-words
# cat words.all.txt|grep -xE '.{5}' |sort -u >words.all.len5.txt
# WORDS   = 'words.all.len5.txt'
WORDS   = 'wordle.wordlist.txt'
vowels  = {'a','e','i','o','u'}
allchr  = set(string.ascii_lowercase)

def wordleResult(w: str, g: str) -> tuple[str, dict]:
    exact = ''
    word    = list(w)
    guess   = list(g)
    for i in range(len(word)):
        if guess[i] == word[i]:
            exact += guess[i]
            word[i]     = '*'       # null this
            guess[i]    = '*'
        else:
            exact += '_'
    # which letters are ok but in the wrong position?
    wrongPositions = {}
    for letterOk in (set(guess).intersection(set(word)) - {'*'} - set(exact)):
        position = g.find(letterOk) + 1        
        wrongPositions[letterOk] = [position]
    # print(f'      * letter belongs but not in position {wrongPositions}')
    return exact + '?' + ''.join(set(guess).intersection(set(word)) - {'*'}) + '!' + ''.join(set(guess) - set(word) - {'*'} - set(exact)), wrongPositions

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

def getExact(guess: str) -> tuple[str, str, str]:
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


def extra(word: str, guess: str) -> str:
    if not guess:
        return word
    # parse the guess values into exact, doesHave and notHave
    exact, doesHave, notHave = getExact(guess)
    return set(set(word) - set(exact) - set(doesHave))

def bestNext(words, guessfilter):
    # now look for the words with highest score
    letterDistro    = {letter: 0 for letter in allchr}
    for word in words:
        for letter in word:
            letterDistro[letter] += 1
    wordScore       = {w: 0 for w in words}
    maxScore        = 0

    for word in words:
        missing = extra(word, guessfilter)
        for letter in set(missing):
            wordScore[word] += letterDistro[letter]
        if wordScore[word] > maxScore:
            maxScore = wordScore[word]
    goodguesses     = []
    bestguess       = ''
    highestguess    = 0
    for word in sorted(words):
        if wordScore[word] == maxScore:
            score = {k: letterDistro[k] for k in word}
            only  = '!ONLY!' if len(words) == 1 else f'[1 of {len(words)}]'
            # print(f'{word} {only} has {maxScore} {score} Letter Probabilities: First {origdistro[word[0]][0]:.3f}%  Last {origdistro[word[-1]][1]:.3f}%')
            if (origdistro[word[0]][0] + origdistro[word[-1]][1]) > highestguess:
                bestguess       = word
                highestguess    = origdistro[word[0]][0] + origdistro[word[-1]][1]
            goodguesses.append(word)
    return bestguess

def mergeNotInPosition(old: dict, added: dict):
    for letter,wrongposition in added.items():
        if letter not in old:
            old[letter] = wrongposition
        else:
            if wrongposition[0] not in old[letter]:
                old[letter].append(wrongposition[0]) 
    return

def noBadPositions(word: str, wrong: dict) -> bool:
    for letter,badpositions in wrong.items():
        if letter in word and (word.find(letter) + 1) in badpositions:
            return False
    return True

def fullGame(startGuess):
    MAXITERATS = 12
    maxdepth = 0
    maxword  = ''
    totdepth = 0
    histogram = [0] * MAXITERATS
    for wordleword in originalwords[0:]:
        guesses = [startGuess]
        iterats = 1
        guess   = startGuess
        words   = originalwords
        # print(f'      iteration 0 reduced universe to {len(words)} words. First guess: {guess}')
        letterNotInPosition = {}
        while  guess != wordleword and guess != '' and iterats < MAXITERATS:
            # simplify the word space to matching from guess
            guessfilter,wrongPositions = wordleResult(wordleword, guess)
            mergeNotInPosition(letterNotInPosition,wrongPositions)
            # print(f'      * letter belongs but not in positions {letterNotInPosition}')
            # print(f'----- [{wordleword}] Guess: {guess} resulted in: {guessfilter}')
            words = [word for word in words if filter(word, guessfilter) and noBadPositions(word,letterNotInPosition)]
            guess = bestNext(words, guessfilter)
            guesses.append(guess)
            # print(f'      iteration {iterats} reduced universe to {len(words)} words. Next guess: {guess}')
            iterats += 1
            if guess != wordleword:
                words = set(words) - {guess}
        if iterats > maxdepth :
            maxdepth = iterats
            maxword  = wordleword
        # print(f'{wordleword} Game ended in {iterats} iterations: {guesses}')
        histogram[iterats] += 1
        totdepth += iterats
    clean_histo = [value for value in histogram if value != 0]
    cu_list = [sum(clean_histo[0:x:1]) for x in range(1, len(clean_histo)+1)]
    print(f'{startGuess}... {totdepth}. ', end = '', flush=True)
    return startGuess, maxdepth, maxword, totdepth, clean_histo, cu_list


# Word to be guessed:
with open(WORDS) as f:
    originalwords = [line.rstrip() for line in f]
# compute first and last letter probability
origdistro = {k: [0,0] for k in allchr}
for word in originalwords:
    origdistro[word[0]][0] += 1
    origdistro[word[-1]][1] += 1
for letter in list(sorted(origdistro.keys())):
    if origdistro[letter] == [0,0]:
        continue
    origdistro[letter] = [100*origdistro[letter][0]/len(originalwords),100*origdistro[letter][1]/len(originalwords)]
    # print(f'{letter} [{origdistro[letter][0]:.3f}%, {origdistro[letter][1]:.3f}%]')

# analyze every possible combination
mindepth    = len(originalwords) * 5
results     = {}

if __name__ == '__main__':
    with Pool(multiprocessing.cpu_count()-1) as p:
        paralleresults = p.map(fullGame, originalwords[0:])

    results = {result[0]: result[1:] for result in paralleresults}
    print('\nDone')
    
    optimal     = []
    avgopt      = []
    for word in sorted(results.keys()):
        maxdepth, maxword, avgdepth, clean_histo, cu_list = results[word]
        # if avgdepth < (len(originalwords) * 4):
        # print(f'iterating {word} {maxdepth:2d} toughest word: {maxword} - totdept: {avgdepth} {avgdepth/len(originalwords):.3f} - cumulative histogram {cu_list}')
        if avgdepth == mindepth:
            optimal.append(word)
            avgopt.append(avgdepth)
        if avgdepth < mindepth:
            mindepth = avgdepth
            optimal  = [word]
            avgopt   = [avgdepth]

    print(f'best words {optimal} for maxdepth {maxdepth} tot depth {avgopt}\n')

    sortedResults = {k: v for k, v in sorted(results.items(), key=lambda item: item[1][2])}
    count   = 0
    MAXBEST = 20
    for k,v in sortedResults.items():
        print(f'{k}: {v}')
        count += 1
        if count >= MAXBEST:
            break

