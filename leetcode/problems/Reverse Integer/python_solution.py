class Solution:
    def reverse(self, x: int):
        
        z=str(x)
        f=''
        neg=0
        
        if int(z)>=((2**31)-1) or int(z)<=((-2**31)+1):
            return 0
        else:
            if z[0]=='-':
                neg=1
                z=z[1:]

            for i in range(len(z)-1,-1,-1):
                m=z[i]
                print(m)
                f=f+m
                print(f)
                
            if neg==1:
                f='-'+f
                
            if int(f)>=((2**31)-1) or int(f)<=((-2**31)+1):
                return 0
            else:
                return int(f) 
