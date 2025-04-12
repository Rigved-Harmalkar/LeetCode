class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = float("-inf")
        start = -1
        end = -1
        summ = 0
        for i in range(len(nums)):
            summ += nums[i]

            if summ > max_sum:
                end = i
                max_sum = summ
            
            if summ < 0:
                start = i + 1
                summ = 0
        return max_sum


        