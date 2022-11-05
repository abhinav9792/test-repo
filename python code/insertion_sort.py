#insertion sort
j=1
b =[]
a= [6,5,1,3,2]
for j in range(len(a)):
    key =a[j]
    i = j-1
    while (i>0 and a[j]>key):
        a[i+1]= a[i]
        i = j-1
        a[i+1] =key
        b.append(a[i+1])


print(b)



