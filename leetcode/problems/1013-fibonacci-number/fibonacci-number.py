def calcfib(x,a,b):
        if x == 0:
            return a+b
        return calcfib(x-1,b,a+b)

class Solution:
    def fib(self, n: int) -> int:
        if n==0:
            return 0
        if n==1:
            return 1
        return calcfib(n-2,0,1)