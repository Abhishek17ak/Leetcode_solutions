class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()                        # Sort intervals by start time
        res = 0                                 # Count of intervals to remove
        prevEnd = intervals[0][1]               # End time of last kept interval
        
        for start, end in intervals[1:]:        # Check each interval after the first
            if start >= prevEnd:                # No overlap
                prevEnd = end                   # Keep this interval
            else:                               # Overlap detected
                res += 1                        # Remove one interval
                prevEnd = min(end, prevEnd)     # Keep the one that ends earlier
        return res
