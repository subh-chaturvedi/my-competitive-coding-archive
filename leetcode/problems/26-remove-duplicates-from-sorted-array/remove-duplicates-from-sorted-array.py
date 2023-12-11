from collections import OrderedDict
class Solution(object):
    def removeDuplicates(self, nums):
        nums[:] =  OrderedDict.fromkeys(nums)
        return len(nums)