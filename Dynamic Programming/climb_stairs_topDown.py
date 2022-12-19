class Solution:
    def climbStairs(self, n: int) -> int:
        mem = [-1 for i in range(n)]
        def climbStair(n,mem,tabs=""):
            if(n < 2):
                return 1
            if(mem[n-1]!=-1):
                return mem[n-1]
            one_j = climbStair(n-1,mem,tabs+'\t')
            two_j = climbStair(n-2,mem,tabs+'\t')

            mem[n-1] = one_j+two_j
            
            return one_j+two_j

        return climbStair(n,mem)