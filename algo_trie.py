#!/usr/bin/env python3

import random,sys, string
from algo_trie_words import all_words

class TrieNode:
    def __init__(self, prefix, value=-1, parent=None, isLeaf=False):
        self.prefix     = prefix
        self.value      = value
        self.parent     = parent
        self.isLeaf     = isLeaf
        self.children   = []
        self.topn       = []

    def __str__(self):
        return f'Trie prefix: {self.prefix} value: {self.value}, parent:<{self.parent}>, leaf: {self.isLeaf}, children: {len(self.children)}'

    def printTrie(self,indent='->',level=0):
        print(f'{level:02d} {indent} {self.prefix}@{self.value} {self.isLeaf} top5: {self.topn}' + (f'child: {len(self.children)}' if len(self.children) > 0 else ''))
        for child in sorted(self.children, key=lambda item: item.prefix):
            child.printTrie('-' + indent,level+1)

    def flatten(self):
        if self.isLeaf:
            return f'<{self.prefix}>:0:{self.value}::{self.isLeaf};;'
        childs = ''
        for child in self.children:
            childs += child.flatten()
        return f'<{self.prefix}>:{len(self.children)}:{self.value}::{self.isLeaf};;{childs}'

    def flatTopn(self):
        if self.isLeaf and not self.children:
            return ''
        childs = ''
        for child in self.children:
            childs += child.flatTopn()
        return f'<<{self.prefix}>>:{self.topn}\n{childs}'


    def collapse(self):
        # remove all single child children that are not leafs
        nc = len(self.children)
        for idx,child in enumerate(list(self.children)):
            if not child.isLeaf and len(child.children) == 1:
                # we need to collapse this one
                realchild = child.children[0]
                while not realchild.isLeaf and len(realchild.children) == 1:
                    realchild = realchild.children[0]
                # realchild now points to the one we need to bring up
                self.children[idx] = realchild
                pass
            self.children[idx].collapse()

    def find(self,what):
        answer = []
        n = len(what)
        i = 1
        branch = self 
        while i <= n:
            for child in branch.children:
                if child.prefix == what[0:i]:
                    print(f'{child.prefix}', end=' -> ')
                    answer = child.topn
                    branch = child
                    break
            i += 1
        print()
        return answer 

    def topValue(self,k=5):
        # get all leaf nodes and sort them by value
        collect = []
        if self.isLeaf:
            collect.append( (self.prefix, self.value))
        for child in self.children:
            collect += child.topValue(k)
        self.topn = list(sorted(collect, key=lambda item: item[1], reverse= True))[0:min(k,len(collect))]
        return self.topn


    def hang(self,prefix,value,debug=False):
        n = len(prefix)
        if n == 0:
            return
        i = 1
        # example "cat" hang "c", hang "ca" and "cat"
        curr = self
        while i < n:
            # does prefix[0:i] exist?
            found = False
            for child in curr.children:
                if child.prefix == prefix[0:i]:
                    found = True
                    curr  = child
                    break
            # if not found, add it!
            if not found:
                newchild = TrieNode(prefix[0:i],-1,parent=curr,isLeaf=False)
                curr.children.append(newchild)
                curr = newchild
            i += 1
        # if we are here, we are ready to add the leaf node
        newleaf = TrieNode(prefix,value,parent=curr,isLeaf=True)
        curr.children.append(newleaf)
        print('hang',prefix,value, f'Parent: {newleaf.parent}') if debug else None


print('Computing TRIE')
# all_words = ['zoo','zoos','able','ability']
all_words = [x for i,x in enumerate(all_words) if i < 100 ]
all_words_freq = [random.randint(0,1000) for _ in all_words]

trie_prefix = {}

trie = TrieNode('')

for idx,w in enumerate(all_words):
    if all_words_freq[idx] < 300:
        continue
    trie.hang(w,all_words_freq[idx])
trie.collapse()
trie.topValue()
# trie.printTrie()
print(trie.flatten())
print(trie.flatTopn())

new_name = ''
print(f'Todays most popular: {trie.topn}')

sys.exit()
while new_name != 'quit':
    # Ask the user for a name.
    new_name = input("Please start typing, or enter 'quit': ")
    if new_name == 'quit' or new_name == 'q':
        break
    answer   = trie.find(new_name)
    print(answer)
