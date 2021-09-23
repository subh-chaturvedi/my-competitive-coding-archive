# cook your dish here
T=int(input())

for i in range(0,T):
    x=input("")
    
    args= list(x.split(" "))
    N=int(args[0])
    A=int(args[1])
    B=int(args[2])
    
    journey=input("")
    time=0
    
    for i in journey:
        if i=="1":
            time=time+B
        if i=="0":
            time=time+A 
    
    print(time)
