class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1 = [int(i) for i in version1.split(".")]
        v2 = [int(i) for i in version2.split(".")]

        if len(v1)>len(v2):
            v2+=[0]*(len(v1)-len(v2))
        if len(v2)>len(v1):
            v1+=[0]*(len(v2)-len(v1))
        
        ans=0

        for i in range(len(v1)):
            if v1[i]>v2[i]:
                ans=1
                break
            if v1[i]<v2[i]:
                ans=-1
                break
        
        return ans
