class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        
        # print(time%(n-1),time%(2*(n-1)))

        if time%(n-1) == time%(2*(n-1)):
            return 1+time%(n-1)
        else:
            return n-(time%(n-1))