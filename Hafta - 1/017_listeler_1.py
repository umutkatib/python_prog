a = [4, 5, 6]
b = [True, 0.3, 4345664564, None, [4, "umut", 7.5]]

print(a)
print(b)
print(b[0])
print(b[4][2])

tr = "turkiye".capitalize()
print(tr)
print(tr[0:4]) # 0 dan 4 e kadar kes

b[4][1] = [8, 55, 4.5, "hello", "world"]
print(b[4][1])
print(b[4][1][4])