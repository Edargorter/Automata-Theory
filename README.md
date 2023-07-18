# Automata-Theory
Some simulations of theoretical machines (including Finite Automata) found in the field of Automata Theory, for educational and empirical scientific purposes.

# Read input as follows, 
``` 
    q_0, q_1				# states
    0, 1					# alphabet
    q_0						# start
    q_0, q_1				# accept
    q_0, 0, q_1			# Transitions lines = |states| x |alphabet|
    q_0, 1, q_1			# from_state, symbol, to_state
    q_1, 0, q_0
    q_1, 1, q_1
	----------------- BLANK LINE ----------------
	q_0, q_1, q_2, q_3, ...	# Next FSM
	... etc.
``` 
