# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        temp1=head
        temp2=head
        for i in range(n):
            temp2=temp2.next
        if(not temp2):
            return head.next
        while(temp2.next):
            temp2=temp2.next
            temp1=temp1.next
        temp1.next=temp1.next.next
        return head