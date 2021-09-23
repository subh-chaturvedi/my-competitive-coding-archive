# cook your dish here

#input

n=int(input(""))
resp=[]
for i in range(0,n):
    resp.append(input(""))
    
    
#print(n,resp)

def validlang(req):
    newreq=[]
    for i in req:
        if i!=" ":
            newreq.append(i)
    needed=[newreq[0],newreq[1]]
    lang1=[newreq[2],newreq[3]]
    lang2=[newreq[4],newreq[5]]
    final=[]
    for i in needed:
        if i in lang1:
            final.append("A")
        else:
            final.append("B")
    if final[0]!=final[1]:
        return 0
    elif final[0]==final[1] and final[0]=="A":
        return 1
    elif final[0]==final[1] and final[0]=="B":
        return 2 

for i in resp:
    print(validlang(i))
