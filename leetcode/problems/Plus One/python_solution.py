class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
               
        strno = ''.join([str(elem) for elem in digits])
       
        newstr=str(int(strno)+1)
        
        digits=[]
        
        
        for i in newstr:
            digits.append(i)
        return digits
