class Solution:
    def binsearch(self,arr,k):
        
        s,e=0,len(arr)-1

        while s<=e:
            mid= (s+e)//2

            if arr[mid]==k:
                return mid
            elif arr[mid]<k:
                s=mid+1
            else:
                e=mid-1
        
        return -1

    def search(self, nums: List[int], target: int) -> int:

        if len(nums)==1:
            if nums[0]==target:
                return 0
            else:
                return -1
        
        for i in range(1,len(nums)):
            if nums[i]<nums[i-1]:
                if target>=nums[0]:
                    return self.binsearch(nums[:i],target)
                else:
                    pos = self.binsearch(nums[i:],target)
                    if pos==-1:
                        return pos
                    return i+pos
        
        return self.binsearch(nums,target)