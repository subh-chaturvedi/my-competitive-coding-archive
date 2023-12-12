class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        x= len(nums)

        sumed = sum(nums)

        shouldbe= x*(x+1)/2

        y=shouldbe-sumed

        return int(y)