# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root):
        ls=[]
        self.helper(root,ls)
        return ls
    def helper(self,root,ls):
        if(root ==None):
            return
        self.helper(root.left,ls)
        ls.append(root.val)
        self.helper(root.right,ls)