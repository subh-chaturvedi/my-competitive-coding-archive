class Solution:
    
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        for i in range(len(nums)):
            n=target-nums[i]
            rest_of_nums=nums[i+1:]
            
            if n in rest_of_nums:
                return[i,(rest_of_nums.index(n))+i+1]
