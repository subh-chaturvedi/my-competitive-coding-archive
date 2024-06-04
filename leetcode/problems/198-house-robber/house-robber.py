class Solution:
    def f(self, nums, i, dp):
        if i<0:
            return 0
        
        if dp[i]==-1:
            dp[i] = max(self.f(nums,i-1,dp),self.f(nums,i-2,dp) + nums[i])
        
        return dp[i]

    def rob(self, nums: List[int]) -> int:
        #2 1 1 2

        dp = [-1]*len(nums)

        return self.f(nums,len(nums)-1,dp)
