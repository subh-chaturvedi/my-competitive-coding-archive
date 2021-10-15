# cook your dish here
for i in range(int(input())):
    x=input()
    args= list(x.split(" "))
    M=int(args[0])
    N=int(args[1])
    K=int(args[2])
    
    z=N*K
    
    if M>z:
        print("YES")
        continue
    print("NO")
