class Solution:
    def canWinNim(self, n: int) -> bool:
        
        # rem = n%6

        # if rem<=3 and rem>0:
        #     return True
        # else:
        #     return False

        if n%4==0:
            return False
        else:
            return True