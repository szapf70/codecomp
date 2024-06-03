# https://www.codewars.com/kata/64b84ed4b46f91004b493d87/train/python
# Play Nerdle - It's Wordle for Calculations

def solve_micro_nerdle(history):
    ## history is a list [(guess1, feedback1), (guess2, feedback2), ....]. 
    ## Each element is a tuple containing a previous guess with the feedback it received.
    ## The most recent guess is the last element of history.
    
    if history == []: guess = '1+2=3' ## guess = any valid arithmetic expression of length 5
    else: guess = '1+2=3' ## CHANGE THIS: guess = what could target expression be, based on history
    
    return guess

