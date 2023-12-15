class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        pos = [p for p in nums if p > 0]
        neg = [n for n in nums if n < 0]
        ans = []
        for p, n in zip(pos, neg):
            ans += [p, n]
        return ans