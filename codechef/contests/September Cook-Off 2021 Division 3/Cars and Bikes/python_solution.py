# cook your dish here
for i in range(int(input())):
    x=int(input())
    
    
    cars=x//4
    left=x-(cars*4)
    bikes=left//2
    leftafter=left-(bikes*2)
    
    if bikes>0:
        print("YES")
    else:
        print("NO")
