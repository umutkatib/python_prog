sozluk = {
    "Marka": "Audi",
    "Model": "Rs6",
    "Yıl": "2022"
}

print(sozluk)
print(sozluk["Marka"])
print(sozluk["Model"])
print(sozluk["Yıl"])

sozluk["Renk"] = "Mavi"
print(sozluk)
print(sozluk["Renk"])
sozluk["Renk"] = "Beyaz"
print(sozluk)

print(sozluk.keys()) # marka,model,yil
print(sozluk.values()) # audi,rs6,2022

for i in sozluk.keys():
    print(i, ":", sozluk[i])