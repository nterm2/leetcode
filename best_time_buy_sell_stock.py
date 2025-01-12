class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        start_pointer = 0
        next_pointer = 1
        current_profit = 0
        if len(prices) < 2:
            return 0
        while (next_pointer < len(prices)):
            if (prices[start_pointer] >= prices[next_pointer]):
                start_pointer = next_pointer
                next_pointer += 1
            else:
                if (prices[next_pointer] - prices[start_pointer] > current_profit):
                    current_profit = prices[next_pointer] - prices[start_pointer]
                next_pointer += 1
        return current_profit
