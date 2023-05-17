class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        triplets = set()

        for i in range(len(nums)-2):
            j=i+1
            k=len(nums)-1

            while j<k:
                x=nums[i]+nums[j]+nums[k]

                if x == 0:
                    triplets.add((nums[i],nums[j],nums[k]))
                    j=j+1
                    k=k-1
                elif x<0:
                    j=j+1
                elif x>0:
                    k=k-1
        
        return triplets
                