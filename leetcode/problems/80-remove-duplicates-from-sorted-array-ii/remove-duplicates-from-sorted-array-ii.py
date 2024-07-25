class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        i = 0
        count = 0

        while i<len(nums)-1:
            if nums[i]==nums[i+1]:
                if count==1:
                    nums.pop(i)
                else:
                    count=1
                    i+=1
            else:
                i+=1
                count=0
        
        # print(nums)