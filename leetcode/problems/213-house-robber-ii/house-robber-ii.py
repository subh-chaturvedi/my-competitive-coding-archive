class Solution:
    def f(self, nums, i, dp):
        print(i,nums)
        if i<0:
            return 0
        
        if dp[i]==-1:
            # print(self.f(nums,i-1,dp))
            # print(self.f(nums,i-2,dp) + nums[i])
            dp[i] = max(self.f(nums,i-1,dp),self.f(nums,i-2,dp) + nums[i])
        
        # print(dp[i])
        return dp[i]

    def rob(self, nums: List[int]) -> int:
        if len(nums)<3:
            return max(nums)        


        dp = [-1]*len(nums)
        m1 = self.f(nums[1:],len(nums)-2,dp)

        dp = [-1]*len(nums)
        m2 = self.f(nums[:-1],len(nums)-2,dp)

        return max(m1,m2)
