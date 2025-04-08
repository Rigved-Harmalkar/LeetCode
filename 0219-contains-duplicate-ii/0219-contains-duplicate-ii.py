class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        dictt = {}

        for i in range(len(nums)):
            if nums[i] in dictt:
                length = i - dictt[nums[i]]
                if length <= k:
                    return True
            dictt[nums[i]] = i
        return False
        
        