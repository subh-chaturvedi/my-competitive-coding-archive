class Solution:
    def countGoodNumbers(self, n: int) -> int:
        MOD = 10 ** 9 + 7

        if n==1:
            return 5
        if n==0:
            return 0

        if n%2==0:
            completeSets = n//2
            # ans = (20**completeSets)% MOD
            ans = pow(20,completeSets,MOD)
        else:
            completeSets = (n-1)//2
            # rem=1
            ans = pow(20,completeSets,MOD)*5

        return ans % MOD