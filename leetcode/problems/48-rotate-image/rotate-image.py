class Solution:
    def transpose(self,matrix):
        cols= len(matrix[0])
        rows = len(matrix)

        for i in range(rows-1):
            for j in range(i+1,cols):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        return matrix

    def reverse(self,matrix):
        for i in range(len(matrix)):
            start=0
            end=-1

            for j in range(len(matrix[0])//2):
                matrix[i][start], matrix[i][end] = matrix[i][end], matrix[i][start]
                start+=1
                end-=1
        
        return matrix

    def rotate(self, matrix: List[List[int]]) -> None:
        
        matrix = self.transpose(matrix)
        matrix = self.reverse(matrix)