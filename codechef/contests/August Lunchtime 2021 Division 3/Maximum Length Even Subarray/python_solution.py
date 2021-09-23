# cook your dish here

n=int(input(""))

zlist=[]
for i in range(0,n):
    z=int(input(""))
    zlist.append(z)
    
    
for i in zlist: 
    sumnum=i*(i+1)/2
    
    #print(listnum)
    if sumnum%2==0:
        print(i)
    else:
        print(i-1)
