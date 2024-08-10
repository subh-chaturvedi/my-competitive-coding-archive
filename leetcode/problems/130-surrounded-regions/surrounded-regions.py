class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        queue=[]
        
        for r in range(len(board)):
            for c in range(len(board[0])):
                if r==0 or r==len(board)-1 or c==0 or c==len(board[0])-1:
                    if board[r][c]=="O":
                        board[r][c]="S"
                        queue.append((r,c))
        
        # print(board)
        # print(queue)

        directions = [(1,0),(-1,0),(0,1),(0,-1)]

        def dfs(r,c,root):
            # print("DFS called",r,c)

            if r<0 or c<0 or r>= len(board) or c>= len(board[0]):
                return

            if board[r][c] == "X" or board[r][c]=="S":
                if not root:
                    return

            board[r][c] = "S"

            for rr, cc in directions:
                # print("calling further",rr,cc)
                dfs(r+rr,c+cc,False)

            return
        

        for r,c in queue:
            dfs(r,c,True)
        
        print(board)
        for r in range(len(board)):
            for c in range(len(board[0])):

                if board[r][c] == "O":
                    board[r][c] = "X"
                elif board[r][c] == "S":
                    board[r][c] = "O"
        
        


