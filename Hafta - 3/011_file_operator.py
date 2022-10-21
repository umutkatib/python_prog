dosya = open("metin.txt", "r")

for satir in dosya:
    print(satir[:-3]) # sondan 3 karakter siler
    print(satir)

