class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)-1
        mem = [-1 for i in range(n+1)]
        print(mem)

        def dp_sol(nums,index,mem):
            if(index == 0):
                return nums[index]
            if(index<0):
                return 0
            if(mem[index] != -1):
                return mem[index]
            pick = nums[index]+dp_sol(nums,index-2,mem)
            notpick = dp_sol(nums,index-1,mem)
            mem[index] = max(pick,notpick)
            return max(pick,notpick)

        return dp_sol(nums,n,mem)