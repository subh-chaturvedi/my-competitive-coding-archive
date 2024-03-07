# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        q=deque()
        q.append(root)
        temp=deque()
        ans=[root.val]

        while q:
            while q:
                _ = q.popleft()
                print(_.val)
                if _.left:
                    temp.append(_.left)
                if _.right:
                    temp.append(_.right)
            
            if temp:
                ans.append(temp[-1].val)

            q=temp
            temp=deque()

        return ans