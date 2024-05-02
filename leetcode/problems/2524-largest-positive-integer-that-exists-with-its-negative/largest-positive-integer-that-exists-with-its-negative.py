class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        pairs = {}

        for i in nums:
            if i not in pairs:
                if -i not in pairs:
                    pairs[i]=0
                else:
                    pairs[i]=1
        
        ans = -1

        for i in pairs.keys():
            if abs(i)>ans:
                if pairs[i] == 1:
                    ans = abs(i)

        return ans
