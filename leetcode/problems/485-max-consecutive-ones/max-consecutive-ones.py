class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count=0
        maxcount=0
        for i in nums:
            if i!=1:
                count=0
            else:
                count+=1
                if count > maxcount:
                    maxcount = count
        

        return maxcount