l=[2,3,4,5,6]     #adding elements of two lists
m=[5,6,7,8,9]
n=list(zip(l,m))
print(n)
for i in n:
    print(i[0]*i[1])



list=[5,7,6,3,6,35,5,64,25,62,87,74]    #1 return max elements from list
n=int(input('how many max numbers return:'))
def Nmaxelments(list,n):
    return_list = []
    for i in range(n):
        max = 0
        for j in range(len(list)):
            if list[j] > max:
                max = list[j]
        list.remove(max)
        return_list.append(max)
    return return_list

x = Nmaxelments(list,n)
print(x)



list=[5,7,6,3,6,35,5,64,25,62,87,74]       #2 return max elements from list
def Nmaxelements2(list,n):
    return_list =[]
    x = sorted(list,reverse=True)
    for i in range(n):
        return_list.append(x[i])
    return return_list

x = Nmaxelements2(list,2)
print(x)