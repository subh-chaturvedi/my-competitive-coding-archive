class Solution:
    def justBig(self,x,llist):
        y=[]
        for i in llist:
            if i>x:
                y.append(i)
        
        return min(y)

    def nextPermutation(self, nums: List[int]) -> None:
        
        for i in range(len(nums)-1,0,-1):
            
            if nums[i]>nums[i-1]:
                x= self.justBig(nums[i-1],nums[i:])
                notnums=nums[i-1:]
                notnums.remove(x)
                notnums.sort()
                nums[:]=nums[:i-1]+[x]+notnums
                break
                
            if i==1:
                nums[:] = nums[::-1]
                break
        