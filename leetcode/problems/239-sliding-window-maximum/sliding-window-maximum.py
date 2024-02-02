class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        left=0

        ans=[]

        curmax=[] # (index,value)

        for i in range(k):
            while curmax and nums[i]>curmax[-1][1]:
                curmax.pop()
            curmax.append([i,nums[i]])
        
        ans.append(curmax[0][1])

        for i in range(k,len(nums)):
            left+=1
            while curmax and nums[i]>curmax[-1][1]:
                curmax.pop()
            curmax.append([i,nums[i]])

            while curmax[0][0]<left:
                curmax.pop(0)

            ans.append(curmax[0][1])
        
        return ans
            
