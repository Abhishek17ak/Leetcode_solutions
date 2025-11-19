#1. Two sum
seen=set()
for num in nums:
    if num in seen:
        return True
    seen.add(num)
return False

#2. valid anagram
if len(s)!=len(t):
    return False
    countS,countT={},{}
    for i in range(len(s)):
        countS[s[i]]=1 +countS.get(s[i],0)
        countT[t[i]]=1 +countT.get(t[i],0)
    return countS==countT
#3.two sum
mapi={}
for i,n in enumerate(nums):
    diff = target-n
    if diff in mapi:
        return [mapi[diff],i]
    mapi[n]=i

#4. group anagrams
res=defaultdict(list)
for s in str:
    count=[0]*26
    for c in s:
        count[ord(c)-ord('a')]+=1
    res[tuple(count)].append(s)
return list(res.values())
#5.k most frequent elements
count={}
for num in nums:
    count[num]=1+count.get(num,0)
heap=[]
for num in count.keys():
    heapq.heappush(heap,(count[num],num))
    if len(heap)>k:
        heapq.heappop(heap)
    res=[]
    for i in range(k):
        res.append(heapq.heappop(heap)[1])
    return res
#6. encode and decode strings

#encode:
res=""
for s in strs:
    res+=str(len(s))+"#"+s
    return str
#decode:
res,i=[],0
while i<len(s):
    j=i
    while s[j]!="#":
        j+=1
    length=int(s[i:j])
    res.append(s[j+1:j+1+length])
    1=j+1+length
return res

#7. product of array excpet itself
n=len(nums)
res=[0]*n
pre=[0]*n
suf=[0]*n

pre[0]=suf[n-1]=1

for i in range(1,n):
    pre[i]=nums[i-1]*pre[i-1]
for i in range(n-2,-1,-1):
    suf[i]=nums[i+1]*suf[i+1]
for i in range(n):
    res[i]=pre[i]*suf[i]
return res

#8. valid sudoku

cols = collections.defaultdict(set)      
rows = collections.defaultdict(set)      
squares = collections.defaultdict(set) 
for r in range(9):
    for c in range(9):
        if board[r][c]=".":
            continue
        if (board[r][c] in rows[r] or
            board[r][c]in cols{c}or 
            board[r][c] in squares[(r//3),(c//3)]):
            return False
        cols[c].add(board[r][c])
        rows[r].add(board[r][c])
        squares[(r//3),(c//3)].add(board[r][c])
return True