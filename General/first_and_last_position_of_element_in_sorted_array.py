class Solution(object):
    def searchRange(self, nums, target):
        err=[]
        flag=0
        for i in range(0,len(nums)):
            if(nums[i]==target):
                flag=1
                err.append(i)
                if(i+1<len(nums)):
                    while(nums[i+1]==target):
                        i+=1
                        if(i+1==len(nums)):
                            break
                err.append(i)
                break
        if(flag==0):
            arr=[-1,-1]
            return arr
        else:
            return err