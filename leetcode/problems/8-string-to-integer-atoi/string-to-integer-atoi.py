class Solution:
    def myAtoi(self, s: str) -> int:
        
        x=""

        if s == "":
            return 0

        firstnonspace=0
        digitencountered=0
        sign=1
        signenc=0


        for i in s:
            if i == " ":
                if firstnonspace == 0:
                    continue
                else:
                    break
            if i.isdigit()==False:
                if i in ["-","+"] and digitencountered==0 and signenc==0:
                    firstnonspace=1
                    sign *= int(i+"1")
                    signenc=1
                else:
                    break
            else:
                x+=i
                firstnonspace=1
                digitencountered=1
            
        if x == "":
            return 0
        
        value=int(x)

        value = sign * value
        value = min(value, 2 ** 31 - 1)
        value = max(-(2 ** 31), value)

        return value