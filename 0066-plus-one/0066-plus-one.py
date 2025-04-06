class Solution:
    def plusOne(self, nums: List[int]) -> List[int]:
        res = []
        ele = ""
        for num in nums:
            ele += str(num)
        ele = str(int(ele) + 1)
        for i in range(len(ele)):
            res.append(int(ele[i]))
        return res
        