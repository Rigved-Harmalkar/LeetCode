class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        res = set(nums)
        if len(nums) == len(res):
            return False
        else:
            return True
        