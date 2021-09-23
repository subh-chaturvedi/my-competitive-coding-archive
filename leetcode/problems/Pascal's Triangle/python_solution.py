class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        
        
        finalLine=[[1],[1,1]]
        
        def nextline(ogline):
            newline=[]
            for i in range(0,len(ogline)-1):
                newline.append(ogline[i]+ogline[i+1])
            newline=[1]+newline+[1]
            return newline
            
        if numRows==1:
            return [[1]]
        if numRows==2:
            return [[1],[1,1]]
        else:
            for i in range(3,numRows+1):
                finalLine.append(nextline(finalLine[-1]))
            return finalLine
