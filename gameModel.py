#!/usr/bin/env python3

import random, math, csv, json, argparse, uuid, os, gzip

from statistics import mean,median
from math import sqrt
from termcolor import colored
from itertools import permutations, combinations

class CustomJsonEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Decimal):
            return float(obj)
        if isinstance(obj, (datetime, date)):
            return obj.isoformat()
        return super(CustomJsonEncoder, self).default(obj)

class Game:
    DEFAULTCASES   = [0.01, 1, 5, 10, 25, 50, 75, 100, 200, 300, 400, 500, 750, 1000, 5000, 10000, 25000, 50000, 75000, 100000, 200000, 300000, 400000, 500000, 750000, 1000000]
    DEFAULTROUNDS  = [6, 5, 4, 3, 2, 1, 1, 1, 1]

    def __init__(   self,
                    gameID=uuid.uuid4(),
                    caseValues=[0.01, 1, 5, 10, 25, 50, 75, 100, 200, 300, 400, 500, 750, 1000, 5000, 10000, 25000, 50000, 75000, 100000, 200000, 300000, 400000, 500000, 750000, 1000000], 
                    gameRounds=[6, 5, 4, 3, 2, 1, 1, 1, 1],
                    bankerOffer='((26 - C)/26) * E',
                    panelShow=2):
        self.gameID      = gameID
        self.caseValues  = sorted(caseValues.copy())
        self.caseNumbers = list(range(1, len(caseValues) + 1))
        self.gameRounds  = gameRounds.copy()
        self.bankerOffer = bankerOffer
        self.panelShow   = panelShow
        self.round       = 0
        self.valuesGone  = []
        self.offersMade  = []
        self.recommend   = []

        self.playerCase  = random.randint(0, len(self.caseValues)-1)
        self.caseContent = self.caseValues[:]
        random.shuffle(self.caseContent)
        self.valuesPlay  = self.caseValues[:]
        self.valuesPlay.remove(self.caseContent[self.playerCase])


    def setRound(self,cases=[]):
        # we always end with two cases, the player's and one more.
        aux = self.DEFAULTROUNDS + [0]
        casesPerRound = [(len(self.DEFAULTCASES) - sum(aux[:x])) for x in range(len(aux))]
        round = casesPerRound.index(len(cases))
        print(casesPerRound,cases,round)
        self.round = round
        self.gameRounds = self.gameRounds[round:]
        for i in range(len(self.caseValues)):
            if self.caseValues[i] not in cases:
                self.caseValues[i] = -self.caseValues[i]
        print(self.gameRounds,self.caseValues)
        self.valuesPlay = cases[:]
        random.shuffle(self.valuesPlay)
        newPlayer = cases[random.randint(0, len(cases)-1)]
        self.valuesPlay.remove(newPlayer)
        newPlayerCaseNumber = self.caseContent.index(newPlayer)
        self.playerCase = newPlayerCaseNumber

    def playRound(self):
        if len(self.gameRounds) == 0:
            print('Game ended. Player won {} or {} if he switched cases'.format(colored(self.caseContent[self.playerCase],'red'), colored(self.valuesPlay[0],'blue')))
            return False
        num = self.gameRounds.pop(0)
        print(self.gameRounds)
        self.round += 1
        cases = self.selectCase(num)
        print('cases selected {}'.format(cases))
        self.openCase(cases)
        return True

    def selectCase(self,qty):
        random.shuffle(self.valuesPlay)
        return self.valuesPlay[:qty]


    def casesToRemove(self):
        return self.gameRounds[0] if len(self.gameRounds) > 0 else 0

    def chosenCase(self):
        return self.caseContent[self.playerCase]

    def chosenCaseNumber(self):
        return self.playerCase


    def makeOffer(self):
        inplay = [value for value in self.caseValues if value > 0]
        C   = len(inplay)
        T   = sum(inplay)
        E   = round(sum(inplay) / (C * 1000)) * 1000
        S   = sum([x**2 for x in inplay])
        MAX = max(inplay)
        MIN = min(inplay)
        O   = (E * C - MAX) / (C-1)
        offer = round(eval(self.bankerOffer)/1000) * 1000
        self.offersMade.append(offer)
        print('Banker offer ${} [average {}  max {}  playercase {}  offersmade {}]'.format(colored(offer,'cyan',attrs=['bold']),E,MAX,self.caseContent[self.playerCase],self.offersMade))
        return offer,E,MAX

    def adviseOffer(self,offer):
        inplay = [value for value in self.caseValues if value > 0]
        C   = len(inplay)
        E   = round(sum(inplay) / (C * 1000)) * 1000
        MED = round(median(inplay))
        MAX = max(inplay)
        MIN = min(inplay)
        QLO = sum([1 for value in inplay if value < offer])
        QHI = sum([1 for value in inplay if value > offer])

        inplay.remove(MAX)
        rC   = len(inplay)
        rE   = round(sum(inplay) / (rC * 1000)) * 1000
        rMED = round(median(inplay))
        rMAX = max(inplay)
        rMIN = min(inplay)
        rQLO = sum([1 for value in inplay if value < offer])
        rQHI = sum([1 for value in inplay if value > offer])

        # inplay.remove(rMAX)
        # inplay.append(MAX)
        # rrC   = len(inplay)
        # rrE   = round(sum(inplay) / (rrC * 1000)) * 1000
        # rrMED = round(median(inplay))
        # rrMAX = max(inplay)
        # rrMIN = min(inplay)
        # rrQLO = sum([1 for value in inplay if value < offer])
        # rrQHI = sum([1 for value in inplay if value > offer])

        # inplay.remove(rrMIN)
        # inplay.append(rMAX)
        # bC   = len(inplay)
        # bE   = round(sum(inplay) / (bC * 1000)) * 1000
        # bMED = round(median(inplay))
        # bMAX = max(inplay)
        # bMIN = min(inplay)
        # bQLO = sum([1 for value in inplay if value < offer])
        # bQHI = sum([1 for value in inplay if value > offer])


        # factor = offer/E if E > 10000 else 0

        print('       {} cases left, [med/avg/max {} {} {}] with {} below and {} above offer'.format(C,MED,E,MAX,QLO,QHI))
        print('\t      Without the 1st MAX {} left [med/avg/max {} {} {}] with {} below and {} above offer'.format(rC,rMED,rE,rMAX,rQLO,rQHI))
        # print('\t      Without the 2nd MAX {} left [med/avg/max {} {} {}] with {} below and {} above offer'.format(rrC,rrMED,rrE,rrMAX,rrQLO,rrQHI))
        # print('\t      Best case scenario  {} left [med/avg/max {} {} {}] with {} below and {} above offer'.format(bC,bMED,bE,bMAX,bQLO,bQHI))
        # print('\t++++> Recommendation: Prob(choosing the 1st MAX) {}% Prob(choosing any of 2 MAX) {}% '.format(100/C, 2* 100/C))
        # print('\t++++> Best next offer {} worst if top value hit {} or if 2nd top {}'.format(round(factor*bE), round(factor*rE), round(factor*rrE)))

        return 

    def nextOffer(self,original=0, num=1):
        inplay = [value for value in self.caseValues if value > 0]
        C   = len(inplay)
        E   = round(sum(inplay) / (C * 1000)) * 1000
        # I need to analyze what happens with E when I remove num elements
        # they are all equally likely...
        combs = list(combinations(inplay,len(inplay)-int(num)))
        nextE = 0
        tcombs = len(combs)
        # print(C,E,nextE)
        below = 0
        above = 0
        for comb in combs:
            inplay = list(comb)
            C      = len(inplay)
            E      = round(sum(inplay) / (C * 1000)) * 1000
            nextE  = nextE + E
            if E > original:
                above += 1
            else:
                below +=1
        nextOffer = round(nextE/tcombs)
        numAbove  = sum([1 for value in self.caseValues if value > original])
        recommend = ''
        print('\nADVISE likely offer ${} ({} variants analyzed). Probability above {:3.2f}%  below {:3.2f}%'.format(colored(nextOffer,'cyan',attrs=['bold']),tcombs,100*above/tcombs,100*below/tcombs))
        print('ADVISE we have {} cases above the offer and will remove {} cases, '.format(numAbove, num))
        print('ADVISE history {}'.format(self.recommend))
        if nextOffer > 1.25*original and 100*below/tcombs < 20 and numAbove >= (num - 1):
            print(colored('-----> Keep Playing','blue',attrs=['bold','blink']))
            recommend = 'keep'
        else:
            print(colored('-----> Take Offer','red',attrs=['bold','blink','reverse']))
            recommend = 'take'
        self.recommend.append((recommend, nextOffer))
        return nextOffer


    def openCase(self,valueList):
        # remove the first appearance of values from valueList
        for value in valueList:
            self.valuesPlay.remove(value)
            for i in range(len(self.caseValues)):
                if self.caseValues[i] == value:
                    self.caseValues[i] = - self.caseValues[i]
                    break

    def showGame(self):
        print('\033c', end='')
        print('Game ID {}\n\tValues: {}\n\tRounds: {}\n'.format(self.gameID,self.caseValues,self.gameRounds))
        print('Player\'s case is {}'.format(self.playerCase))
        print('Player\'s cases are {}'.format(self.caseNumbers))
        return

    def showBoard(self):
        inplay = 'red'
        ofplay = 'magenta'
        chunkSize   = int(len(self.caseValues)/self.panelShow)
        board       = [self.caseValues[i*chunkSize:(i+1)*chunkSize] for i in range(0, self.panelShow)]
        
        print('\033c', end='')
        print('Board for game ID {} \n\tround {} - Player to remove {} cases. Remaining {} {}\n'.format(self.gameID,colored(self.round,'cyan',attrs=['bold']),self.gameRounds[0] if len(self.gameRounds) > 0 else 0,self.gameRounds, sum(self.gameRounds) + 2))
        # print('\tCase: {} [{}] contents: {}\n'.format(self.playerCase,self.caseContent[self.playerCase],self.caseContent))
        for row in range(0,len(board[0])):
            for col in range(0,len(board)):
                print('{}   '.format(colored('{:>10}'.format(board[col][row]),inplay if board[col][row] > 0 else ofplay,attrs=['bold' if board[col][row] > 0 else 'dark'])), end = '')
            print('\n',end='')
        print()

