# cook your dish here
for i in range(int(input())):
    x=input()
    args= list(x.split(" "))
    
    nonrainy=args.count("1")
    rainy=args.count("0")
    
    if nonrainy>rainy:
        print("YES")
        continue
    print("NO")
