class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()

        start=0

        while start != len(intervals)-1:
            if intervals[start][-1]>=intervals[start+1][0]:
                intervals[start]=[intervals[start][0],max(intervals[start][-1],intervals[start+1][-1])]
                intervals.pop(start+1)
            else:
                start+=1
        
        return intervals