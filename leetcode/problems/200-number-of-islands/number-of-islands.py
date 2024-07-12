class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ans=0

        def dfs(x,y):
            # print(x,y)
            if x>=len(grid) or x<0 or y<0 or y>=len(grid[0]):
                # print("oob")
                return

            if grid[x][y]=="0":
                # print("zero")
                return
            
            else:
                # print("dfs")
                grid[x][y] = "0"

                dfs(x-1,y) #top
                dfs(x+1,y) #bottom
                dfs(x,y-1) #left
                dfs(x,y+1) #right
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    # print("started",i,j)
                    ans+=1
                    dfs(i,j)
        
        return ans