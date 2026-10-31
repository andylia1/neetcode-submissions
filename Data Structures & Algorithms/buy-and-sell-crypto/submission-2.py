class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buyInd = 0
        maxSell = 0

        for sell in range(1, len(prices)):
            maxSell = max(maxSell, prices[sell] - prices[buyInd])
            if prices[sell] < prices[buyInd]:
                buyInd = sell

        return maxSell