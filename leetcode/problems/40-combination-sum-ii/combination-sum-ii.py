class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        def backtrack(nums,targetLeft,path):
            
            if targetLeft==0:
                res.append(path)
                return
            
            for i in range(len(nums)):
                if i>0 and nums[i]==nums[i-1]:
                    continue
                if nums[i]>targetLeft:
                    break
                backtrack(nums[i+1:],targetLeft-nums[i],path+[nums[i]])    
            
        res=[]
        backtrack(sorted(candidates),target,[])
        return res