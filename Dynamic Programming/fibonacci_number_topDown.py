class Solution:
    def fib(self, n: int) -> int:

        def sol(n,mem):
            if(n==0):
                return 0
            if(n<3):
                return 1
            if(mem[n-1]!=-1):
                return mem[n-1]
            val = sol(n-1,mem)+sol(n-2,mem)
            mem[n-1] = val
            return val
        
        mem = [-1 for i in range(n)]
        return sol(n,mem)