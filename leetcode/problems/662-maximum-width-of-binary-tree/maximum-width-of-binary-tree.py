# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        tree={}

        def dfs(root,level,col):
            if root:
                # print(root.val)
                if level in tree:
                    tree[level].append(col)
                else:
                    tree[level]=[col]
                
                dfs(root.left,level+1,col*2)
                dfs(root.right,level+1,(col*2)+1)
        
        dfs(root,1,0)

        ans=0
        # print(tree)
        for i in tree:
            ans=max(ans,(max(tree[i])-min(tree[i]))+1)
        
        return ans