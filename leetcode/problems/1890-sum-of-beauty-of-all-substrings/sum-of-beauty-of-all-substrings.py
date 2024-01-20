class Solution:
    def findBeauty(self, s):
        fq={}

        for i in s:
            if i in fq:
                fq[i]+=1
            else:
                fq[i]=1
        
        bty = max(fq.values())-min(fq.values())

        return bty

    def beautySum(self, s: str) -> int:
        count=0
        for i in range(len(s)):
            for j in range(i+1,len(s)):
                beut = self.findBeauty(s[i:j+1])
                count+=beut
                # print(s[i:j+1])

        return count