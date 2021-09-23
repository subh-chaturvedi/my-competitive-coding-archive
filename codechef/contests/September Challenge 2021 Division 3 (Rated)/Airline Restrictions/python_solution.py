# cook your dish here
T=int(input())

for i in range(0,T):
    x=input("")
    
    args= list(x.split(" "))
    A=int(args[0])
    B=int(args[1])
    C=int(args[2])
    D=int(args[3])
    E=int(args[4])
    
    possiblecombo=[[[A,B],[C]],[[A,C],[B]],[[C,B],[A]]]
    #print(possiblecombo)
    
    answer="NO"
    
    for i in possiblecombo:
        if sum(i[0])<=D and sum(i[1])<=E:
            #print(i)
            answer="YES"
            break
    print(answer)
