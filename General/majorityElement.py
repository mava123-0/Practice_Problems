class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        arr = []
        arrcount = []
        for i in range(len(nums)):
            if(nums[i] not in arr):
                arr.append(nums[i])
                arrcount.append(1)
            else:
                arrcount[arr.index(nums[i])] += 1
        if (max(arrcount) >= len(nums)/2):
            return arr[arrcount.index(max(arrcount))]
        return 