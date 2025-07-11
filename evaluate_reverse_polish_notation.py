'''
Brute Force Method
Simulate the evaluation by repeatedly scanning the tokens array to find the first operator,
then replace the operator and its two preceding operands with the result, 
and repeat until one value remains.

Time Complexity: O(n²) (since each operation reduces the array size by 2, but each scan may be O(n))

Space Complexity: O(n) (for the intermediate array)

def evalRPN(tokens):
    while len(tokens) > 1:
        for i in range(len(tokens)):
            if tokens[i] in "+-*/":
                a, b = int(tokens[i-2]), int(tokens[i-1])
                if tokens[i] == "+":
                    res = a + b
                elif tokens[i] == "-":
                    res = a - b
                elif tokens[i] == "*":
                    res = a * b
                else:
                    res = int(float(a) / b)
                tokens = tokens[:i-2] + [str(res)] + tokens[i+1:]
                break
    return int(tokens[0])

'''

'''
Optimal Method (Stack)
Use a stack: for each token, if it's a number, push to stack; 
if it's an operator, pop two numbers, apply the operation, 
and push the result back. At the end, the stack contains the result.

Time Complexity: O(n) (each token is processed once)

Space Complexity: O(n) (stack can grow up to n/2)
'''

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []                              # Stack to store numbers
        for c in tokens:                        # Process each token
            if c == "+":                        # Addition
                stack.append(stack.pop() + stack.pop())
            elif c == "-":                      # Subtraction  
                a, b = stack.pop(), stack.pop()
                stack.append(b - a)
            elif c == "*":                      # Multiplication
                stack.append(stack.pop() * stack.pop())
            elif c == "/":                      # Division
                a, b = stack.pop(), stack.pop()
                stack.append(int(float(b) / a))
            else:                               # It's a number
                stack.append(int(c))
        return stack[0]                         # Final result
