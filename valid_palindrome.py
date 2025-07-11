'''
Brute Force Method
Filter out non-alphanumeric characters, convert to lowercase, and 
check if the cleaned string equals its reverse.

Time Complexity: O(n)

Space Complexity: O(n) (for the cleaned string)

def isPalindrome(s):
    cleaned = ''.join(c.lower() for c in s if c.isalnum())
    return cleaned == cleaned[::-1]

'''
'''Optimal Method (Two Pointers, In-Place)
Use two pointers from both ends, skipping non-alphanumeric characters, 
and compare characters in a case-insensitive way.

Time Complexity: O(n)

Space Complexity: O(1) (no extra space except a few variables)'''

class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1                    # Two pointers: left and right

        while l < r:                            # While pointers haven't met
            while l < r and not self.alphaNum(s[l]):  # Skip non-alphanumeric from left
                l += 1
            while r > l and not self.alphaNum(s[r]):  # Skip non-alphanumeric from right
                r -= 1
            if s[l].lower() != s[r].lower():    # Compare characters (case-insensitive)
                return False
            l, r = l + 1, r - 1                # Move both pointers inward
        return True
    
    def alphaNum(self, c):                      # Helper: check if character is alphanumeric
        return (ord('A') <= ord(c) <= ord('Z') or 
                ord('a') <= ord(c) <= ord('z') or 
                ord('0') <= ord(c) <= ord('9'))
