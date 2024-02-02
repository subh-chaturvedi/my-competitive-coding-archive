class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        MOD = 10 ** 9 + 7
        ans=0

        stack=[]

        for i, n in enumerate(arr):
            while stack and stack[-1][1]>n:
                j,m = stack.pop()
                if stack:
                    left=j-stack[-1][0] 
                else:
                    left=j+1
                right = i-j

                ans = (ans+(right*left*m)) % MOD
            stack.append([i,n])
        
        for i in range(len(stack)):
            j,m = stack[i]
            if i>0:
                left=j-stack[i- 1][0] 
            else:
                left=j+1
            right = len(arr)-j

            ans = (ans+(right*left*m)) % MOD


        return ans

