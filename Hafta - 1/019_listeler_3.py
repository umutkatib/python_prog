araba = ["Audi", "Mercedes", "Porsche", "BMW"]

araba.sort() # alfabetik olarak siraladi
print(araba)

araba.reverse()
print(araba)

def fonksiyon(n):
    return abs(n - 50)

sayi_listesi = [100, 50, 65, 82, 23] # 50,0,15,32,|-27|=27

sayi_listesi.sort() # normal siralama
print(sayi_listesi)

sayi_listesi.sort(key=fonksiyon) # fonksiyona gore siralama
print(sayi_listesi)
