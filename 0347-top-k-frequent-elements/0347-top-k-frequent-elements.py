import heapq
from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        freq = Counter(nums)

        min_heap = []

        for idx,count in freq.items():
            heapq.heappush(min_heap,(count,idx))

            if len(min_heap) > k:
                heapq.heappop(min_heap)

        return [num for count,num in min_heap]

        
        