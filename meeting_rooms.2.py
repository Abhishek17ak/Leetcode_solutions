"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
#create two arrays to track start and end times, then comapre using two pointers,
#the amount of meetings going on around same time and increase count
#so find maximum amount of meetings going on around same to find rooms required

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        start = sorted([i.start for i in intervals])    # All start times, sorted
        end = sorted([i.end for i in intervals])        # All end times, sorted
        
        res = count = 0                                 # Track max rooms and current rooms
        s = e = 0                                       # Pointers for start and end arrays
        
        while s < len(intervals):                       # Process all meetings
            if start[s] < end[e]:                       # Meeting starts before earliest end
                s += 1                                  # Move to next start time
                count += 1                              # Need one more room
            else:                                       # Meeting starts after/when earliest ends
                e += 1                                  # Move to next end time
                count -= 1                              # Free up one room
            res = max(res, count)                       # Track maximum rooms needed
            
        return res
