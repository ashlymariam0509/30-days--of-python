def count_vowels(str):
    if len(str) == 0:
        return 0
    vowels = "aeiouAEIOU"
    if str[0] in vowels:
       return 1 + count_vowels(str[1:])
    else:
        return count_vowels(str[1:])
str=input("Enter the string:")
print(count_vowels(str))