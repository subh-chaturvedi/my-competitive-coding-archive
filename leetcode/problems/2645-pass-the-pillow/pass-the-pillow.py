class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        
        # print(time%(n-1),time%(2*(n-1)))

        t1 = time%(n-1)
        t2 = time%(2*(n-1))

        if t1 == t2:
            return 1+t1
        else:
            return n-(t1)