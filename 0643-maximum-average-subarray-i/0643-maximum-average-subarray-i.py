class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        summ = sum(nums[:k])
        max_avg = summ/k
        i = 0
        while i + k < len(nums):
            summ += nums[i+k] - nums[i]
            max_avg = max(max_avg,summ/k)
            i+=1
        return max_avg
        