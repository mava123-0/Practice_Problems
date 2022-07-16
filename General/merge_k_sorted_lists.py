# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if(not lists):
            return
        if(len(lists)==1):
            return lists[0]
        flist=[]
        n=len(lists)
        # print(lists)
        for i in range (n):
            temp=lists[i]
            while(temp):
                flist.append(temp.val)
                temp=temp.next
        flist.sort()
        if(len(flist)>0):
            newHead=fhead=ListNode()
            for i in range(len(flist)):
                newHead.val=flist[i]
                if(i+1<len(flist)):
                    newHead.next=ListNode()
                    newHead=newHead.next
            return fhead
        return
        