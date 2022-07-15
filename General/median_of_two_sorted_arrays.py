class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        farr=[]
        for i in range(len(nums1)):
            farr.append(nums1[i])
        for i in range(len(nums2)):
            farr.append(nums2[i])
        farr.sort()
        mid=len(farr)//2
        if(len(farr)%2!=0):
            return farr[mid]
        sum=farr[mid]+farr[mid-1]
        return sum/2