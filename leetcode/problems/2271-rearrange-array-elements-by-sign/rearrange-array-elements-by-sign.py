class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        i=0
        ic=0
        j=0
        jc=0
        x=[]

        while len(x)!=len(nums):
            #print(i,j,ic,jc)
            if i < len(nums):
                if nums[i] <0:
                    i+=1
            if i < len(nums):
                if nums[i] >0 and ic==jc:
                    x.append(nums[i])
                    i+=1
                    ic+=1
            if j < len(nums):
                if nums[j]>0:
                    j+=1
            if j < len(nums):    
                if nums[j] <0 and ic==jc+1:
                    x.append(nums[j])
                    j+=1
                    jc+=1

        return x
                
