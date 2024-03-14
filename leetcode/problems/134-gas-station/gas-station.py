class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        
        fill=0
        ans=-1
        start=0
        circ=0
        trav=0
        i=0

        # 3,1,1
        # 1,2,2

        while start<len(gas):
            if i>=len(gas):
                i=0

            print(i,start,fill)

            if i ==start and trav:
                return start
        
            trav=1
            fill+=gas[i]
            fill-=cost[i]
            print("*",gas[i],cost[i])
            i+=1

            if fill<0:
                if i <= start:
                    break
                fill=0
                start=i
                trav=0

        return ans