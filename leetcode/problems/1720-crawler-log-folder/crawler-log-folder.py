class Solution:
    def minOperations(self, logs: List[str]) -> int:
        
        pt=0

        for i in logs:
            if i == "../":
                if pt>0:
                    pt-=1
            elif i == "./":
                continue
            else:
                pt+=1
        
        return pt