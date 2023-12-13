class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()

        x = nums[int(len(nums)/2)]

        return x