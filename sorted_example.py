lst = ['a', 'ab', 'abc', 'ac', [1, 2]]

def my_sort(str_el: str) -> int:
    return len(str_el)
    # if str_el == 'a':
    #     return 1

# print('sorted(lst)', sorted(lst)) # a < b
print('sorted(lst)', sorted(lst, key=len))
print('sorted(lst)', sorted(lst, key=my_sort))

