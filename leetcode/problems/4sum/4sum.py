class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        qlets = set()
        for o in range(0,len(nums)-3):
            for i in range(o+1,len(nums)-2):
                j=i+1
                k=len(nums)-1

                while j<k:
                    x=nums[o]+nums[i]+nums[j]+nums[k]

                    if x == target:
                        qlets.add((nums[o],nums[i],nums[j],nums[k]))
                        j=j+1
                        k=k-1
                    elif x<target:
                        j=j+1
                    elif x>target:
                        k=k-1
            
        return qlets
                