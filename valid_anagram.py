'''
Brute Force Method
Sort both strings and compare if they are equal.

Time Complexity: O(n log n) (due to sorting, where n is the length of the strings)
Space Complexity: O(n) (space for sorted strings)

def isAnagram(s, t):
    return sorted(s) == sorted(t)
'''
'''
Optimal Method (Hash Map/Array Counting)
Count the frequency of each character in both strings and compare the counts.

Time Complexity: O(n)

Space Complexity: O(1) (since the alphabet size is constant, 26 for lowercase English letters)
'''

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

      

        #using hashmap
        #first check if length is same
        if len(s)!= len(t):
            return False
        #create Hashmaps    
        countS, countT= {},{}

        for i in range(len(s)):
            countS[s[i]]=1+countS.get(s[i],0)
            countT[t[i]]=1+countT.get(t[i],0)
        return countS == countT

