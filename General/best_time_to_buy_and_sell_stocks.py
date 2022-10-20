class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        curmin = max(prices)
        curmax = 0
        for x in prices:
            if (x<curmin):
                curmin = x
            if(x-curmin>curmax):
                curmax = x-curmin
        return curmax