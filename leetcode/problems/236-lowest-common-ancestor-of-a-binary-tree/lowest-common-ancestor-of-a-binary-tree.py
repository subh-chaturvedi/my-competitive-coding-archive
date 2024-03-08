# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.ans = None
        def dfs(root):
            if not root:
                return False
            
            l = dfs(root.left)
            r = dfs(root.right)
            print(l,r, root.val)
            if root == p or root == q:
                if l or r:
                    self.ans = root
                    return False
                else:
                    return True
            else:
                if l and r:
                    self.ans = root
                    return False
                if l or r:
                    return True
                return False
            
        dfs(root)

        return self.ans
            
