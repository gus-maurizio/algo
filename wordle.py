#!/usr/bin/env python3

import random,sys, string

# from https://github.com/dwyl/english-words
# cat words.all.txt|grep -xE '.{5}' |sort -u >words.all.len5.txt
# WORDS   = 'words.all.len5.txt'
WORDS   = 'wordle.wordlist.txt'
vowels  = {'a','e','i','o','u'}
allchr  = set(string.printable)
matches = None if len(sys.argv) == 1 else sys.argv[1]
avoids  = None if len(sys.argv) <= 2 else sys.argv[2]
exact   = None
# support notation _e_r_ for exact position!
if matches and '_' in matches:
    exact   = matches + '_____'
    matches = None


with open(WORDS) as f:
    words = [line.rstrip() for line in f]

frequency           = {chr: 0 for chr in allchr}
firstlettfrequency  = {chr: 0 for chr in allchr}
sumchrs             = 0
sumfirsletterchrs   = 0

for word in words:
    nvowels = 0
    wvowels = []
    for letter in word:
        if letter in vowels:
            nvowels += 1
            wvowels.append(letter)
    distinct = len(set(wvowels))
    if nvowels >= 2 and not matches and not exact:
        print(f'{word} has {nvowels} vowels {distinct}: {sorted(wvowels)}')
    # if matches and not any([l in word for l in matches]):
    #     print(f'--- {word} negative matches {matches}')
    if matches and not avoids and all([l in word for l in matches if l != '_']):
        unmatched = set(word) - set(matches)
        print(f'+++ {word} positive matches {matches} remain: {unmatched}')
    if matches and all([l in word for l in matches]) and avoids and not any(l in word for l in avoids):
        unmatched = set(word) - set(matches)
        print(f'+++ {word} positive matches {matches} that avoid {avoids} remain: {unmatched}')
        # save the unmatched frequency
        firstlettfrequency[word[0]] += 1
        sumfirsletterchrs           += 1
        for chr in unmatched:
            frequency[chr]          += 1
        sumchrs                     += len(unmatched)

    # support exact matching
    if exact and not avoids and all([word[i] == exact[i] if exact[i] != '_' else True for i in range(len(word))]):
        unmatched = set(word) - set(exact)
        print(f'+++ {word} positive exact {exact[0:5]} remain: {unmatched if unmatched else None}')

    if exact and all([word[i] == exact[i] if exact[i] != '_' else True for i in range(len(word))])  and avoids and not any(l in word for l in avoids):
        unmatched = set(word) - set(exact)
        print(f'+++ {word} positive exact {exact[0:5]} remain: {unmatched if unmatched else None}')
        # save the unmatched frequency
        firstlettfrequency[word[0]] += 1
        sumfirsletterchrs           += 1
        for chr in unmatched:
            frequency[chr]          += 1
        sumchrs                     += len(unmatched)


# most probable letters
# for first character
for chr,freq in sorted(firstlettfrequency.items()):
    if freq == 0:
        continue
    print(f'- First letter {chr}: {(freq/sumfirsletterchrs)*100:.2f}% probability')

for chr,freq in sorted(frequency.items()):
    if freq == 0:
        continue
    print(f'- Letter {chr}: {(freq/sumchrs)*100:.2f}% probability')

