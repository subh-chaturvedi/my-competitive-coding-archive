class Solution:
    def scoreOfString(self, s: str) -> int:
        prev=0
        curr=0
        ans=-ord(s[:1])
        
        for i in s:
            # print(i,curr,prev,ans)
            curr = ord(i)
            ans+= abs(curr-prev)

            prev= curr
        
        return ans