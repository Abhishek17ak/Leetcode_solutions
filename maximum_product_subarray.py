class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]                           # Track overall maximum product
        curMin, curMax = 1, 1                   # Track current min and max products

        for num in nums:
            tmp = curMax * num                  # Save current max before updating
            curMax = max(num * curMax, num * curMin, num)  # New maximum product
            curMin = min(tmp, num * curMin, num)           # New minimum product
            res = max(res, curMax)              # Update global maximum
            
        return res
