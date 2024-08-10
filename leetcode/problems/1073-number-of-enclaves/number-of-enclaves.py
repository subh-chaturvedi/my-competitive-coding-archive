class Solution:
    def numEnclaves(self, board: List[List[int]]) -> int:
        directions = [(1,0),(-1,0),(0,1),(0,-1)]

        def dfs(r,c):
            if r<0 or c<0 or r>= len(board) or c>= len(board[0]):
                return
            if board[r][c] == 0 or board[r][c]==2:
                return
            board[r][c] = 2
            for rr, cc in directions:
                dfs(r+rr,c+cc)
            return
        
        for r in range(len(board)):
            for c in range(len(board[0])):
                if r==0 or r==len(board)-1 or c==0 or c==len(board[0])-1:
                    if board[r][c]==1:
                        dfs(r,c)
        ans = 0
        for r in range(len(board)):
            for c in range(len(board[0])):

                if board[r][c] == 1:
                    ans+=1
        
        return ans