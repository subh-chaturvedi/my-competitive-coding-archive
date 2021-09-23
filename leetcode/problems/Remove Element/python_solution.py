class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k=0
        i=0
        
        while i<len(nums):
            
            if nums[i]==val:
                k=k+1

                for j in range(i, len(nums)-1):

                    nums[j]=nums[j+1]

                nums.pop()
            else:
                i=i+1
