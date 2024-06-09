class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        freq, prefix_sum, total = {0:1}, 0, 0

        for num in nums:
            prefix_sum += num
            total += freq.get(prefix_sum-k, 0)
            freq[prefix_sum] = freq.get(prefix_sum, 0) + 1

        return total