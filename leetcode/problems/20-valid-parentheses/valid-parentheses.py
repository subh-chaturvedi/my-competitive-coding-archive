class Solution:
    def isValid(self, s: str) -> bool:

        stck=["x"]

        for i in range(len(s)):
            if s[i] in ["[","(","{"]:
                stck.append(s[i])
            elif s[i] == "]" and stck[-1]=="[":
                stck.pop()
            elif s[i] == "}" and stck[-1]=="{":
                stck.pop()
            elif s[i] == ")" and stck[-1]=="(":
                stck.pop()
            else:
                return False
        
        return stck==["x"]