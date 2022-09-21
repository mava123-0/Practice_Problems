class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans = [[]]
        nums.sort()
        if(len(nums) != 0):
            for num in nums:
                for j in range(len(ans)):
                    if (ans[j]+[num] not in ans):
                        (ans.append(ans[j]+[num])) 
        return ans