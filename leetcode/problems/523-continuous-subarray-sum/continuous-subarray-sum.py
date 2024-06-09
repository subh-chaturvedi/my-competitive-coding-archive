class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        
        cache = {0:-1}
        remsum=0

        for i,num in enumerate(nums):
            # print(i)
            remsum = (remsum+num)%k

            if remsum in cache:
                if i-cache[remsum]>1:
                    return True
            else:
                cache[remsum]=i

        return False        

# 5 1 5
# 23 2 4 6
# 0 0 2 2
        
        