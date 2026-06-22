class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) <= 1: return 0
        
        low = 0 
        high = 1
        maxVal = prices[high]-prices[low]
        for i in range(1,len(prices)) :
            if prices[i] > prices[high] :
                high = i
                maxVal = prices[high] - prices[low] if maxVal < prices[high] - prices[low] else maxVal
            elif prices[i] < prices[low] :
                low = i
                high = i

        return maxVal if maxVal > 0 else 0
        