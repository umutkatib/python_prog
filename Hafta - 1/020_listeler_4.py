sayi_listesi = [5, 8, 15, -4, 2, 13]
x = sayi_listesi # listeyi bir degiskene atadik
print("Degiskene 'atanmis' dizi ----->>>>", x)

sayi_listesi.sort()
print("Sirali hali: ----->>>>", x)

#######################

sayi_listesi = [5, 8, 15, -4, 2, 13]
x = sayi_listesi.copy()
print("Degiskene 'kopyalanmis' dizi: ----->>>>", x)

sayi_listesi.sort()
print("Sirali hali: ----->>>>", x)

