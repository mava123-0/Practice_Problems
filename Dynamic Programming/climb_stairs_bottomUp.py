class Solution:
    def climbStairs(self, n: int) -> int:
        if(n<2):
            return 1
        df = [-1 for i in range(n+1)]
        df[0] = df[1] = 1

        for i in range(2,n+1):
            df[i] = df[i-1]+df[i-2]
        return df[n]