class Solution:
    def jump(self, nums: List[int]) -> int:

        ans=0

        if len(nums)<2: #Edge case where the array is of length 1 or 0
            return ans

        end=0 
        maxend=0
        i=0

        while True: #Constraint is that every test case is valid for the jump game so this loop has to eventually end by return
            while i<=end:
                if nums[i]+i > maxend:
                    maxend=nums[i]+i
                if maxend >= len(nums)-1:
                    return ans+1
                i+=1
                # if i>=len(nums):
                #     break
            if end < maxend:
                end=maxend
                ans+=1
            # else:
            #     break
        return ans