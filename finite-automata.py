#!/usr/bin/env python

# Author: Zachary Bowditch (Edargorter)
# Year: 2023
# Description: Demonstration of a python implementation of an arbitrary (deterministic) finite automaton using a class objects 

import string
import random 
import time 

class State:

    def __init__(self, label: str, transitions: dict()):
        self.label = label
        self.transitions = transitions 

    def getLabel(self):
        return self.label 

    def transition(self, symbol: str) -> str:
        return self.transitions[symbol]

    def to_string(self):
        return "\n".join([f"({self.label}, {s}) -> {self.transitions[s]}" for s in self.transitions])

    def __str__(self):
        return "\n".join([f"({self.label}, {s}) -> {self.transitions[s]}" for s in self.transitions])

class FA:

    def __init__(self, states: dict(), alphabet: list, start: str, accepts: list):
        self.alphabet = alphabet
        self.states = states 
        self.start = start
        self.accepts = accepts

    def doesAccept(self, string) -> bool:
        curr = self.states[self.start]
        for c in string:
            curr = self.states[curr.transition(c)]
        return curr.getLabel() in self.accepts

    def __str__(self):
        return "States: {}\nAlphabet: {}\nStart: {}\nAccept(s): {}\nTransitions:\n{}".format(", ".join([self.states[s].getLabel() for s in self.states]), ', '.join([c for c in self.alphabet]), self.start, ", ".join([a for a in self.accepts]), "\n".join([self.states[s].to_string() for s in self.states]))

def getRandomString(alphabet: list, length: int):
    return ''.join([random.choice(alphabet) for i in range(length)])

def getRandomFA(alphabet_limit: int, state_limit: int, accepts_limit: int) -> FA:
    assert accepts_limit <= state_limit
    universal_alphabet = string.digits + string.ascii_lowercase 
    alphabet_limit = min(alphabet_limit, len(universal_alphabet))
    alphabet_limit = random.randint(1, alphabet_limit)
    state_number = random.randint(1, state_limit)
    accepts_limit = min(accepts_limit, state_number)
    # symbols = random.sample(alphabet, alphabet_limit)
    alphabet = universal_alphabet[:alphabet_limit]
    state_labels = ['q_' + str(i) for i in range(state_number)]
    states = {}
    for sl in state_labels:
        transitions = {}
        for c in alphabet:
            transitions[c] = state_labels[random.randint(0, state_number - 1)]
        state = State(sl, transitions)
        states[sl] = state 
    accepts = random.sample(state_labels, accepts_limit)
    return alphabet, FA(states, alphabet, state_labels[0], accepts)

if __name__ == "__main__":
    # FA accepting only strings that end in 1 
    q1 = State("q1", {"0": "q1", "1": "q2"})
    q2 = State("q2", {"0": "q1", "1": "q2"})
    states = {q1.getLabel(): q1, q2.getLabel(): q2}
    start = q1.getLabel()
    accepts = [q2.getLabel()]
    fsm = FA(states, "01", start, accepts)
    print(fsm)
    no_1 = "10110101010101010100000000000"
    yes_1 = "100000000000000000000000001"
    yes_2 = "111111111111111111111111111"
    print(no_1, " : ", fsm.doesAccept(no_1))
    print(yes_1, " : ", fsm.doesAccept(yes_1))
    print(yes_2, " : ", fsm.doesAccept(yes_2))

    # Some empirical experimentation 

    total = 100000
    len_limit = 100
    accept = 0

    for i in range(total):
        alphabet, fsm = getRandomFA(alphabet_limit = 3, state_limit = 8, accepts_limit = 3) # 82% accept
        # alphabet, fsm = getRandomFA(alphabet_limit = 10, state_limit = 10, accepts_limit = 2) # 48% accept 
        # alphabet, fsm = getRandomFA(alphabet_limit = 10, state_limit = 10, accepts_limit = 1) # 29% accept 
        rstring = getRandomString(alphabet, random.randint(1, len_limit))
        yes = fsm.doesAccept(rstring)
        accept += yes 
        '''
        print(fsm)
        print(rstring)
        print(yes)
        '''

    print(f"Accept rate: {100 * accept / total} %")
