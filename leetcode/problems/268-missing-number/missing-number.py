class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        x= len(nums)

        sumed = sum(nums)

        shouldbe= x*(x+1)/2

        return int(shouldbe-sumed)