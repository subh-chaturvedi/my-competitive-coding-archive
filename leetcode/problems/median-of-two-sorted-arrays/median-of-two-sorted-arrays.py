
def medianfinder(l):
    if len(l) % 2 == 0:
        median = (l[(len(l)//2)-1]+l[(len(l)//2)])/2
    else:
        median = (l[(len(l)-1)//2])

    return median

class Solution:
    
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        x = nums1 + nums2
        x.sort()

        return medianfinder(x)