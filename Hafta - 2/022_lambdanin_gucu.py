"""
    Sinavda sorulabilir bir sorudur
"""

def my_func(n):
    return lambda x: x * n

katini_al = my_func(2)  # x: x * 2
print(katini_al(3)) # n'e atanir

katini_al = my_func(4)
print(katini_al(2))
