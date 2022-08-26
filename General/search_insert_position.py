class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        for i in range(len(nums)):
            if(nums[i]==target):
                return i
            # elif(nums[i]>target):
            elif(nums[i]>target):
                if(i<0):
                    return 0
                else:
                    return i
            elif(i==len(nums)-1):
                return i+1