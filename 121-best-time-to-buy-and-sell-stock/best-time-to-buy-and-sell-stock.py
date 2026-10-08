class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        profit=0
        min_price=prices[0]
        for i in range(1,len(prices)):
            current_profit=prices[i]-min_price
            if (current_profit > profit):
                profit=current_profit
            min_price=min(min_price,prices[i])
        return profit
        
        

        
        
       