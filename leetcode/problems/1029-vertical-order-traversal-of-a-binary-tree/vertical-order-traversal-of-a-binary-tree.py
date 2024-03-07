# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        coords={(0,0):[root.val]}
        ans=[]
        self.minw=0
        self.maxw=0

        def dfs(root,origin):
            if not root:
                return
            
            if root.left:
                if origin[1]==self.minw:
                    self.minw-=1
                if (origin[0]+1,origin[1]-1) in coords:
                    coords[(origin[0]+1,origin[1]-1)].append(root.left.val)
                    coords[(origin[0]+1,origin[1]-1)].sort()
                else: coords[(origin[0]+1,origin[1]-1)]=[root.left.val]
                
            
            if root.right:
                if origin[1]==self.maxw:
                    self.maxw+=1
                if (origin[0]+1,origin[1]+1) in coords:
                    coords[(origin[0]+1,origin[1]+1)].append(root.right.val)
                    coords[(origin[0]+1,origin[1]+1)].sort()
                else: coords[(origin[0]+1,origin[1]+1)]=[root.right.val]
            
            dfs(root.left,[origin[0]+1,origin[1]-1])
            dfs(root.right,[origin[0]+1,origin[1]+1])
            
            return
        
        dfs(root,[0,0])
        print(coords)
        # coords.sort()
        
        for i in range(self.minw,self.maxw+1):
            temp=[]
            for key in sorted(coords.items()):
                print(key)
                if key[0][1]==i:
                    temp+=coords[key[0]]
                    # coords.pop(key)
                    
            ans.append(temp)


        return ans