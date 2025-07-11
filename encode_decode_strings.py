'''
time:(m) for both
space:(m+n) for both
m= sum of lengths of all strings
n= no of strings'''
class Solution:
    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res    # <-- should return res, not s

    def decode(self, s: str) -> List[str]:
        res, i = [], 0
        while i < len(s):   # <-- use s, not str
            j = i
            while s[j] != "#":   # <-- use s, not str
                j += 1
            length = int(s[i:j])
            res.append(s[j+1:j+1+length])
            i = j + 1 + length
        return res
