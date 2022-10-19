def birim_islem(**birim):
    print("Birimin Tipi: ", type(birim))
    print("Birimin Adi: ", birim["ad"])
    print("Birimin Tipi: ", birim["tip"])
    print("Birimin Yili: ", birim["yil"])

birim_islem(ad="Bursa Uludag", tip="Universite", yil="1977")