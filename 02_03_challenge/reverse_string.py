"""
Python Data Structures - A Game-Based Approach
Stack challenge
Robin Andrews - https://compucademy.net/
"""

import stack

string = "gninraeL nIdekniL htiw tol a nraeL"
reversed_string = ""
s = stack.Stack()

# Your solution here.
def reverse_string(my_string):
    reversed_string = ""
    for c in my_string:
        s.push(c)
    while s.size() > 0:
        reversed_string += s.pop()
        
    return reversed_string

reversed_string = reverse_string(string)    
print(reversed_string)
