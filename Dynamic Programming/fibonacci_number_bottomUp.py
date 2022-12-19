class Solution:
    def fib(self, n: int) -> int:
        if(n==0):
            return 0
        if(n<3):
            return 1
        fib = [-1 for i  in range(n)]
        fib[0] = fib[1] = 1
        for i in range(2,n):
            fib[i] = fib[i-1]+fib[i-2]
        return fib[i]