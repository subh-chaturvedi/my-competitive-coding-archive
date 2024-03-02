# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.maxDia = root.val
        
        def post(root):
            if root is None:
                return 0
            
            lh = post(root.left)
            rh = post(root.right)

            dia = lh+rh+root.val
            self.maxDia = max(dia,self.maxDia)

            return max((max(lh,rh)+root.val),0)
        
        post(root)
        return self.maxDia
