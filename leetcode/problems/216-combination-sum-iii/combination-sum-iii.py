class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        ans=[]
        def f(curr,s):
            if len(curr)==k:
                if s==n:
                    curr.sort()
                    if curr not in ans:
                        ans.append(curr)
                return
            if s>=n:
                return
            
            for i in range(1,10):
                if s+i<=n and i not in curr:
                    f(curr+[i],s+i)
                
        f([],0)

        return ans