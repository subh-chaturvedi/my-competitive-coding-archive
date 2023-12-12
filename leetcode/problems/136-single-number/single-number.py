class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        nums.sort()
        for i in range(0,len(nums),2):
            if i==len(nums)-1:
                return nums[i]
            elif nums[i] == nums[i+1]:
                continue
            
            else:
                return nums[i]