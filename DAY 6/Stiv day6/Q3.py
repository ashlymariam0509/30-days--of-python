str='hello'
a=len(str)
c=0
for i in range(a):
    if str[i]=='a':
        c+=1
    elif str[i]=='e':
        c+=1
    elif str[i]=='i':
        c+=1
    elif str[i]=='o':
        c+=1
    elif str[i]=='u':
        c+=1
print('number of vowels=',c)