def getArgs():
    parser = argparse.ArgumentParser(description='Generate test data.')
    parser.add_argument('-t', '--trials',       type=int, default=10, help='#trials')

    parser.add_argument('-c', '--cases',        type=str,   default='[0.01, 1, 5, 10, 25, 50, 75, 100, 200, 300, 400, 500, 750, 1000, 5000, 10000, 25000, 50000, 75000, 100000, 200000, 300000, 400000, 500000, 750000, 1000000]',    help='case money')
    # parser.add_argument('-c', '--cases',        type=str,   default='[0.01, 1, 5, 10, 25, 50, 75, 100, 200, 300, 400, 500, 750, 1000000, 1000000, 1000000, 1000000, 1000000, 1000000, 1000000, 1000000, 1000000, 1000000, 1000000, 1000000, 1000000]',    help='case money')
    # parser.add_argument('-s', '--state',        type=str,   default='[5,10,200,300,300000]',    help='state game case money')
    parser.add_argument('-s', '--state',        type=str,   default='[]',    help='state game case money')

    
    parser.add_argument('-r', '--remove',       type=str,   default='[6, 5, 4, 3, 2, 1, 1, 1, 1]',  help='removal per round')
    # E is the expected value of the contestant's case (i.e. the arithmetic mean of all remaining values), S is the sum of square values of remaining, 
    # C is the number of cases remaining, and M is the maximum value on the board.
    # $12,275.30 + (0.748 * E) - (2714.74 * C) - (0.40 * M) + (.0000006986 * E^2) + (32.623 * C^2)
    # parser.add_argument('-f', '--formula',      type=str,   default='12275.30 + 0.748 * E - 2714.74 * C - 0.40 * M + .0000006986 * E**2 + 32.623 * C**2',  help='banker offer formula. ')
    # parser.add_argument('-f', '--formula',      type=str,   default='sqrt(S/C)',  help='banker offer formula. ')
    parser.add_argument('-f', '--formula',      type=str,   default='0.85 * (26 - C) * E / 26',  help='banker offer formula. ')
    parser.add_argument('-p', '--player',       type=str,   default='offer > 0.7 * E and offer > O and T < 1750000',  help='player accept offer strategy. ')

    parser.add_argument('-l', '--log',          type=str, default='dealornodeal', help='filename (no extension)')
    parser.add_argument('-z',  '--gzip',        default=False, action='store_true',help='Activate gzip.')
    parser.add_argument('-v',  '--verbose',     default=False, action='store_true',help='Verbose details.')
    parser.add_argument('-vv',  '--vverbose',   default=False, action='store_true',help='verbose end.')
    args = parser.parse_args()
    return args

