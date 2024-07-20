class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        
        ans = [([0]*len(colSum)) for i in range(len(rowSum))]

        for i in range(len(rowSum)):
            for j in range(len(colSum)):
                ans[i][j] = min(rowSum[i],colSum[j])

                rowSum[i]-=ans[i][j]
                colSum[j]-=ans[i][j]

        return ans
                