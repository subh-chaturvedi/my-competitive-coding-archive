class Solution:
    from collections import deque
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        rows = len(grid)

        if rows==0:
            return -1
        
        cols = len(grid[0])
        
        rotten = deque()

        fresh = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==2:
                    rotten.append([r,c])
                elif grid[r][c]==1:
                    fresh+=1
        
        mins =0

        while rotten and fresh>0:
            mins+=1

            for _ in range(len(rotten)):
                r,c = rotten.popleft()

                for dr, dc in [[0,1],[0,-1],[1,0],[-1,0]]:
                    rr = r+dr
                    cc = c+dc

                    if rr<0 or cc<0 or cc>=cols or rr>=rows:
                        continue
                    if grid[rr][cc] in [0,2]:
                        continue
                    
                    grid[rr][cc]=2
                    rotten.append([rr,cc])
                    fresh-=1

        if fresh==0:
            return mins
        
        return -1
