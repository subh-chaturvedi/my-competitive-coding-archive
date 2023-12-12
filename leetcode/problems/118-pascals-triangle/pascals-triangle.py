class Solution:
    def nextPascal(self, step):
        if step==[1]:
            return [1,1]
        newpascal = []
        for i in range(len(step)-1):
            newpascal.append(step[i]+step[i+1])
        newpascal = [1] + newpascal + [1]
        return newpascal
    def generate(self, numRows: int) -> List[List[int]]:
        pascal=[[1]]
        for i in range(numRows-1):
            pascal.append(self.nextPascal(pascal[-1]))
        
        return pascal