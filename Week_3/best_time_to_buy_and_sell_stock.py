class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxp = 0
        minp = sys.maxsize
        for x in range(len(prices)):
            price = prices[x]
            if price < minp:
                minp = price
            elif price - minp > maxp:
                maxp = price - minp
        return maxp