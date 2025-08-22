list = ["a",'b','v','d','e','de']
s=[]
l = list[::-1]
for j in range (1,(len(list)//2)+1):
    a=[]
   
    for i in range(j):
        a.append(l[i])
        # a=a[::-1]