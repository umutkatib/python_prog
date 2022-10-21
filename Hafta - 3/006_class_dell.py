class sinif:
    metin = ""
    def __init__(self, x):
        self.metin = x

    def __del__(self):
        print("yikici metot")

nesne = sinif("Helooo")
del nesne