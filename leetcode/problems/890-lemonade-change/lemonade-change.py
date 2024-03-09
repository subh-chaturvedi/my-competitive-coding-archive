class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        
        c1 = 0
        c2 = 0
        

        for i in bills:
            if i==5:
                c1+=1
            elif i==10:
                c2+=1
                c1-=1
            else:
                
                if c2>0:
                    c2-=1
                    c1-=1
                else:
                    c1-=3
            if c1<0 or c2<0:
                return False
        
        return True