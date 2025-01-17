class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        break_ele = -1

        # find the breakpoint
        for i in range(len(nums)-2,-1,-1):
            if nums[i] < nums[i+1]:
                break_ele = i
                break
        if break_ele == -1:
            nums.reverse()
            return nums

        # find the smallest after break_ele
        for i in range(len(nums)-1,break_ele,-1):
            if nums[i] > nums[break_ele]:
                nums[i], nums[break_ele] = nums[break_ele], nums[i]
                break


        # reverse after break_ele

        nums[break_ele+1:] = reversed(nums[break_ele+1:])

        return nums

            
        