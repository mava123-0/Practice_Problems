# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def getInor(self,root,que):
        if(root!=None):
            self.getInor(root.left,que)
            que.append(root.val)
            self.getInor(root.right,que)
        return que
        
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if(root==None):
            return True
        que=[]
        self.getInor(root,que)
        print(que)
        n=len(que)
        if(len(que)==1):
            return True
        for i in range(len(que)):
            if(que[i]==que[i-1]):
                return False
        if(sorted(que)==que):
            return True
        return False
        