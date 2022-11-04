import sqlite3

bag = sqlite3.connect("ornek.uk")
# tablo baglantisi

cursor = bag.cursor()
# cursor degiskeni veri tabnı uzerinde islem yapcagımız imlec oluyor

cursor.execute("CREATE TABLE IF NOT EXISTS kitap "
               "(id INTEGER NOT NULL PRIMARY KEY,"
               "isim TEXT, yazar TEXT, yayin_evi TEXT, "
               "sayfa_sayisi INT)") #sorgu calistirir

bag.commit() #Sorgunun veritabanı üzerinde geçerli olması için commit işlemi lazim

bag.close() #baglanti koparma