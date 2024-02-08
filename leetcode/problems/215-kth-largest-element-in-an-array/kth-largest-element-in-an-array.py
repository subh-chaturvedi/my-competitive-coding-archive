import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        pq= []
        n= len(nums)

        for i in nums:
            heapq.heappush(pq,-i)
        
        for i in range(k):
            ans = heapq.heappop(pq)
        
        return -ans