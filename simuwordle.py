#!/usr/bin/env python3

import sys, string


# Word and Guess are the parameters:
word    = None if len(sys.argv) <=  1 else sys.argv[1]
guess   = None if len(sys.argv) <=  2 else sys.argv[2]

def wordleResult(w: str, g: str) -> str:
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
    return exact + '?' + ''.join(set(guess).intersection(set(word)) - {'*'}) + '!' + ''.join(set(guess) - set(word) - {'*'})


print(f'{wordleResult(word, guess)}')
