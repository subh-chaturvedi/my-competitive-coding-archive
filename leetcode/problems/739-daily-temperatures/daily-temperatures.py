class Solution:
    def dailyTemperatures(self, temp: List[int]) -> List[int]:
        ans = [0]*len(temp)
        stack=[]

        for i in range(len(temp)):
            if not stack:
                stack.append([i,temp[i]])
            while stack and stack[-1][1]<temp[i]:
                popd=stack.pop()
                ans[popd[0]]=i-popd[0]
            stack.append([i,temp[i]])
        
        return ans