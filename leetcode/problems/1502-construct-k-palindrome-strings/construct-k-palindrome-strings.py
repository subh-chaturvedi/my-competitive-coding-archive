class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        if len(s)<k:
            return False
        elif len(s)==k:
            return True
        

        freq = {}

        for i in s:
            freq[i] = freq.get(i,0) + 1

        
        odds = 0

        for i in freq.keys():
            if freq[i] % 2 !=0:
                odds+=1
        
        if odds>k:
            return False
        
        return True