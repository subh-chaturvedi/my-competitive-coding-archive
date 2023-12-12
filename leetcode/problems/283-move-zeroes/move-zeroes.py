class Solution:
    def moveZeroes(self, nums: List[int]) -> None:

        i=0
        count=0
        
        while i!= len(nums):
            if nums[i]==0:
                count +=1
                nums.pop(i)
            else:
                i +=1
        
        nums+=[0]*count

        return nums