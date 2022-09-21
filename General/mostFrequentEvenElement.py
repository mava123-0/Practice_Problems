class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        arr = []
        arrcount = []
        nums.sort()
        for i in range(len(nums)):
            if(nums[i]%2==0 and nums[i] not in arr):
                arr.append(nums[i])
                arrcount.append(1)
            elif (nums[i]%2==0):
                arrcount[len(arrcount)-1] = arrcount[len(arrcount)-1]+1
        if(arrcount):
            return arr[arrcount.index(max(arrcount))]
        return -1