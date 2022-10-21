class sinif:
    x = 5
    y = "dgf"
    z = [2, 5, 9]

    def yazdir(self):
        d = 500
        print(d, self.x)

    def yazdir2(self, t):
        self.yazdir()
        print(t)


nesne = sinif()
nesne.yazdir()
nesne.yazdir2("asdads")
