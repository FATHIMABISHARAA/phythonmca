def long(lis):
    max1=len(lis[0])
    temp=lis[0]
    for i in lis:
        if(len(i)>max1):
            max1=len(i)
            temp=i
    print("the word with longest string is",temp,"and longest is",max1)

lis=[]
n=int(input("ENTER THE LIST SIZE"))
for i in range(0,n):
    a=input("enter the word to insert")
    lis.append(a)
print(lis)
long(lis)
