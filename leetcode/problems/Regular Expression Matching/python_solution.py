class Solution:
  
    def isMatch(self, s: str, p: str) -> bool: 
        return self.backtrack(s, p)
      
    def backtrack(self, s, p):
        if not s and not p:
            return True
        
        if len(p) > 1 and p[1] == "*":
            i = 0 
            
            # don't match to anything
            if self.backtrack(s, p[2:]):
                return True
            
            # match
            while i < len(s) and (s[i] == p[0] or p[0] == "."):
                if self.backtrack(s[i + 1:], p[2:]):
                    return True
                i += 1
        elif not p or not s:
            return False
        elif s[0] == p[0] or p[0] == ".":
             if self.backtrack(s[1:], p[1:]):
                return True
        else:
            return False
