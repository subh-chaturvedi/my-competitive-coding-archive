class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        ans=[]
        def f(curr):
            if len(curr)==k:
                if sum(curr)==n:
                    curr.sort()
                    if curr not in ans:
                        ans.append(curr)
                return
            if sum(curr)>=n:
                return
            
            for i in range(1,10):
                if sum(curr)+i<=n and i not in curr:
                    f(curr+[i])
                
        f([])

        return ans