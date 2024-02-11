class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        row=0
        col=len(matrix[0])-1

        candidate = matrix[row][col]

        while row<len(matrix) and col>=0:
            # print(candidate, row, col)
            if candidate<target:
                row+=1
                if row<len(matrix):
                    candidate = matrix[row][col]
            elif candidate>target:
                col-=1
                if col>=0:
                    candidate = matrix[row][col]
            else:
                return True
        
        return False
