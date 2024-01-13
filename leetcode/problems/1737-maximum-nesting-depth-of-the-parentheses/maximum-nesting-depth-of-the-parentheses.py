class Solution:
    def maxDepth(self, s: str) -> int:
        
        x=0
        maxx=0

        for i in s:
            if i=="(":
                x+=1
            elif i ==")":
                x-=1
            maxx=max(x,maxx)
        
        return maxx