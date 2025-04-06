class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2  # Calculating the mid

            # mid is target
            if nums[mid] == target:
                return mid

            # target is on the left side

            if nums[mid] >= nums[left]:
                if target >= nums[left] and target <= nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1

            # target is on the right side
            else:
                if target <= nums[right] and target >= nums[mid]:
                    left = mid + 1
                else:
                    right = mid - 1
        return -1
            