class Solution:
    def majorityElement(self, nums):
        nums.sort()
        result = []
        count = 1
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                count += 1
            else:
                if count > len(nums) // 3:
                    result.append(nums[i - 1])
                count = 1
        if count > len(nums) // 3:
            result.append(nums[-1])
        return result