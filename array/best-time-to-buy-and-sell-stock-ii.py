class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        Intuition:
            - State Machine
            - Greedy Approach

        Greedy Approach:
            Since we can make unlimited transactions, the maximum profit is obtained by
                    capturing every positive price increase.
            Therefore,
                Max Profit = Sum of all positive daily price differences.

            For every pair of consecutive days,
                if prices[i] > prices[i - 1]:
                    profit += prices[i] - prices[i - 1]

            This works because a continuous increase

                Buy at a, Sell at d

            has the same profit as
                Buy at a, Sell at b
                Buy at b, Sell at c
                Buy at c, Sell at d
            since
                (b - a) + (c - b) + (d - c) = d - a.

            Thus, summing every positive increase is equivalent to buying at each local
                minimum and selling at the next local maximum.
        """
        
        @cache
        def state_machine(day, holding):
            if day == len(prices):
                return 0
            
            # Doesn't change holding status since rest
            rest = state_machine(day + 1, holding = holding)

            if holding:
                # Add with the profits from future days if today we choose to Sell
                sell = prices[day] + state_machine(day + 1, False)
                return max(rest, sell) # Take the best profit between Rest and Sell
            else:
                # Add with the profits from future days if today we choose to Buy
                buy = -prices[day] + state_machine(day + 1, True)
                return max(rest, buy) # Take the best profit between Buy and Rest
        #return state_machine(0, False)

        def greedy():
            profit = 0
            for i in range(len(prices) - 1):
                future_price = prices[i+1]
                curr_price = prices[i]
                if future_price > curr_price:
                    profit += future_price - curr_price
            return profit
        return greedy()

