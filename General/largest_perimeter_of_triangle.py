class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        arr = sorted(nums)
        for i in range(len(nums)-3,-1,-1):
            print(arr[i],arr[i+1],arr[i+2])
            if(arr[i+1]+arr[i]>arr[i+2]):
                return arr[i+1]+arr[i+2]+arr[i]
        return 0