# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#SOLUTION NUMBER 1
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        que=[]
        self.temp(root,que)
        return que
    
    def temp(self,root,que):
        if(root!=None):
            self.temp(root.left,que)
            self.temp(root.right,que)
            que.append(root.val)
#SOLUTION NUMBER 2
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        que=[]
        if(root!=None):
            que=self.postorderTraversal(root.left)
            que=que+self.postorderTraversal(root.right)
            que.append(root.val)
        return que
