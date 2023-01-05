

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

bag = sqlite3.connect("cripto.vt")
cursor = bag.cursor()

if not os.path.exists("veri"):
    os.mkdir('veri')
    arsiv = zipfile.ZipFile('parite_cikti.zip')
    arsiv.extractall("veri/")

    tumDosyalar = os.listdir("veri")
    pandas_csv_list = []

    for csv_dosya in tum_dosyalar:
        veri = pd.read_csv("veri/" + csv_dosya)
        del veri["volume"]
        veri["parite"] = csv_dosya.split("_")[0]
        pandas_csv_listesi.append(veri)

    birlesmis_csv = pd.concat(pandas_csv_listesi)
    birlesmis_csv.to_csv('hepsi.csv', index=False)
    cursor.execute("CREATE TABLE IF NOT EXISTS parite("
                   + "id INTEGER PRIMARY KEY AUTOINCREMENT,"
                   + "parite TEXT, otime TEXT, open FLOAT, "
                   + "high FLOAT, low FLOAT, close FLOAT);")

    kayitlar = pd.read_csv("hepsi.csv")
    for row in kayitlar.itertuples():
        cursor.execute("INSERT INTO "
                       + "parite(parite,otime,open,high,low,close)"
                       + " VALUES("
                       + "'" + row.parite + "',"
                       + "'" + row.otime + "',"
                       + "" + str(row.open) + ","
                       + "" + str(row.high) + ","
                       + "" + str(row.low) + ","
                       + "" + str(row.close) + ")")

    bag.commit()

parite = input("Parite :")
baslangic_tarih = input("Başlangıç Tarih :")
bitis_tarih = input("Bitiş Tarih :")

sorgu = "SELECT * FROM parite WHERE " \
        "(otime BETWEEN '"+baslangic_tarih+"' " \
        "AND '"+bitis_tarih+"') " \
        "AND parite='"+parite+"'"
cursor.execute(sorgu)
sonuc = cursor.fetchall()
print(sonuc)


bag.close()