def max_profit(prices, i, n, can_sell, mem):
    if i >= len(prices) or n == 0: 
        # We have reached the end of the prices array, or can't perform any more transactions
        # Our profit from this point on is 0 in this case
        return 0
    elif (i, n, can_sell) in mem:
        # This state was previously encountered - return the memorized value
        return mem[(i, n, can_sell)]
    
    # Buy the stock if we aren't holding any, or sell it otherwise
    do = max_profit(prices, i+1, n-1, not can_sell, mem) + (prices[i] if can_sell else -prices[i])
    # Skip the position without buying/selling
    skip = max_profit(prices, i+1, n, can_sell, mem)
    
    mem[(i, n, can_sell)] = max(do, skip)
    return mem[(i, n, can_sell)]

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        return max_profit(prices, 0, 4, False, {})