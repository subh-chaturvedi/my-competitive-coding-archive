# cook your dish here
for _ in range(int(input())):
    x=input()
    args= list(x.split(" "))
    N=int(args[0])
    A=int(args[1])
    B=int(args[2])
    C=int(args[3])
    
    if N>B:
        print("NO")
        continue
    
    if A+C>=N:
        print("YES")
    else:
        print("NO")
