class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        i = 1 
        res = []
        num_set = set(nums)  
        while i <= len(nums):  
            if i not in num_set:  
                res.append(i)  
            i += 1  
        return res 

            
                


        