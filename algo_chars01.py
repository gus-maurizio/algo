
doc_rotationalCipher='''
Rotational Cipher
One simple way to encrypt a string is to "rotate" every alphanumeric character by a certain amount. Rotating a character means replacing it with another character that is a certain number of steps away in normal alphabetic or numerical order.
For example, if the string "Zebra-493?" is rotated 3 places, the resulting string is "Cheud-726?". Every alphabetic character is replaced with the character 3 letters higher (wrapping around from Z to A), and every numeric character replaced with the character 3 digits higher (wrapping around from 9 to 0). Note that the non-alphanumeric characters remain unchanged.
Given a string and a rotation factor, return an encrypted string.
Signature
string rotationalCipher(string input, int rotationFactor)
Input
1 <= |input| <= 1,000,000
0 <= rotationFactor <= 1,000,000
Output
Return the result of rotating input a number of times equal to rotationFactor.
Example 1
input = Zebra-493?
rotationFactor = 3
output = Cheud-726?
Example 2
input = abcdefghijklmNOPQRSTUVWXYZ0123456789
rotationFactor = 39
output = nopqrstuvwxyzABCDEFGHIJKLM9012345678


'''

def rotationalCipher(input, rotation_factor):
    from collections import namedtuple
    import string

    # Write your code here
    alower = list(string.ascii_lowercase)
    aupper = list(string.ascii_uppercase)
    adigit = list(string.digits)
    # python treats strings as immutable so change in place is not possible, leverage a list of char
    answer = []
    for c in input:
        if c.islower():
            answer.append(chr(((ord(c)-ord(alower[0]))+rotation_factor)%len(alower)+ord(alower[0])))
        elif c.isupper():
            answer.append(chr(((ord(c)-ord(aupper[0]))+rotation_factor)%len(aupper)+ord(aupper[0])))
        elif c.isdigit():
            answer.append(chr(((ord(c)-ord(adigit[0]))+rotation_factor)%len(adigit)+ord(adigit[0])))
        else:
            answer.append(c)
    return ''.join(answer)

import random,datetime
P = 'Zebra-493?'
# P = 'abcdefghijklmNOPQRSTUVWXYZ0123456789'
myAlgo = [rotationalCipher]
for s in myAlgo:
    start = datetime.datetime.now()    #timeit.timeit()
    r = s(P,3)
    end = datetime.datetime.now()
    print(f'executing {s} for {len(P)} random alpha --- time: {(end-start).total_seconds()}, {r}')
