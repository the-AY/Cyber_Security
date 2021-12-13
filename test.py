n=int(input('Enter the no of list element'))
a=0
l=[]
for i in range(0,n):
    m=input()
    l=l.append(m)
    for  j in l:
        a=l.count(j)
        if(a>1):
             for k in range(1,a):
                 l.remove(j)
print(l)