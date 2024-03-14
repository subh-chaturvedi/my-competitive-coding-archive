# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        
        def treeCons(inord,postord):
            if not inord:
                return None

            root = TreeNode(postord[-1])

            div = inord.index(postord[-1])

            lTree_inord = inord[:div]
            rTree_inord = inord[div+1:]

            postord.pop(-1)

            lTree_postord = postord[:len(lTree_inord)] 
            rTree_postord = postord[len(lTree_inord):]

            root.left = treeCons(lTree_inord,lTree_postord)
            root.right = treeCons(rTree_inord,rTree_postord)

            return root
        

        root = treeCons(inorder,postorder)

        return root