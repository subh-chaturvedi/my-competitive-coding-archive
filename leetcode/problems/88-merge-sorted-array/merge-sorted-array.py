class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        
        if nums2 == []:
            return

        index1=0
        index2=0

        k=0

        x=len(nums1)

        nums1[:] = nums1[:-len(nums2)]

        while k<x:
            print(k,index1,index2,nums1,nums2)
            if k==len(nums1):
                nums1[:]=nums1+nums2[index2:]
                break    
            if nums1[index1] <= nums2[index2]:
                k+=1
                index1+=1
            else:
                nums1.insert(k,nums2[index2])
                k+=1
                index1+=1
                index2+=1
                if index2==len(nums2):
                    return
