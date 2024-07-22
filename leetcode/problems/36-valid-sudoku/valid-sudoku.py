class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #45

        rows = [[],[],[],[],[],[],[],[],[]]
        cols = [[],[],[],[],[],[],[],[],[]]
        boxs = [[],[],[],[],[],[],[],[],[]]

        mapping = {(0,0):0,(0,1):1,(0,2):2,(1,0):3,(1,1):4,(1,2):5,(2,0):6,(2,1):7,(2,2):8}

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == ".":
                    continue

                num = int(board[i][j])

                if num in rows[i]:
                    return False
                rows[i].append(num)
                # if rows[i]>45:
                #     return False
                
                if num in cols[j]:
                    return False
                cols[j].append(num)
                # if cols[j]>45:
                #     return False
                
                box_x = i//3
                box_y = j//3


                if num in boxs[mapping[(box_x,box_y)]]:
                    return False
                boxs[mapping[(box_x,box_y)]].append(num)
                
                # if boxs[mapping[(box_x,box_y)]] > 45:
                #     return False
        
        return True



