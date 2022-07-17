# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        temp1=l1
        temp2=l2
        stk1=[]
        stk2=[]
        while(temp1!=None):
            stk1.append(temp1.val)
            temp1=temp1.next
        while(temp2!=None):
            stk2.append(temp2.val)
            temp2=temp2.next
        num1=0
        while(stk1):
            num1=10*num1+stk1.pop()
        num2=0
        while(stk2):
            num2=10*num2+stk2.pop()
        sum=num1+num2
        print(sum)
        size=len(str(sum))
        stk3=[]
        while(size>0):
            stk3.append(sum%10)
            sum=int(sum//10)
            size-=1
        i=0
        head=n=ListNode(0)
        while(i<len(stk3)):
            n.next=ListNode(stk3[i])
            n=n.next
            i+=1
        return head.next
        