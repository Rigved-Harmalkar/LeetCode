class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = right = 0
        max_sum = 0
        
        while right < len(prices) - 1:
            
            if prices[right] >= prices[left]:
                right += 1
            else:
                left = right
                right += 1
            summ = prices[right] - prices[left]
                
            max_sum = max(summ,max_sum)
            
        return 0 if max_sum < 0 else max_sum