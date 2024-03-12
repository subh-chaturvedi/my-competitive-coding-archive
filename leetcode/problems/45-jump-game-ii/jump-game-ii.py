class Solution:
    def jump(self, nums: List[int]) -> int:

        ans=0

        if len(nums)<2:
            return ans

        start=0
        end=0
        maxend=0
        i=0

        while True:
            while i<=end:
                if nums[i]+i > maxend:
                    maxend=nums[i]+i
                if maxend >= len(nums)-1:
                    return ans+1
                i+=1
            if end < maxend:
                end=maxend
                ans+=1
        
        return ans