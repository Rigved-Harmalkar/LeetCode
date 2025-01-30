class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        res = dict()

        right = 0

        while right <= len(nums) - 1 :
            if nums[right] in res:
                if right - res[nums[right]] <= k:
                    return True
            res[nums[right]] = right
            right += 1
        return False

        