class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        prefSumsD = {0:1}

        prefsum = 0

        ans=0

        for i in nums:
            prefsum+=i

            if (prefsum-k) in prefSumsD:
                ans+=prefSumsD[prefsum-k]
            
            if prefsum in prefSumsD:
                prefSumsD[prefsum]+=1
            else:
                prefSumsD[prefsum]=1
            
        
        return ans