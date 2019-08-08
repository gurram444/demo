s=input()
s1=s.split(' ')
print('-'.join(s1))



str="narendra"
l=list(str)
l[5]='j'
p="".join(l)
print(p)
st=str[:4]+'j'+str[5:]
print(st)

str1=input('enter string:')
substr=input('substring')
if substr in str1:
    print(len(substr))