for i in range(1,int(input())):
    print(str(i)*i)

list=[]
list.insert(0,5)
list.insert(1,10)
list.insert(0,6)
print(list)
list.remove(6)
list.append(9)
list.append(1)
print(list)
list.sort()
print(list)
list.pop()
list.reverse()
print(list)

lst=[2,3,4,5,3,5,7]  #remove duplicate elements from the list
m=[]
for i in lst:
    if i not in m:
        m.append(i)
print(m)

list=[45,54,3,44,77,87,56,59]    #return max values from list
n=3
returnlist=[]
x=sorted(list, reverse=True)
for i in range(n):
    returnlist.append(x[i])
print(returnlist)
