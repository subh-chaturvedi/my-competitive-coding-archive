class Solution:
    def convert(self, s: str, numRows: int) -> str:
        n=numRows
        count = 0
        count2= n-2
        bigap=[]
        smallap=[]
        finstring= ""

        if n == 1 or len(s)<=n:
            return s
        if n == 2:
            str1 = ""
            str2 = ""
            for i in s:
                if count == 0:
                    str1 += i
                    count += 1
                else:
                    str2 += i
                    count = 0
            return str1+str2

        for i in range(0,len(s)):
            if count < n:
                smallap.append(s[i])
                count +=1
            else:
                
                if count2 == n-2:
                    bigap.append(smallap)
                    if i == len(s)-1:
                        smallap=[]
                if count2 > 0:
                    x = ["_"]*n
                    x[count2] = s[i]
                    bigap.append(x.copy())
                    count2 = count2-1
                    if i == len(s)-1:
                        smallap=[]
                else:
                    count = 1
                    smallap=[s[i]]
                    count2=n-2

        if count>=1:
        

            bigap.append(smallap)


        for i in range(0,n):
            for j in bigap:
                try:
                    if j[i] != "_":
                        finstring += j[i]
                except:
                    break

        return finstring