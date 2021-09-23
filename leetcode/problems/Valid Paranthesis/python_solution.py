class Solution:
    def isValid(self, s: str) -> bool:
        
        
        open1=0
        open2=0
        open3=0
        
        opener=["(","[","{"]
        closer=[")","]","}"]
        
        activeopen=[]
        activeclose=[]
        
        if s[0] in closer:
            return False
        
        for i in range(0,len(s)):
            #print("$",s[i])
        
            if s[i] in opener:
                activeopen.append(s[i])
                #print("ACTIVE",activeopen)
                
            if activeopen==[] and s[i] in closer:
                return False
                
            if s[i] in closer:
                
                matcher=opener[closer.index(s[i])]
                
                
                print("shldmatch  ",activeopen[-1])
                if matcher==activeopen[-1]:
                    activeopen.pop(-1)
                    #print("YAY")
                else:
                    return False
        if activeopen==[]:
            return True
