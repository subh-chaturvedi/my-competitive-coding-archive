class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans=[]
        
        def picker(curr,rem):
            if rem==[]:
                ans.append(curr)
                return
                
            # print(rem,curr)

            #picked
            picker(curr+[rem[0]],rem[1:])

            #not picked
            picker(curr,rem[1:])

            return
        
        picker([],nums)
        return ans