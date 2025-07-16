class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        total_sum = 0
        max_sum = float("-inf")

        for i in range(len(nums)):
            total_sum += nums[i]
            max_sum = max(total_sum,max_sum)
            if total_sum < 0:
                total_sum = 0
            
        return max_sum
        