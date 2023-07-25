#!/usr/bin/env python

# Author: Zachary Bowditch (Edargorter)
# Year: 2023
# Reason: Fun and games 
# Lang: Python 3.10.6
# Description: Demonstration of a python implementation of an arbitrary (deterministic) finite-state machine using class objects 
#
#
#
#
#   q_0, q_1				# states
#   0, 1					# alphabet
#   q_0						# start
#   q_0, q_1				# accept
#   q_0, 0, q_1			    # Transitions lines = |states| x |alphabet| 
#   q_0, 1, q_1
#   q_1, 0, q_0
#   q_1, 1, q_1
#

import string
import random 
import time 
from sys import argv 

class State:

    def __init__(self, label: str, transitions: dict()):
        self.label = label
        self.transitions = transitions 

    def getLabel(self):
        return self.label 

    def transition(self, symbol: str) -> str:
        return self.transitions[symbol]

    def toString(self):
        return "\n".join([f"{self.label}, {k}, {v}" for k, v in self.transitions.items()])

    def __str__(self):
        return "\n".join([f"{self.label}, {k}, {v}" for k, v in self.transitions.items()])

    def prettyString(self):
        return "\n".join([f"q({self.label}, {k}) -> {v}" for k, v in self.transitions.items()])
        

class FSM:

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

    def getAlphabet(self):
        return self.alphabet

    def __str__(self):
        return "{}\n{}\n{}\n{}\n{}".format(", ".join([s for s in self.states]), ', '.join([c for c in self.alphabet]), self.start, ", ".join([a for a in self.accepts]), "\n".join([v.toString() for k, v in self.states.items()]))

    # For pretty printing  :)
    def prettyString(self):
        return "States: {}\nAlphabet: {}\nStart: {}\nAccept(s): {}\nTransitions:\n{}".format(", ".join([s for s in self.states]), ', '.join([c for c in self.alphabet]), self.start, ", ".join([a for a in self.accepts]), "\n".join([self.states[s].prettyString() for s in self.states]))
            
def getRandomString(alphabet: list, length: int):
    random.seed()
    return ''.join([random.choice(alphabet) for i in range(length)])

def getRandomFSM(alphabet_limit: int, state_limit: int, accepts_limit: int) -> FSM:
    assert accepts_limit <= state_limit
    random.seed()
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
    return alphabet, FSM(states, alphabet, state_labels[0], accepts)

def readFSM(des):
    state_labels = [token.strip() for token in des[0].split(",")]
    alphabet = [token.strip() for token in des[1].split(",")]
    start = des[2].strip()
    accepts = [token.strip() for token in des[3].split(",")]
    states = {}
    index = 4
    for i in range(len(state_labels)):
        state_tra = {}
        state = state_labels[i]
        for j in range(len(alphabet)):
            from_state, symbol, to_state = [token.strip() for token in des[index].split(",")]
            state_tra[symbol] = to_state
            index += 1
        states[state] = State(state, state_tra)
    return FSM(states, alphabet, start, accepts)

def readFSMs(filename):
    try:
        lines = [line.strip() for line in open(filename, 'r').readlines()]
    except Exception as e:
        print(e)
        return None
    
    fsms = []
    description = []
    for line in lines:
        if line == "":
            fsms.append(readFSM(description))
            description = []
            continue 
        description.append(line)
    return fsms

if __name__ == "__main__":
    # Get SMALL test FSMs
    fsms = readFSMs("small_test_cases.txt")
    index = 0
    accept = 0
    passed = 0

    # Get SMALL test strings
    for line in [line.strip() for line in open("small_test_strings.txt", 'r').readlines()]:
        result, s = line.split(" ")
        test = fsms[index].doesAccept(s)
        # print("\n" + fsms[index].prettyString() + "\n") #Pretty print FSM
        accept += test
        if test == eval(result):
            test_string = "PASS"
            passed += 1
        else:
            test_string = "FAILED"
        print(f"{index}:\t{test_string}") # Does our evaluation match the one for that string in the file?
        index += 1

    print(f"{accept} / {index} accept") # How many strings were accepted by the corresponding FSMs?
    print(f"{passed} / {index} passed") # How many did your code correctly evaluate?

    # Get LARGE test FSMs
    fsms = readFSMs("test_cases.txt")
    index = 0
    accept = 0
    passed = 0

    # Get LARGE test strings
    for line in [line.strip() for line in open("test_strings.txt", 'r').readlines()]:
        result, s = line.split(" ")
        test = fsms[index].doesAccept(s)
        # print("\n" + fsms[index].prettyString() + "\n") #Pretty print FSM
        accept += test
        if test == eval(result):
            test_string = "PASS"
            passed += 1
        else:
            test_string = "FAILED"
        print(f"{index}:\t{test_string}") # Does our evaluation match the one for that string in the file?
        index += 1

    print(f"{accept} / {index} accept") # How many strings were accepted by the corresponding FSMs?
    print(f"{passed} / {index} passed") # How many did your code correctly evaluate?
    '''
    # Some empirical experimentation 

    total = 100000
    len_limit = 100
    accept = 0

    for i in range(total):
        alphabet, fsm = getRandomFSM(alphabet_limit = 3, state_limit = 8, accepts_limit = 3) # 82% accept
        # alphabet, fsm = getRandomFSM(alphabet_limit = 10, state_limit = 10, accepts_limit = 2) # 48% accept 
        # alphabet, fsm = getRandomFSM(alphabet_limit = 10, state_limit = 10, accepts_limit = 1) # 29% accept 
        rstring = getRandomString(alphabet, random.randint(1, len_limit))
        yes = fsm.doesAccept(rstring)
        accept += yes 
        print(fsm)
        print(rstring)
        print(yes)

    print(f"Accept rate: {100 * accept / total} %")
    '''
