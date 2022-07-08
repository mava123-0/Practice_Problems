# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        sum=0
        return self.sumleaf(root,sum)
        
    def sumleaf(self,root,sum):
        if(root):
            if(root.left):
                if(self.isExternal(root.left)):
                    sum=sum+root.left.val
            sum=self.sumleaf(root.left,sum)
            print(sum)
            sum=self.sumleaf(root.right,sum)
            return sum
        return sum
                
    def isExternal(self,node):
        if(node.left==None and node.right==None):
            return True
        return False
                