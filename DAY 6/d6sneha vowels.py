string="Ambulance"
vowels="aeiouAEIOU"
count=0
for i in string:
    if i in vowels:
        count+=1
print(count)