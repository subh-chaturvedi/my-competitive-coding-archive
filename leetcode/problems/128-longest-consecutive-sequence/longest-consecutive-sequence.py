class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        uniques = set(nums)
        max_length = 0

        while len(uniques) != 0:

            high=low=uniques.pop()

            while high+1 in uniques or low-1 in uniques:
                
                if high +1 in uniques:
                    uniques.remove(high+1)
                    high +=1

                if low -1 in uniques:
                    uniques.remove(low-1)
                    low -=1

            max_length = max(high - low + 1, max_length)

        return max_length


        
        