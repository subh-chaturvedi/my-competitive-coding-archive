# cook your dish here
n=int(input())

for i in range(0,n):
    x=input("")
    
    args= list(x.split(" "))
    N=int(args[0])
    S=int(args[1])
    
    possiblecases=[]
    maxval=0
    
    for i in range(0,N+1):
        j=S-i
        if j<=N and j>=0 and abs(i-j)>maxval:
            maxval=abs(i-j)
            break
            
    #print(possiblecases)     
    print(maxval)
