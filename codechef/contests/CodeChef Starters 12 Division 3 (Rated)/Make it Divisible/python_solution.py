# cook your dish here
for i in range(int(input())):
    x=int(input())
    
    if x==1:
        print("3")
    else:
        leading=x-2
        zeroes="0"*leading
        print("1"+zeroes+"5")
