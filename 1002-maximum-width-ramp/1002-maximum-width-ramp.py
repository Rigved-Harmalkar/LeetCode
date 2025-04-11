class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        n = len(nums)
        st = []

        for i in range(len(nums)):
            while not st or nums[st[-1]] > nums[i]:
                st.append(i)

        max_width = 0

        for j in range(len(nums)-1,-1,-1):
            while st and nums[st[-1]] <= nums[j]:
                max_width = max(max_width,j-st.pop())

        return max_width 