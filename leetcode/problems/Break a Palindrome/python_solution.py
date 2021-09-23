class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        length=len(palindrome)
        pal_list=list(palindrome)
        
        if length==1:
            return ""
          
        for i in range(length):
            if pal_list[i]!='a':
                if i!=length//2:
                    pal_list[i]='a'
                    return ''.join(pal_list)
            elif i==length-1:
                if pal_list[i]=='a':
                    pal_list[i]='b'
                else:
                    pal_list[i]='a'
                    
        return ''.join(pal_list)
