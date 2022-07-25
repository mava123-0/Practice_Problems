class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        arr=nums
        arr.sort()
        n=k
        if((len(arr)-n)>0 or len(arr)-n==0):
            return arr[len(arr)-n]
        return