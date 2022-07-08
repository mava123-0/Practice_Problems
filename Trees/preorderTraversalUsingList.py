# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        que=[]
        if(root!=None):
            que.append(root.val)
            que=que+self.preorderTraversal(root.left)
            que=que+self.preorderTraversal(root.right)
        return que
