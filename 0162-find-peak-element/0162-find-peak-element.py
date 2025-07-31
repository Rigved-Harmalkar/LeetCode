class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        n = len(nums)

        if n == 1:
            return 0
        
        low = 1
        high = n - 2

        if nums[0] > nums[1]:
            return 0

        if nums[n-1] > nums[n-2]:
            return n-1 

        while low <= high:
            mid = (low+high) // 2

            # To find the peek element
            if nums[mid-1] < nums[mid] and nums[mid] > nums[mid+1]:
                return mid

            elif nums[mid-1] < nums[mid] and nums[mid] < nums[mid+1]:
                low = mid + 1
            
            elif nums[mid-1] > nums[mid] and nums[mid] > nums[mid+1]:
                high = mid - 1

            else:
                low = mid + 1
            
        return -1
         