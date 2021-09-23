# cook your dish here

#input

n=int(input(""))
anskey=[]
ansgiven=[]
for i in range(0,n):
    x=input("")
    anskey = list(x.split(" "))
    #print(anskey)
    y=input("")
    ansgiven = list(y.split(" "))
    #print(ansgiven)
    if ansgiven.count("1")==anskey.count("1"):
        print("Pass")
    else:
        print("Fail")
