# cook your dish here
for i in range(int(input())):
    x=input()
    args= list(x.split(" "))
    D=int(args[0])
    L=int(args[1])
    R=int(args[2])
    
    if D>=L and D<=R:
        print("Take second dose now")
        continue
    if D<L:
        print("Too Early")
        continue
    if D>R:
        print("Too Late")
