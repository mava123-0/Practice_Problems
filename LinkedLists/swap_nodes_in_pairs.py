# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        even_pos=[]
        odd_pos=[]
        temp=head
        i=0
        while(temp):
            if(i%2==0):
                even_pos.append(temp.val)
            else:
                odd_pos.append(temp.val)
            i+=1
            temp=temp.next
        if(i>1):
            temp=head
            i=0
            j=0
            k=0
            odd_len=len(odd_pos)
            even_len=len(even_pos)
            while(temp):
                if(i%2==0 and odd_len>0):
                    temp.val=odd_pos[j]
                    j+=1
                    odd_len-=1
                else:
                    temp.val=even_pos[k]
                    k+=1
                    even_len-=1
                i+=1
                temp=temp.next
            return head
        else:
            return head