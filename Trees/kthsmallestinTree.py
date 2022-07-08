# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        que=[]
        def kthSmalles(root,k,que):
            if(root!=None):
                kthSmalles(root.left,k,que)
                que.append(root.val)
                kthSmalles(root.right,k,que)
            return que
        print(que)
        kthSmalles(root,k,que)
        return que[k-1]