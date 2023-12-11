class Solution:
    def check(self, nums: List[int]) -> bool:
        isSmallerCheck = 0

        for i in range(0,len(nums)):
            if i == len(nums)-1:
                if nums[i]>nums[0]:
                    isSmallerCheck += 1
                else:
                    continue
            elif nums[i]>nums[i+1]:
                isSmallerCheck += 1
            else:
                continue

        print(isSmallerCheck)

        if isSmallerCheck <= 1:
            return True
        else:
            return False