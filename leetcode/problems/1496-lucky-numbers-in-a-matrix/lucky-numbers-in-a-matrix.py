class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        
        ans = []

        mins = [99999]*len(matrix)
        maxs = [-1]*len(matrix[0])

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                mins[i] = min(mins[i],matrix[i][j])
                maxs[j] = max(maxs[j],matrix[i][j])
        
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):

                if matrix[i][j]==mins[i] and matrix[i][j]==maxs[j]:
                    ans.append(matrix[i][j])
        
        return ans