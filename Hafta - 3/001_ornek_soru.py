"""
kendisine gönderilen sayılardan sadece palindrom
olanları toplayan
diğerlerini de bu toplamdan çıkaran ve geri
döndüren python fonksiyonunu yazınız.

"""

def palindromHesapla(*palindrom):
    total = 0
    for palindrom in palindrom:
        if str(palindrom) == str(palindrom)[::-1]:
            total += palindrom
        else:
            total -= palindrom
    return total

print(palindromHesapla(20, 30, 58, 40, 12))