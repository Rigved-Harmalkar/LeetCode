class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        low = 0
        high = len(nums) - 1

        if len(nums) == 1:
            return nums[0]
        elif nums[low] != nums[low+1]:
            return nums[low]
        elif nums[high] != nums[high-1]:
            return nums[high]

        else:

            while low <= high:
                mid = (low+high) // 2

                if nums[mid] == nums[mid-1]:
                    if (mid-1) % 2 == 0:
                        low = mid + 1
                    else:
                        high = mid - 1

                elif nums[mid] == nums[mid+1]:
                    if (mid+1) % 2 == 0:
                        high = mid - 1
                    else:
                        low = mid + 1
                else:
                    return nums[mid]

        
        