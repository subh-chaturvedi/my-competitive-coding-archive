# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        

        def treeCons(inord,preord):
            if not inord:
                return None

            root = TreeNode(preord[0])

            div = inord.index(preord[0])

            lTree_inord = inord[:div]
            rTree_inord = inord[div+1:]

            preord.pop(0)

            lTree_preord = preord[:len(lTree_inord)] 
            rTree_preord = preord[len(lTree_inord):]

            root.left = treeCons(lTree_inord,lTree_preord)
            root.right = treeCons(rTree_inord,rTree_preord)

            return root
        

        root = treeCons(inorder,preorder)

        return root