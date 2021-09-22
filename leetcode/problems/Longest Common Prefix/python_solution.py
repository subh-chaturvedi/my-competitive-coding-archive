class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        pref=""
        shortlen=len(min(strs, key=len))

        for i in range(0,shortlen):
            matchall=0
            oldmatch=strs[0][i]

            for j in strs:
                if j[i]==oldmatch:
                    matchall=matchall+1
            if matchall==len(strs):
                pref=pref+oldmatch
            else:
                break                
        return pref
