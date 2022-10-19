"""
1 -  Klavyeden girilen 5 tane sayıyı bir listeye atarak
    bunların karelerinden 20 çıktığında ortaya çıkan sonuca
    göre sıralayan
    ve listeyi buna göre yazdıran programı yazınız.
"""

liste = []
for i in range(0, 5):
    liste.append(eval(input()))

def siralama_fonk(x):
    return x * x - 20

liste.sort()
print(liste)

liste.sort(key=siralama_fonk)
print(liste)
