class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans=[]

        def picker(curr):
            # print(curr)
            if sum(curr)>=target:
                if sum(curr)==target:
                    curr.sort()
                    if curr not in ans:
                        ans.append(curr)
                return
            
            for i in candidates:
                #get pickd
                picker(curr+[i])
            
            return

        picker([])

        return ans
            
