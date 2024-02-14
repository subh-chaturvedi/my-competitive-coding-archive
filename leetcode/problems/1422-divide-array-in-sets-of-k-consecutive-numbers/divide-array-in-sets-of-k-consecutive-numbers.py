class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        if len(nums) % k != 0:
            return False

        numsDict = {}


        for i in nums:
            if i in numsDict:
                numsDict[i]+=1
            else:
                numsDict[i]=1
        numsLeft = len(nums)

        while numsLeft>0:
            minI= min(numsDict.keys())
            for i in range(k):
                if minI+i not in numsDict:
                    return False
                else:
                    numsDict[minI+i]-=1
                    numsLeft-=1
                if numsDict[minI+i] == 0:
                    del numsDict[minI+i]
        return True
                