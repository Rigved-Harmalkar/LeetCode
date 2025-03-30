class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        lis = []
        num_set = set(nums)

        for i in range(1,len(nums)+1):
            if i not in num_set:
                lis.append(i)
        return lis
    

            
                


        