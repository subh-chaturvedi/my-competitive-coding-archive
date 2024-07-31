class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        
        stck = ['0']
        ans=0

        for i in s:
            # print(stck,i)
            # if not stck:
            #     stck.append(i)
            #     continue

            if stck[-1]=="0":
                
                stck.append(i)
            else:
                
                if i=="1":
                    stck.append(i)
                else:
                    stck.pop()
                    ans+=1
        
        return ans