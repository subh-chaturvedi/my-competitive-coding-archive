class Solution:
    def splitString(self, s: str) -> bool:
        
        def f(i, parts, prev):
            
            if i == len(s):

                return parts>=2
            
            for j in range(i,len(s)):

                if prev=="x" or int(s[i:j+1]) == prev-1:

                    if f(j+1,parts+1,int(s[i:j+1])):
                        return True
                
            
            return False
        
        return f(0,0,"x")
        
