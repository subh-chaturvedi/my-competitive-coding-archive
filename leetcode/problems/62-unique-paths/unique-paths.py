class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        def f(start,dp):
            # print(start)
            if start == end:
                return 1
            elif start[0]>=m or start[1]>=n:
                return 0
            # print(dp)
            if dp[start[0]][start[1]] == -1:
                dp[start[0]][start[1]] = f([start[0]+1,start[1]],dp) + f([start[0],start[1]+1],dp)
            
            # print([start[0]],[start[1]])
            return dp[start[0]][start[1]]
        
        dp = [[-1]*n for i in range(m)]
        # print(dp)
        end = [m-1,n-1]
        return f([0,0],dp)
        