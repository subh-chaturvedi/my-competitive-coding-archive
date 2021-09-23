class Solution:
    def isPalindrome(self, s: str) -> bool:
        news=""
        
        valid=list(string.ascii_letters + string.digits)
        
        for i in s:
            if i in valid:
                news=news+i
        
        news=news.lower()
        if news==news[::-1]:
            return True
        else:
            return False
    
        
