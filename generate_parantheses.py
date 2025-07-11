'''
Generate all possible sequences of 2n parentheses. For each sequence, 
check if it is valid (well-formed) by counting the balance of open and close parentheses.

Time Complexity: O(2^(2n) * n) (all possible sequences, each checked for validity)

Space Complexity: O(2^(2n) * n) (store all sequences)

def generateParenthesis(n):
    def isValid(seq):
        bal = 0
        for c in seq:
            if c == '(': bal += 1
            else: bal -= 1
            if bal < 0: return False
        return bal == 0

    from itertools import product
    res = []
    for seq in product("()", repeat=2*n):
        s = "".join(seq)
        if isValid(s):
            res.append(s)
    return res

'''

'''
Optimal Method (Backtracking)
Build the string by adding '(' or ')' only when it keeps the string valid. 
Use backtracking to generate all valid combinations.

Time Complexity: O(4^n / sqrt(n)) (Catalan number, number of valid combinations)

Space Complexity: O(4^n / sqrt(n)) (for the result list)
'''

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []                          # Build current combination
        res = []                            # Store all valid combinations
        
        def backtrack(openn, closen):       # openn = open count, closen = close count
            if openn == closen == n:        # Base case: complete valid combination
                res.append("".join(stack))
                return
            
            if openn < n:                   # Can add opening parenthesis?
                stack.append("(")
                backtrack(openn + 1, closen)
                stack.pop()                 # Backtrack
                
            if closen < openn:              # Can add closing parenthesis?
                stack.append(")")
                backtrack(openn, closen + 1)
                stack.pop()                 # Backtrack
                
        backtrack(0, 0)                     # Start with 0 open, 0 close
        return res
