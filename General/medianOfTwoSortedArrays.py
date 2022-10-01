class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        list_num  =nums1+nums2
        list_num.sort()
        print(list_num)
        if(len(list_num)%2!=0):
            return list_num[int(len(list_num)/2)]
        else:
            return (list_num[int(len(list_num)/2)]+list_num[int(len(list_num)/2-1)])/2