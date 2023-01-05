
"""
1 - veri isimli bir klasör oluşturun
2 - zip dsosyasını veri klasörüne çıkartın
3 - zip dosyası içindeki csv dosyalarının tüm içeriğini
    tek bir csv dosyasında birleştirin
    volume olmasın
4 - bu kayıtların tamamını sqlite veritabanına bir tablo
    oluşturarak yükleyin
5 - kullanıcının belirlediği paritenin
    kullanıcının belirlediği aralığının
    kullanıcının belirlediği değerin
    grafiğini çizdirin (veriler sqlite tan çekilecek).
"""



import os
import zipfile
import pandas as pd
import sqlite3
import matplotlib.pyplot as plt

bag = sqlite3.connect("cripto.vt")
cursor = bag.cursor()


parite = "AVAXUSDT"  # input("Parite :")
baslangic_tarih = "2022-02-03"  #  input("Başlangıç Tarih :")
bitis_tarih = "2022-02-04"  # input("Bitiş Tarih :")

sorgu = "SELECT * FROM parite WHERE " \
        "(otime BETWEEN '"+baslangic_tarih+"' " \
        "AND '"+bitis_tarih+"') " \
        "AND parite='"+parite+"'"
cursor.execute(sorgu)
sonuc = cursor.fetchall()
liste_x = []
liste_y = []
for mum in sonuc:
    #print(mum)
    #print(mum[1])
    liste_y.append(mum[6])
    liste_x.append(mum[2])

plt.plot(liste_x, liste_y)
plt.show()
bag.close()