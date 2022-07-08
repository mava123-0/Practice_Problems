<<<<<<< HEAD
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        q1=self.inorderF1(p)
        q2=self.inorderF2(q)
        print(q1)
        print(q2)
        if(q1==q2):
            return True
        return False
        
    def inorderF1(self,p):
        que=[]
        if(p!=None):
            que=self.inorderF1(p.left)
            que.append(p.val)
            que=que+self.inorderF1(p.right)
        que.append('null')
        return que
            
    def inorderF2(self,q):
        que=[]
        if(q!=None):
            que=self.inorderF1(q.left)
            que.append(q.val)
            que=que+self.inorderF1(q.right)
        que.append('null')
        return que
        
=======
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        q1=self.inorderF1(p)
        q2=self.inorderF2(q)
        print(q1)
        print(q2)
        if(q1==q2):
            return True
        return False
        
    def inorderF1(self,p):
        que=[]
        if(p!=None):
            que=self.inorderF1(p.left)
            que.append(p.val)
            que=que+self.inorderF1(p.right)
        que.append('null')
        return que
            
    def inorderF2(self,q):
        que=[]
        if(q!=None):
            que=self.inorderF1(q.left)
            que.append(q.val)
            que=que+self.inorderF1(q.right)
        que.append('null')
        return que
        
>>>>>>> 92f383971117e059d72d5cacaaf0574cf94c15f8
    