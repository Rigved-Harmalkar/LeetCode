class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        if 0 not in nums:
            return 0
        for i in range(len(nums)):
            if i + 1 not in nums:
                return i + 1

            
        