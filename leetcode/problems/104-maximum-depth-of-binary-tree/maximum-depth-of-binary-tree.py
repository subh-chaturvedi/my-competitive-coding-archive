# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        maxheight=[0]

        def depth(root,currDepth):
            if not root.left and not root.right:
                if currDepth>maxheight[0]:
                    maxheight.pop()
                    maxheight.append(currDepth)
            if root.left:
                depth(root.left,currDepth+1)
            if root.right:
                depth(root.right,currDepth+1)
        
        depth(root,1)
        return maxheight[0]
        