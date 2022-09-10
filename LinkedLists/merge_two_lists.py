# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head1=list1
        head2=list2
        flist1=[]
        flist2=[]
        while(head1):
            flist1.append(head1.val)
            head1=head1.next
        while(head2):
            flist2.append(head2.val)
            head2=head2.next
        flist=flist1+flist2
        flist.sort()
        if(flist):
            head=ListNode()
            fhead=head
            i=0
            head.val=flist[0]
            while(i+1<len(flist)):
                head.next=ListNode()
                head=head.next
                i+=1
                head.val=flist[i]
            return fhead
        else:
            return 