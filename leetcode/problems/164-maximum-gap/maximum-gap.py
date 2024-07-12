class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        
        nums.sort()

        ans = 0

        for i in range(1,len(nums)):
            ans = max(ans,nums[i]-nums[i-1])

        
        return ans