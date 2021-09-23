# cook your dish here

n=int(input())

for i in range(0,n):
    x=input("")
    
    args= list(x.split(" "))
    N=int(args[0])
    S=int(args[1])
    
    s=N*(N+1)
    s=s//2
    s=s-S

    if s>=1 and s<=N: 
        print(s)
        continue
    
    print("-1")
