class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        
        ans=[]

        def f(selected, used):
            if len(selected) == len(nums):
                # print(selected,ans)
                if selected not in ans:
                    ans.append(selected[:])
                return
            

            for i in range(len(nums)):
                if used[i]:
                    continue
                
                used[i] =True
                selected.append(nums[i])

                f(selected,used)

                selected.pop()
                used[i]=False
        

        used = [0]*len(nums)
        f([],used)

        return ans
