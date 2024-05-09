class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:

        ans = 0

        happiness.sort(reverse=True)

        for i in range(k):
            # print(i,happiness[i],ans)
            ans+=max(0,happiness[i]-i)
        
        return ans

        