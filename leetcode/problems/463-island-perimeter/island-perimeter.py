class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        
        ans=0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    # print(i,j)
                    if i+1>=len(grid) or grid[i+1][j] == 0:
                        ans+=1
                        # print("top")
                    if i-1<0 or grid[i-1][j] == 0:
                        ans+=1
                        # print("bottom")
                    if j+1>=len(grid[0]) or grid[i][j+1] == 0:
                        ans+=1
                        # print("right")
                    if j-1<0 or grid[i][j-1] == 0:
                        ans+=1
                        # print("left")
        
        return ans