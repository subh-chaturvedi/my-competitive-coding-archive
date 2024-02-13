class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        freq={}
        maxfreq=1
        maxcount=1

        for i in tasks:
            if i in freq:
                freq[i]+=1
                if freq[i]==maxfreq:
                    maxcount+=1
                elif freq[i]>maxfreq:
                    maxcount=1
                    maxfreq=freq[i]
            else:
                freq[i]=1
        # print(freq,maxfreq,maxcount)
        
        ans = ((n+1)*(maxfreq-1))+(maxcount)

        return max(ans,len(tasks))

