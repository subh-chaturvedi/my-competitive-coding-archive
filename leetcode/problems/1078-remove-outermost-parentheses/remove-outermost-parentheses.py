class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        ans=""
        valpenC=0
        maxval=0
        currval=""

        for i in range(len(s)):
            print(s[i],valpenC,currval)
            currval+=s[i]
            if s[i]=="(":
                valpenC+=1
                
            elif s[i]==")":
                valpenC-=1
                if valpenC==0:
                    ans+=currval[1:-1]
                    currval=""
                    
            
        return ans