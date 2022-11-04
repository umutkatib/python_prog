import csv

baslik = ["sicaklik", "nem", "basinc"]
veri = [[27, 75.5, 9], [30.3, 40, 3]]

with open('sensor-ver.csv',
          'w', encoding='UTF8', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(baslik)
    writer.writerows(veri)
