class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float('inf')
        max_profit = 0
        
        for price in prices:
            # Update the minimum price if a lower price is found
            if price < min_price:
                min_price = price
            # Calculate the profit if we sell at the current price and update max_profit
            else:
                profit = price - min_price
                max_profit = max(max_profit, profit)
                
        return max_profit