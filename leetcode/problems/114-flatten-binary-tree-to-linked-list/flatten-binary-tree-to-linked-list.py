# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        if root is None:
            return None
        
        newRight = self.flatten(root.left)
        OldRight = self.flatten(root.right)

        if newRight:
            endOfLeft = newRight
            while endOfLeft.right:
                endOfLeft=endOfLeft.right
            endOfLeft.right = OldRight

            root.right = newRight
            root.left = None
        else:
            root.right = OldRight
            
        return root
        