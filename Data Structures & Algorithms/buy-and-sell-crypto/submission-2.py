class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        minVal = prices[0]

        for val in prices :
            maxProfit = max(maxProfit, val - minVal)
            minVal = min(minVal,val)
        
        return maxProfit
        