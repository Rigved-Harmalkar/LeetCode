class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        low = 0
        high = len(nums) - 1

        while low <= high:
            mid = (low+high) // 2
            if nums[mid] == target:

                #to find the last element
                while mid <= high:
                    if nums[mid] == target:
                        last = mid
                        mid += 1
                    else:
                        break

                mid = mid - 1
                while mid >= low:
                    if nums[mid] == target:
                        first = mid
                        mid -= 1
                    else:
                        break
                return [first,last]

            elif nums[mid] < target:
                low = mid + 1

            else:
                high = mid - 1

        return [-1,-1] 


        
        