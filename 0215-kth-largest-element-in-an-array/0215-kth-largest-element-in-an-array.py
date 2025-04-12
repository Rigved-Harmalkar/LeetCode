import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        max_val = max(nums)
        min_val = min(nums)

        count = [0] * (max_val-min_val+1)

        for num in nums:
            count[num-min_val] += 1
        
        for i in range(len(count)-1,-1,-1):
            k -= count[i]
            if k <= 0:
                return min_val + i
                
        