class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        even = []
        odd = []

        for i in range(len(nums)):
            if nums[i] > 0:
                even.append(nums[i])
            else:
                odd.append(nums[i])

        left = 0
        e = 0
        r = 0
        while left < len(nums):
            if left % 2 == 0:
                nums[left] = even[e]
                e += 1
            else:
                nums[left] = odd[r]
                r += 1
            left += 1
        return nums

        