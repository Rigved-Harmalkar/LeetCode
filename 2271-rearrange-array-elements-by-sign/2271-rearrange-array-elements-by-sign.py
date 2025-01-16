class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        pos = []
        neg = []

        for num in nums:
            if num >= 0:
                pos.append(num)
            else:
                neg.append(num)

        count = 0
        count_nums = 0
        while count_nums <= len(nums)-1:
                if count_nums % 2 == 0:
                    nums[count_nums] = pos[count]
                    count_nums += 1
                else:
                    nums[count_nums] = neg[count]
                    count_nums += 1
                    count += 1
        return nums
        