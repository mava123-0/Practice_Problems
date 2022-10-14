# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp = head
        size=0
        while(temp!=None):
            size+=1;
            temp = temp.next
        if size==1:
            head = head.next
            return head
        if size%2==0:
            n = (size/2)
        else:
            n = (size/2)-1
        index = head
        while(n-1>0):
            n-=1
            index = index.next
        index.next = index.next.next
        return head