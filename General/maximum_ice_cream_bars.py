class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        # mem = [-1 for _ in range(len(costs))]
        costs.sort()
        res = 0 
        i=0

        while(i<len(costs) and coins>=costs[i]):
            res+=1
            coins-=costs[i]
            i+=1
        
        return res