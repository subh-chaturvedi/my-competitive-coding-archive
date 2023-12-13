class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        nums.sort()

        maxc= int(len(nums)/3)
        c=1
        ans=[]

        if len(nums)==1:
            return nums
        if len(nums)==2:
            if nums[0]==nums[1]:
                return [nums[1]]
            else:
                return nums

        for i in range(1,len(nums)):
            print(maxc,i,nums[i],c)
            if nums[i]==nums[i-1]:
                c+=1
                if c>maxc:
                    ans.append(nums[i])
                    c=-len(nums)
            else:
                c=1

        return ans
