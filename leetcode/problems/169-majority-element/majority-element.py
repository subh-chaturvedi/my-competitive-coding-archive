class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        a=0
        b=0

        while True:
            if b==b==len(nums)-1 or len(nums)==1:
                break
            if nums[b]==nums[a]:
                b+=1
                continue
            nums.pop(a)
            nums.pop(b-1)
            b=b-1

        return nums[0]