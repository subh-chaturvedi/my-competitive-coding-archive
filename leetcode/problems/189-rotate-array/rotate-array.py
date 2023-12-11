class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        if k>=len(nums):
            for i in range(k):
                nums[:] = nums[-1:]+nums[:-1]
        else:
            nums[:] = nums[-k:]+nums[:-k]
        