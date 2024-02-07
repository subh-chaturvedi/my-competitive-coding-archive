class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans=[]
        
        def picker(curr,rem):
            if rem==[]:
                ans.append(curr)
                return

            #picked
            picker(curr+[rem[0]],rem[1:])

            #not picked
            picker(curr,rem[1:])

            return
        
        picker([],nums)

        
        for i in ans:
            i.sort()
        ans.sort()
        x=0
        while x<len(ans)-1:
            if ans[x+1]==ans[x]:
                ans.pop(x+1)
            else:
                x+=1

        return ans