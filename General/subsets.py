class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = [[]]
        if(len(nums) != 0):
            for num in nums:
                for j in range(len(ans)):
                    ans.append(ans[j]+[num])
        return ans