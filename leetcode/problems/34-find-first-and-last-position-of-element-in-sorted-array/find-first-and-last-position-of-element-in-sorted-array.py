class Solution:
    def searchFirst(self,nums,target):
        start,end=0,len(nums)-1
        while start<end:
            mid = (start+end)//2

            if nums[mid]<target:
                start=mid+1
            else:
                end=mid

        if nums[start] != target:
            return -1
        return start

    def searchLast(self,nums,target):
    
        index=-1

        start,end=0,len(nums)-1
        while start<=end:
            mid = (start+end)//2
            if nums[mid]==target:
                index=mid
                start=mid+1
            elif nums[mid]>target:
                end=mid-1
            else:
                start=mid+1
            
        return index

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        if nums==[]:
            return [-1,-1]

        index = [self.searchFirst(nums,target),self.searchLast(nums,target)]

        return index