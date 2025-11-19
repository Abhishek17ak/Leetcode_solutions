'''
Brute Force Method
For each string, check against every other string to see if they are anagrams (by sorting or counting), and group them together.

Time Complexity: O(n² * k log k), where n = number of strings, k = maximum string length (since sorting each string takes O(k log k))

Space Complexity: O(nk) (for storing groups)
def groupAnagrams(strs):
    n = len(strs)
    used = [False] * n
    result = []
    for i in range(n):
        if not used[i]:
            group = [strs[i]]
            used[i] = True
            for j in range(i + 1, n):
                if not used[j] and sorted(strs[i]) == sorted(strs[j]):
                    group.append(strs[j])
                    used[j] = True
            result.append(group)
    return result
'''

'''
optimal hash table: Time complexity: O(m*n)
Space complexity:O(m) extra space.
O(m*n) space for the output list.
'''
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)             # Dictionary: signature → list of anagrams
        for s in strs:                      # Process each string
            count = [0] * 26                # Count array for 26 letters (a-z)
            for c in s:                     # Count each character in string
                count[ord(c) - ord('a')] += 1  # Increment count for this letter
            res[tuple(count)].append(s)     # Group by character count signature
        return list(res.values())           # Return all groups
#here time complexity is O(m*n) where m is number of strings and n is average length of strings
#space complexity is O(m) for the hashmap and O(m*n) for the output list