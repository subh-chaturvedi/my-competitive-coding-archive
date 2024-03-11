class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums)<2:
            return True
        maxindex=0
        i=0

        while i <= maxindex:
            maxindex=max(maxindex,nums[i]+i)
            if maxindex>=len(nums)-1:
                return True
            i+=1
        
        return False
        