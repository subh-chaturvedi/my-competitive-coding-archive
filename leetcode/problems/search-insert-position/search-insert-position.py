class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        x = nums.count(target)
        if x == 0:
            nums.append(target)
            nums.sort()
        y= nums.index(target)
        return y
