#brute force This code uses recursion to count the number of ways to climb `n` stairs,
#where you can take either 1 or 2 steps at a time. It tries all paths starting from step 0
#and adds up the valid ones that reach exactly step `n`.(2^n)(n)

#follows fibonacci series, dynamic programming
class Solution:
    def climbStairs(self, n: int) -> int:
        one, two = 1, 1                     # Base cases: ways to reach steps 1 and 2

        for i in range(n - 1):              # Calculate for steps 3 to n
            temp = one                      # Store current value of 'one'
            one = one + two                 # New ways = previous two ways combined
            two = temp                      # Move the old 'one' to 'two'
        
        return one                          # Return ways to reach step n
#(n)(1)
