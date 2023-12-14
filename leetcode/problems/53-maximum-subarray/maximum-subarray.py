class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sumd=0
        maxsum=nums[0]

        for i in nums:
            sumd += i
            maxsum = max(maxsum,sumd)

            if sumd<0:
                sumd=0
        
        return maxsum
            
