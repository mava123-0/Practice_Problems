class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        if(nums):
            index=0
            for i in range(len(nums)):
                if(pivot==nums[i]):
                    index=i
                    break
            left_arr=[]
            right_arr=[]
            eq_arr=[]
            for i in range(len(nums)):
                if(nums[i]<pivot):
                    left_arr.append(nums[i])
                elif(nums[i]>pivot):
                    right_arr.append(nums[i])
                elif(nums[i]==pivot):
                    eq_arr.append(nums[i])
            arr=[]
            arr=left_arr+eq_arr+right_arr
            return arr