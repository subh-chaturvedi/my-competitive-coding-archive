# cook your dish here
n=int(input())

for i in range(0,n):
    N=int(input(""))
    
    if N%2==0:
        for i in range(0,N):
            for j in range(0,N):
                print("-1", end=' ')
            print()
    else:
        for i in range(0,N):
            for j in range(0,N):
                if i==j:
                    print("-1", end=' ')
                else:
                    print("1",end=' ')
            print()
    
    

