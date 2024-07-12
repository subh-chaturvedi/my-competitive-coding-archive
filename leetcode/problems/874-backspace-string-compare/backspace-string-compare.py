class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        
        text1 =""

        for i in s:
            if i =="#":
                text1 = text1[:-1]
            else:
                text1+=i
        
        text2 =""

        for i in t:
            if i =="#":
                text2 = text2[:-1]
            else:
                text2+=i

        return text1==text2
        