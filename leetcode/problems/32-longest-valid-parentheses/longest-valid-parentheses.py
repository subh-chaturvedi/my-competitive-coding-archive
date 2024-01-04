class Solution:
    def longestValidParentheses(self, s: str) -> int:
        
        stck=[-1]
        maxs=0

        for i in range(len(s)):
            if s[i]=="(":
                stck.append(i)
            else:
                stck.pop()
                if not stck:
                    stck.append(i)
                else:
                    maxs=max(maxs,i-stck[-1])
        
        return maxs