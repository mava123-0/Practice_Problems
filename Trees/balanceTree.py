# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    
    def balanceBST(self, root: TreeNode) -> TreeNode:
        
        def getInorder(root):
            if(root==None):
                return
            getInorder(root.left)
            que.append(root.val)
            getInorder(root.right)
            return que
        
        que=[]
        getInorder(root)
        
        def balF(que):
            if not que:
                return None
            mid=len(que)//2
            root=TreeNode(que[mid])
            root.left=balF(que[:mid])
            root.right=balF(que[mid+1:])
            return root
        
        return balF(que)