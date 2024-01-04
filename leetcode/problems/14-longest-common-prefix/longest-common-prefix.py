class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        ans=""
        disruption=0

        for j in range(len(strs[0])):
            for i in range(len(strs)):
                #print(i,j,strs[i])
                if len(strs[i])==j:
                    return ans
                if i==0:
                    tomatch=strs[i][j]
                elif strs[i][j]!=tomatch:
                    disruption=1
                    break
            if disruption==0:
                ans+=tomatch

        return ans