import heapq

class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:
        
        qualitySum = 0

        maxQ = []
        heapq.heapify(maxQ)

        maxRate=0

        ratioList = []
        ans=2**32

        for i in range(len(quality)):
            ratioList.append([wage[i]/quality[i],quality[i]])
        
        ratioList.sort()
        print(ratioList)

        for ratio, q in ratioList:
            # print(maxQ,q)
            if len(maxQ)<k:
                heapq.heappush(maxQ,-q)
                maxRate = max(maxRate,ratio)
                qualitySum+=q
                if len(maxQ)==k:
                    t = qualitySum*maxRate
                    # print(t,qualitySum,maxRate)
                    ans=min(ans,t)
            elif -q>(maxQ[0]):
                qualitySum+=heapq.heappop(maxQ)
                heapq.heappush(maxQ,-q)
                qualitySum+=q
                maxRate = max(maxRate,ratio)
                t = qualitySum*maxRate
                # print(t,qualitySum,maxRate)
                ans=min(ans,t)
        
        return ans
                
            



