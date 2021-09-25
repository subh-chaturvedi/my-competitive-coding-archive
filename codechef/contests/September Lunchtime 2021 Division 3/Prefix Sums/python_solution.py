# cook your dish here
for i in range(int(input())):
    x=int(input())
    
    if x%4!=0:
        print("NO")
        continue
    else:
        print("YES")
    
    A=[]
    B=[]
    for i in range(0,x//4):
            A.append(i+1)
            A.append(x-i)
    for i in range(x//4,(x//2)):
            B.append(i+1)
            B.append(x-i)
    A.sort()
    B.sort()
    for i in A:
        print(i,end=" ")
    print()
    for i in B:
        print(i,end=" ")
    print()
    
