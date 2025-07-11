#if new interval overlaps then modify like (1,3) and (2,5) overlap then (1,5)
#if not overlap, add directly
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda pair: pair[0])    # Sort by start time
        output = [intervals[0]]                     # Start with first interval

        for start, end in intervals:                # Process each interval
            lastEnd = output[-1][1]                 # End of last interval in output

            if start <= lastEnd:                    # Overlap detected
                output[-1][1] = max(lastEnd, end)   # Merge by extending end time
            else:                                   # No overlap
                output.append([start, end])         # Add as new interval
                
        return output
