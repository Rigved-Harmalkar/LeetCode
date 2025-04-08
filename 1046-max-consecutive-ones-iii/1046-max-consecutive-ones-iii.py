class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = 0
        right = 0
        counter = 0
        max_sum = 0

        while right < len(nums):
            if nums[right] == 0:
                counter += 1

            while counter > k:
                if nums[left] == 0:
                    counter -= 1
                left += 1

            max_sum = max(max_sum, right - left + 1)

            right += 1



        return max_sum
        