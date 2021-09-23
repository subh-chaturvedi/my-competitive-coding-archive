class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        
        newstr=s.strip()
        
        if newstr.find(" ")==-1:
            return len(newstr)
        else:
            newerstr=newstr[::-1]
            
            return newerstr.find(" ")
        
