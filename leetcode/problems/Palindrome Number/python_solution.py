class Solution:
    def isPalindrome(self, x: int) -> bool:
      
        stringx=str(x)
        reversestring=stringx[::-1]
        
        if stringx==reversestring:
            return True
        else:
            return False
