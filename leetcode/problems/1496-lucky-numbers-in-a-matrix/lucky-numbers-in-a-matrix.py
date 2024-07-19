class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        
        ans = []

        mins = [99999]*len(matrix)
        maxs = [-1]*len(matrix[0])

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                x=matrix[i][j]
                mins[i] = min(mins[i],x)
                maxs[j] = max(maxs[j],x)
        
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                x=matrix[i][j]
                if x==mins[i] and x==maxs[j]:
                    ans.append(x)
        
        return ans