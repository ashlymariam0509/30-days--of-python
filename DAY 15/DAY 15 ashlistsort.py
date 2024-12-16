def is_sorted(lst):
    if len(lst)<= 1:
        return True
    if lst[0] > lst[1]:
        return False
    return is_sorted(lst[1:])
lst=[3,6,1,9]
print(is_sorted(lst))
