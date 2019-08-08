str='Narendra44'
print (str.isalnum())
print(any(s.isalpha()for s in str))
print(any(s.isdigit()for s in str))
print(any(s.islower()for s in str))
print(any(s.isupper()for s in str))



from collections import defaultdict
list=[2,3,4,5,3,5,2,3,7,8,9,2,5,1,1,4,8,5]
d = defaultdict(int)
for i in list:
    d[i]+=1
print(d)


x='hi, this is narendra'
y='narendra'
print(x.find(y))
z=x.index(y)
print(z)