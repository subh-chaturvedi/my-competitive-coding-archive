class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        
        newstr = ""
        count = 0

        if len(a)>len(b)*4:
            newstr = a*2
            if newstr.find(b) != -1:
                return 2

        while len(newstr)<=len(b)*2:
            count+=1
            newstr+=a
            if newstr.find(b) != -1:
                return count
        
        return -1