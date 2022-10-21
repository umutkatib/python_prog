class sinif:
    metin = ""
    def __init__(self, x):
        self.metin = x

    def __str__(self):
        return "Yazdirilan :" + self.metin

nesne = sinif("helllo")
print(nesne)