def main():
    # Get command-line arguments
    # random.seed(1234)
    args = getArgs()
    print(args)
    cases  = json.loads(args.cases)
    state  = json.loads(args.state)
    offers = json.loads(args.remove)
    numcases = len(cases)
    meanvalue = mean(cases)

    # print('Simulating {:,} trials. {} Cases: {}... Mean: ${:,.2f}'.format(args.trials,numcases, cases, meanvalue))
    game = Game(caseValues=cases, gameRounds=offers, bankerOffer=args.formula)
    game.showGame()
    game.showBoard()

    inp = input('\n\nPress anykey to start game or q/Q to quit: ')
    if inp != '' and inp in 'qQ':
        return

    if len(state) > 0:
        game.setRound(cases=state)
        game.showBoard()
        OFFER,AVG,MAX = game.makeOffer()
        game.adviseOffer(OFFER)
        probableE = game.nextOffer(original=OFFER, num=game.casesToRemove())
        inp = input('\n\nPress anykey to continue (q/Q exit | t/T take offer): ')
        if inp != '' and inp in 'qQ':
            print('Exiting game')
            return
        if inp != '' and inp in 'tT':
            print(colored('\nOffer taken for ${}. Player\'s case had ${}'.format(OFFER,game.chosenCase()),'magenta'))
            return

    while game.playRound():
        game.showBoard()
        OFFER,AVG,MAX = game.makeOffer()
        game.adviseOffer(OFFER)
        probableE = game.nextOffer(original=OFFER, num=game.casesToRemove())
        inp = input('\n\nPress anykey to continue (q/Q exit | t/T take offer): ')
        if inp != '' and inp in 'qQ':
            print('Exiting game')
            return
        if inp != '' and inp in 'tT':
            print(colored('\nOffer taken for ${}. Player\'s case had ${}'.format(OFFER,game.chosenCase()),'magenta'))
            return
    print(colored('\nPlayer kept case with ${}'.format(game.chosenCase()),'magenta'))




if __name__ == '__main__':
    main()
