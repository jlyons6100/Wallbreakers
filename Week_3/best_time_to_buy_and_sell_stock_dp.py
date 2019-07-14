class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 0:
            return 0
        n = len(prices)
        diff_matrix = []
        diff_matrix.append(0)
        for i in range(0,n-1):
            diff_matrix.append(prices[i+1] - prices[i])
        summ = self.max_sum(diff_matrix, 0, n-1)
        return summ
    
    def find_sum(self, prices, low, mid, high):
        r = -1
        cur = 0
        for i in range(mid + 1, high + 1, 1):
            cur += prices[i]
            r = max(r, cur)
        l = -1
        cur = 0
        for i in range(mid, low-1, -1):
            cur += prices[i]
            l = max(l, cur)
        return l + r
    
    def max_sum(self, prices, low, high):
        if low == high:
            return prices[low]
        mid = (low + high) // 2
        l_max = self.max_sum(prices, low, mid)
        m_max = self.find_sum(prices, low, mid, high)
        r_max = self.max_sum(prices, mid+1, high)
        return max(m_max, max(l_max, r_max))
    