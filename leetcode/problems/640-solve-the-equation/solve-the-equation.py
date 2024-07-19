class Solution:
    def solveEquation(self, eq: str) -> str:
        
        hs = eq.split("=")


        def validate(s):
            s.strip()

            if s[0] not in ["+","-"]:
                s = "+" + s
            
            newS = ""

            while s.find("+x") != -1 or s.find("-x")!=-1:
                s = s.replace("+x","+1x")
                s = s.replace("-x","-1x")
            

            s+="+"

            return s


        def stacker(s):

            s = validate(s)

            const=0
            var = 0

            stck = []

            isVar=0

            for i in s:

                s = validate(s)

                if i in ["+","-"]:
                    if isVar:
                        isVar = 0

                        coeff = ""
                        toAdd = ""
                        if len(stck)>0:
                            while toAdd not in ["+","-"]:
                                coeff = toAdd + coeff
                                toAdd = stck.pop()
                            op = toAdd

                            if op == "-":
                                var-= int(coeff)
                            else:
                                var+= int(coeff)
                    else:
                        coeff = ""
                        toAdd = ""
                        if len(stck)>0:
                            while toAdd not in ["+","-"]:
                                coeff = toAdd + coeff
                                toAdd = stck.pop()
                            op = toAdd

                            if op == "-":
                                const-= int(coeff)
                            else:
                                const+= int(coeff)

                    stck.append(i)

                elif i == "x":
                    isVar = 1
                else:
                    stck.append(i)
            
            return [const,var]


        lhs = stacker(hs[0])
        rhs = stacker(hs[1])

        var = lhs[1]-rhs[1]
        const = rhs[0]-lhs[0]

        if const == 0 and var==0:
            return "Infinite solutions"
        if const==0:
            return "x=0"
        if var==0:
            return "No solution"
        return "x=" + str(const//var)

