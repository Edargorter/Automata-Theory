# Automata-Theory
Some simulations of theoretical machines (including Finite Automata) found in the field of Automata Theory, for educational and empirical scientific purposes.

## Test case schema:
``` 
q_0, q_1                # states
0, 1                    # alphabet
q_0                     # start
q_0, q_1                # accepting states 
q_0, 0, q_1             # Transitions (|states| x |alphabet| lines)  "from_state, symbol, to_state"
q_0, 1, q_1				
q_1, 0, q_0
q_1, 1, q_1
------------------------ BLANK LINE -----------------------
q_0, q_1, q_2, q_3, ... # Next FSM
.
.
.

``` 

## Measure time on Linux
```
time ./finite-automata.py
```
Output:
```
2377 out of 10000 accept

real    0m1.974s
user    0m1.889s
sys     0m0.084s
```
