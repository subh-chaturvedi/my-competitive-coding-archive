# cook your dish here
T=int(input())

for i in range(0,T):
    
    x=input("")
    y=input("")
    numbers=list(y.split(" "))
    args= list(x.split(" "))
    N=int(args[0])
    
    
    evens=[]
    odds=[]
    
    for i in numbers:
        i=int(i)
        
        if i%2!=0:
            odds.append(i)
        else:
            evens.append(i)
    
    
    sumd=0 
    
    for i in range(1,len(numbers)+1):
        #print(i,evens,odds,sumd)
        if i%2==0 and len(odds)>0:
            odds.pop()
            sumd=sumd+1
        elif i%2!=0 and len(evens)>0:
            evens.pop()
            sumd=sumd+1 
        
    
    print(sumd)
