class Solution:
    def repeatedStringMatch(self, A: str, B: str) -> int:
    	if set(B).issubset(set(A)) == False: return -1
    	for i in range(1,int(len(B)/len(A))+3):
    		if B in A*i: return i
    	return -1