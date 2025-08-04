class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low = 1
        high = self.find_max(piles)

        while low <= high:
            mid = (low+high) // 2
            time = self.time_taken(piles,mid)
            
            if time > h:
                low = mid + 1
            else:
                high = mid - 1
                
        return low

    def find_max(self,arr):
        max_val = float("-inf")

        for num in arr:
            if num > max_val:
                max_val = num

        return max_val

    def time_taken(self,arr,e):
        total_hours = 0
        for i in range(len(arr)):
            
            # if koko is eating more than pile
            if e > arr[i]:
                total_hours += 1
            
            else:
                total_hours += math.ceil(arr[i]/e)
                
        return total_hours