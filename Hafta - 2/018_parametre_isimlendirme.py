def topla(*toplancak, fazladan = 0):
    toplam = 0
    for deger in toplancak:
        toplam += deger + fazladan
    return toplam

print(topla(3, 5, 9, 15.2, 36, fazladan=1))