<<<<<<< HEAD
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if(root==None):
            return True
        return (abs(self.nodeh(root.left)-self.nodeh(root.right))<2) and self.isBalanced(root.left) and self.isBalanced(root.right)
    
    def nodeh(self,node):
        if(node==None):
            return 0
=======
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if(root==None):
            return True
        return (abs(self.nodeh(root.left)-self.nodeh(root.right))<2) and self.isBalanced(root.left) and self.isBalanced(root.right)
    
    def nodeh(self,node):
        if(node==None):
            return 0
>>>>>>> 92f383971117e059d72d5cacaaf0574cf94c15f8
        return 1+max(self.nodeh(node.left),self.nodeh(node.right))