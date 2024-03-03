# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        ans=[]
        tempAns=[]
        q = deque()
        q.append(root)
        temp = deque()
        leftToRight = True

        while q and root:
            while q:
                curr = q.popleft()
                if curr.left: temp.append(curr.left)
                if curr.right: temp.append(curr.right)
                tempAns.append(curr.val)

            if leftToRight:
                ans.append(tempAns)
            else:
                ans.append(tempAns[::-1])

            tempAns=[]
            leftToRight = not leftToRight

            q=temp
            temp=deque()

        return ans
            


