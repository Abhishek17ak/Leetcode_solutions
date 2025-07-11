#LIS[n]=a
#LIS[n-1]=b,1+a
#LIS[n-1]=max(a,LIS[n]) ,if nums[n-1]<nums[n]
#LIS[n-2]=max(b,1+LIS[n-1],1+LIS[n]), if nums[n-2]<nums[n-1] , nums[n-2]<nums[n]
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        LIS = [1] * len(nums)                   # LIS[i] = length of LIS starting from index i

        for i in range(len(nums) - 1, -1, -1):  # Work backwards from end to start
            for j in range(i + 1, len(nums)):   # Check all elements after position i
                if nums[i] < nums[j]:           # Can extend sequence from i to j
                    LIS[i] = max(LIS[i], 1 + LIS[j])  # Take best option
                    
        return max(LIS)                         # Return longest sequence found

        