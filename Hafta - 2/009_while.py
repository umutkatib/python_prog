x = 6

while x < 12:
    x += 1
    if x == 9:
        continue
    if x == 12:
        break
    print(x)
else:
    print("x artik 12 ya da daha buyuk")