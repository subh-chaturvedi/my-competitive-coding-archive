# cook your dish here
T=int(input())

for i in range(0,T):
    x=input("")
    
    args= list(x.split(" "))
    N=int(args[0])
    K=int(args[1])
    L=int(args[2])
    
    y=input("")
    parts= list(y.split(" "))
    yeah=0
    
    if N==1:
        print("Yes")
        continue
    
    if K<0:
        print("No")
        continue
    if int(parts[-1])>int(max(parts[:-1])):
        print("Yes")
        continue    
    
    for i in range(0,L):
        newPart=int(parts[-1])+(i*K)
        if newPart>int(max(parts)):
            print("Yes")
            yeah=1
            break
    if yeah==0:
        print("No")
