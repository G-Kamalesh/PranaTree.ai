class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        bp = prices[0]
        p = 0
        check = []
        for i in range(1,len(prices)):
            if prices[i] < bp:
                bp = prices[i]
            if prices[i] > bp:
                p = prices[i] - bp
                check.append(p)
        if check:
            h = max(check)
            if h < 0:
                return 0
            else:
                return h
        else:
            return 0
        