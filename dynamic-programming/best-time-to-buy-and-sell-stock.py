class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """ 
        Intuition:
            Sort of a State Machine?

            On any given day, you can either:
                Buy, Sell, or Rest
                You can only Buy if: You haven't Sold
                You can only Sell if: You have Bought and sell only for idx > idx you bought
                You can Rest in either State

            for a given day
                Try: Buy or Rest
                    If Buy then next day: Sell or Rest
                    If Rest then next day: Buy or Rest

        Or you can do greedy option since its simple enough
            On every day, compute min_price and max_profit
                min_price = min(min_price, current_price)
                max_profit = max(max_profit, current_price - min_price)
                    If min_price is the same day as current_price -> profit = 0 
        """

        def greedy():
            min_price = float('inf')
            max_prof = 0

            for price in prices:
                min_price = min(min_price, price)
                max_prof = max(max_prof, price - min_price)
            return max_prof
        return greedy()