#brute force( linear search): This code inserts a new interval into a sorted list of 
#non-overlapping intervals by first adding all intervals before it, 
#then merging any overlapping ones, and finally appending the remaining intervals.
#(n),((1) for extra space,(n) space for o/p list) for both solutions
#greedy method
#if new interval overlaps then modify like (1,3) and (2,5) overlap then (1,5)
#if not overlap, add directly
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []

        for i in range(len(intervals)):
            if newInterval[1] < intervals[i][0]:           # Case 1: No overlap, newInterval comes before
                res.append(newInterval)
                return res + intervals[i:]
            elif newInterval[0] > intervals[i][1]:         # Case 2: No overlap, newInterval comes after
                res.append(intervals[i])
            else:                                          # Case 3: Overlap, merge intervals
                newInterval = [
                    min(newInterval[0], intervals[i][0]),  # Take earlier start
                    max(newInterval[1], intervals[i][1]),  # Take later end
                ]
        res.append(newInterval)                            # Add final newInterval
        return res
