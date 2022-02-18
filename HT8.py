lst = [0, 1, 2, 3, 4, 5]
print(lst)
if len(lst) == 0:
    b = 0
else:
    lst_a = lst[::2]
    a = sum(lst_a)
    b = a * lst[-1]
print(b)
