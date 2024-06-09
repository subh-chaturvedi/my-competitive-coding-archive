class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:

        def f(x,y,dp):
            # print(x,y)
            if (y,x) == (len(grid[0])-1,len(grid)-1):
                return grid[-1][-1]
            
            if y>= len(grid[0]) or x>=len(grid):
                return 2**30

            if dp[x][y]==-1:
                dp[x][y] = min(grid[x][y] + f(x+1,y,dp),grid[x][y] + f(x,y+1,dp))

            return dp[x][y]
        
        dp = [[-1 for i in range(len(grid[0]))] for j in range(len(grid))]
        # print(dp)

        return f(0,0,dp)