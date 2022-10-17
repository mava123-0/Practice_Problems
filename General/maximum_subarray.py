class Solution:
    def maxSubArray(self, nums):
        if(len(nums)==1):
            return nums[0]
        ans = nums[0]
        ans_arr = []
        ans_arr.append(ans)
        nums.pop(0)
        for j in nums:
            ans += j
            ans = max(ans, j)
            ans_arr.append(ans)
        return max(ans_arr)